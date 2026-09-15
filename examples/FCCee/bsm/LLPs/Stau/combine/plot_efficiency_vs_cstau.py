import re
import os
from array import array

import ROOT


# ============================================================
# Configuration
# ============================================================

efficiency_path = (
    "/afs/desy.de/user/m/mrandria/ThomasData/FCCAna/Final/fullset/root"
    "/outputTabular.txt"
)

plots_dir = (
    "/afs/desy.de/user/m/mrandria/DUST/COMBINE/"
    "combine_plots/efficiency_plots"
)

os.makedirs(plots_dir, exist_ok=True)


# ============================================================
# Choose masses to plot
# ============================================================

selected_masses = [160]


# ============================================================
# Choose ANY number of selections to plot
#
# The names do NOT need to contain "_region".
# ============================================================

# channels =  ["semiLep_KV", "semiLep_DV", "hadronic_KV", "hadronic_DV", "escaping_Staus"]

selected_selections = [
    "semiLep_KV",
    # "semiLep_DV",
    # "hadronic_KV",
    "hadronic_DV",
    # "escaping",
    "escaping_Staus",
]


# ============================================================
# ROOT style
# ============================================================

ROOT.gROOT.SetBatch(True)

ROOT.gStyle.SetOptStat(0)

ROOT.gStyle.SetTitleFont(42, "XYZ")
ROOT.gStyle.SetLabelFont(42, "XYZ")

ROOT.gStyle.SetTitleSize(0.045, "XYZ")
ROOT.gStyle.SetLabelSize(0.040, "XYZ")

ROOT.gStyle.SetPadLeftMargin(0.13)
ROOT.gStyle.SetPadRightMargin(0.05)
ROOT.gStyle.SetPadBottomMargin(0.12)
ROOT.gStyle.SetPadTopMargin(0.08)


# ============================================================
# Colors
#
# We generate enough colors automatically for an arbitrary
# number of selections.
# ============================================================

colors = [
    ROOT.kRed + 1,
    ROOT.kBlue + 1,
    ROOT.kGreen + 2,
    ROOT.kMagenta + 1,
    ROOT.kOrange + 7,
    ROOT.kCyan + 1,
    ROOT.kViolet + 1,
    ROOT.kTeal + 1,
    ROOT.kPink + 1,
    ROOT.kAzure + 2,
    ROOT.kSpring + 5,
    ROOT.kYellow + 2,
]


# ============================================================
# Marker styles
#
# Markers represent different masses.
# If you use more masses than listed here, the styles cycle.
# ============================================================

marker_styles = [
    20,   # circle
    21,   # square
    22,   # triangle
    23,   # diamond
    29,   # star
    33,   # cross
    34,
    47,
]


# ============================================================
# Read file
# ============================================================

with open(efficiency_path, "r") as f:
    text = f.read()


if "Efficiency:" not in text:
    raise RuntimeError(
        "Could not find 'Efficiency:' in the file."
    )

efficiency_text = text.split(
    "Efficiency:",
    1
)[1]


# ============================================================
# Extract Efficiency table
# ============================================================

table_match = re.search(
    r"\\begin\{table\}.*?\\end\{table\}",
    efficiency_text,
    re.DOTALL
)

if not table_match:
    raise RuntimeError(
        "Could not find the Efficiency table."
    )

table_text = table_match.group(0)


# ============================================================
# Find header
# ============================================================

header_line = None

for line in table_text.splitlines():

    if "FCCee_120_stau" in line:

        header_line = line
        break


if header_line is None:
    raise RuntimeError(
        "Could not find the efficiency table header."
    )


header_line = header_line.replace(
    r"\hline",
    ""
)

header_parts = [
    x.strip()
    for x in header_line.split("&")
]

# First column = selection name
header = [
    x for x in header_parts[1:]
    if x
]

print(
    f"Found {len(header)} process columns."
)


# ============================================================
# Find ALL efficiency rows
#
# IMPORTANT:
# We no longer require "_region".
#
# Every row whose first field is not empty is considered
# a possible selection row.
# ============================================================

efficiency_rows = {}

for line in table_text.splitlines():

    line = line.strip()

    # Ignore non-data lines
    if not line:
        continue

    if "&" not in line:
        continue

    # Remove LaTeX commands
    clean_line = line.replace(
        r"\hline",
        ""
    ).strip()

    parts = [
        x.strip()
        for x in clean_line.split("&")
    ]

    if len(parts) < 2:
        continue

    selection = parts[0].strip()

    # Ignore LaTeX/table commands
    if not selection:
        continue

    if selection.startswith(r"\_"):
        continue

    # The header starts with an empty field, so it is
    # automatically excluded by checking for "FCCee..."
    if "FCCee_" in selection:
        continue

    # Store the row
    efficiency_rows[selection] = parts[1:]


# ============================================================
# Print available selections
# ============================================================

print("\nAvailable selections:")

for selection in efficiency_rows:
    print(
        f"  {selection}"
    )


# ============================================================
# Check requested selections
# ============================================================

for selection in selected_selections:

    if selection not in efficiency_rows:

        raise RuntimeError(
            f"\nSelection '{selection}' was not found "
            f"in the efficiency table.\n\n"
            f"Available selections are:\n"
            + "\n".join(
                f"  - {x}"
                for x in efficiency_rows
            )
        )


# ============================================================
# Signal pattern
# ============================================================

signal_pattern = re.compile(
    r"^FCCee_(\d+)_stau_([\d.]+)m_ctau_ecm_365$"
)


# ============================================================
# Parse signal columns
# ============================================================

signals = []

for index, process in enumerate(header):

    process = process.strip()

    match = signal_pattern.match(
        process
    )

    if not match:
        # Background process
        continue

    mass = int(
        match.group(1)
    )

    lifetime = float(
        match.group(2)
    )

    signals.append({
        "index": index,
        "process": process,
        "mass": mass,
        "lifetime": lifetime
    })


print(
    f"\nFound {len(signals)} signal points."
)


# ============================================================
# Build efficiency dictionary
#
# efficiency[selection][mass][lifetime]
# ============================================================

efficiency = {}

for selection, values in efficiency_rows.items():

    efficiency[selection] = {}

    for signal in signals:

        index = signal["index"]

        if index >= len(values):
            continue

        value_string = values[index]

        value_string = (
            value_string
            .replace(r"\hline", "")
            .replace("\\\\", "")
            .strip()
        )

        if not value_string:
            continue

        try:
            value = float(
                value_string
            )

        except ValueError:
            continue

        mass = signal["mass"]
        lifetime = signal["lifetime"]

        efficiency[
            selection
        ].setdefault(
            mass,
            {}
        )

        efficiency[
            selection
        ][mass][lifetime] = value


# ============================================================
# Get lifetime values
# ============================================================

all_lifetimes = set()

for selection in selected_selections:

    for mass in selected_masses:

        if mass not in efficiency[selection]:
            continue

        all_lifetimes.update(
            efficiency[
                selection
            ][mass].keys()
        )


lifetimes = sorted(
    all_lifetimes
)


if not lifetimes:
    raise RuntimeError(
        "No lifetime points were found for the "
        "requested selections/masses."
    )


# ============================================================
# Print what will actually be plotted
# ============================================================

print("\nPlotting:")

for selection in selected_selections:

    print(
        f"\n{selection}:"
    )

    for mass in selected_masses:

        if mass not in efficiency[selection]:
            print(
                f"  m = {mass}: no data"
            )
            continue

        available = sorted(
            efficiency[
                selection
            ][mass].keys()
        )

        print(
            f"  m = {mass}: "
            f"{len(available)} lifetime points"
        )


# ============================================================
# Create ONE combined plot
# ============================================================

canvas = ROOT.TCanvas(
    "c_efficiency",
    "Efficiency",
    1200,
    900
)

canvas.SetGrid()
canvas.SetTickx()
canvas.SetTicky()


# ============================================================
# Frame
# ============================================================

xmin = min(lifetimes)
xmax = max(lifetimes)

# Add some space on both sides
xmin_plot = max(
    0.0,
    xmin - 0.05 * (xmax - xmin)
)

xmax_plot = (
    xmax + 0.05 * (xmax - xmin)
)


frame = ROOT.TH2F(
    "frame",
    "Signal region selection efficiency;"
    "c#tau [m];"
    "Efficiency",
    100,
    xmin_plot,
    xmax_plot,
    100,
    0.0,
    1.0
)

frame.SetStats(0)

frame.SetMinimum(0.0)
frame.SetMaximum(1.0)

frame.GetXaxis().SetTitle(
    "c#tau [m]"
)

frame.GetYaxis().SetTitle(
    "Efficiency"
)

frame.GetXaxis().SetTitleSize(
    0.045
)

frame.GetYaxis().SetTitleSize(
    0.045
)

frame.GetXaxis().SetLabelSize(
    0.040
)

frame.GetYaxis().SetLabelSize(
    0.040
)

frame.Draw()


# ============================================================
# Create automatic color assignment
#
# One color = one selection
# One marker = one mass
# ============================================================

selection_colors = {}

for i, selection in enumerate(
    selected_selections
):

    selection_colors[selection] = colors[
        i % len(colors)
    ]


mass_markers = {}

for i, mass in enumerate(
    selected_masses
):

    mass_markers[mass] = marker_styles[
        i % len(marker_styles)
    ]


# ============================================================
# Draw curves
# ============================================================

graphs = []


for selection in selected_selections:

    color = selection_colors[
        selection
    ]

    for mass in selected_masses:

        if mass not in efficiency[selection]:
            continue

        mass_data = efficiency[
            selection
        ][mass]

        x_values = []
        y_values = []

        for lifetime in sorted(
            mass_data
        ):

            x_values.append(
                lifetime
            )

            y_values.append(
                mass_data[lifetime]
            )

        if not x_values:
            continue

        x_array = array(
            "d",
            x_values
        )

        y_array = array(
            "d",
            y_values
        )

        graph = ROOT.TGraph(
            len(x_values),
            x_array,
            y_array
        )

        # --------------------------------------------
        # Color = selection
        # --------------------------------------------

        graph.SetLineColor(
            color
        )

        graph.SetMarkerColor(
            color
        )

        # --------------------------------------------
        # Marker = mass
        # --------------------------------------------

        graph.SetMarkerStyle(
            mass_markers[mass]
        )

        graph.SetMarkerSize(
            1.1
        )

        graph.SetLineWidth(
            2
        )

        graph.Draw(
            "PL SAME"
        )

        graphs.append(
            (
                graph,
                selection,
                mass
            )
        )


# ============================================================
# Selection display names
#
# Optional: make the legend prettier.
# ============================================================

selection_labels = {

    "selNone":
        "No selection",

    "semiLep_KV":
        "Semi-leptonic, KV",

    "semiLep_DV":
        "Semi-leptonic, DV",

    "hadronic_KV":
        "Hadronic, KV",

    "hadronic_DV":
        "Hadronic, DV",

    "escaping":
        "Escaping",

    "escaping_Staus":
        "Escaping staus",
}


# ============================================================
# Legend
#
# With many selections/masses, make the legend larger.
# ============================================================

legend = ROOT.TLegend(
    0.15,
    0.50,
    0.48,
    0.88
)

legend.SetBorderSize(0)
legend.SetFillStyle(0)
legend.SetTextSize(0.024)


for graph, selection, mass in graphs:

    selection_label = selection_labels.get(
        selection,
        selection
    )

    legend.AddEntry(
        graph,
        (
            f"{selection_label}, "
            f"m_{{#tilde{{#tau}}}} = {mass} GeV"
        ),
        "lp"
    )


legend.Draw()


# ============================================================
# FCC-ee labels
# ============================================================

label = ROOT.TLatex()

label.SetNDC()
label.SetTextSize(0.035)

label.DrawLatex(
    0.70,
    0.33,
    "FCC-ee Simulation"
)

label.DrawLatex(
    0.70,
    0.29,
    "#sqrt{s} = 365 GeV"
)


# ============================================================
# Redraw
# ============================================================

canvas.RedrawAxis()
canvas.Update()


# ============================================================
# Save PNG
# ============================================================

selection_string = "_".join(
    selected_selections
)

mass_string = "_".join(
    str(m)
    for m in selected_masses
)

outfile = os.path.join(
    plots_dir,
    f"efficiency_{selection_string}_{mass_string}.png"
)
outfile_pdf = os.path.join(
    plots_dir,
    f"efficiency_{selection_string}_{mass_string}.pdf"
)
canvas.SaveAs(
    outfile
)

canvas.SaveAs(
    outfile_pdf
)
canvas.Close()
# ============================================================
# Final message
# ============================================================

print("\n" + "=" * 70)

print(
    f"Selected selections: "
    f"{len(selected_selections)}"
)

print(
    f"Selected masses: "
    f"{len(selected_masses)}"
)

print(
    f"Saved: {outfile}"
)

print("=" * 70)