import re
import os


# ============================================================
# Configuration
# ============================================================

input_file = (
    "/afs/desy.de/user/m/mrandria/ThomasData/FCCAna/Final/fullset/root/outputTabular.txt"
)

output_file = (
    "/afs/desy.de/user/m/mrandria/DUST/COMBINE/proper_latex.txt"
)


# ------------------------------------------------------------
# Signals to put in the table
# ------------------------------------------------------------

masses = [120, 140, 170, 180]
lifetimes = ["0.5m", "5m", "20m"]

# Selection columns to include in the output table.
# Keep the names exactly as they appear in outputTabular.txt.
selected_columns = [
    "semiLep_KV",
    "semiLep_DV",
    "hadronic_KV",
    "hadronic_DV",
    "escaping_Staus",
]


# ------------------------------------------------------------
# Backgrounds
# ------------------------------------------------------------

backgrounds = [
    "p8_ee_WW_ecm365",
    "p8_ee_ZZ_ecm365",
    "wzp6_ee_nuenueH_Htautau_ecm365",
    "wzp6_ee_bbH_Htautau_ecm365",
    "p8_ee_tt_ecm365",
    "wzp6_ee_tautau_ecm365",
]


# ============================================================
# Formatting
# ============================================================

def latex_escape(value):
    return value.replace(
        "_",
        r"\_"
    )


def format_yield(value):
    """
    Convert the yield from outputTabular.txt into
    a clean number for the LaTeX table.

    The uncertainty is removed.

    Examples:
        5.84e+03 +/- ...  -> 5840
        3.50e+03 +/- ...  -> 3500
        0.                 -> 0
    """

    if value is None:
        return "--"

    value = value.strip()

    # Remove everything after the uncertainty
    # e.g. "5.84e+03 $\\pm$ 1.88e+01"
    value = re.split(
        r"\s*\$?\\pm\$?",
        value
    )[0].strip()

    if value in ("0.", "0", "0.0"):
        return "0"

    try:
        number = float(value)
    except ValueError:
        return "--"

    # Use integer representation for event yields
    if number >= 1:
        return f"{number:.0f}"

    return f"{number:.3g}"


# ============================================================
# Read file
# ============================================================

with open(input_file, "r") as f:
    text = f.read()


# ============================================================
# Extract Yields section
# ============================================================

if "Yields:" not in text:
    raise RuntimeError(
        "Could not find 'Yields:' in outputTabular.txt"
    )

yields_text = text.split(
    "Yields:",
    1
)[1]


# ============================================================
# Find Yields table
# ============================================================

table_match = re.search(
    r"\\begin\{table\}.*?\\end\{table\}",
    yields_text,
    re.DOTALL
)

if not table_match:
    raise RuntimeError(
        "Could not find the Yields table."
    )

table_text = table_match.group(0)


# ============================================================
# Find header automatically
# ============================================================

header = None

for line in table_text.splitlines():

    if "selNone" in line:

        clean_line = line.replace(
            r"\hline",
            ""
        )
        clean_line = re.sub(r"\\\\\s*$", "", clean_line)

        header = [
            x.strip()
            for x in clean_line.split("&")
            if x.strip()
        ]

        break


if header is None:
    raise RuntimeError(
        "Could not find the Yields table header."
    )


print("\nFound columns:")
for i, column in enumerate(header):
    print(f"  {i}: {column}")


# ============================================================
# Determine selection columns
# ============================================================

if "selNone" not in header:
    raise RuntimeError(
        "The Yields table does not contain 'selNone'."
    )


sel_none_index = header.index(
    "selNone"
)


# Everything after selNone is considered a cut.
#
# Example:
#
# All events | selNone | semiLeptonic | KV_region | DV_region
#
# becomes:
#
# Before selection | Cuts 1 | Cuts 2 | Cuts 3
#

available_cut_columns = header[
    sel_none_index + 1:
]

missing_columns = [
    column
    for column in selected_columns
    if column not in available_cut_columns
]

if missing_columns:
    raise RuntimeError(
        "Selected columns were not found in outputTabular.txt: "
        + ", ".join(missing_columns)
    )

cut_columns = selected_columns


print("\nCuts found:")

for i, cut in enumerate(
    cut_columns,
    start=1
):
    print(
        f"  Cuts {i}: {cut}"
    )


# ============================================================
# Parse yield rows
# ============================================================

yields = {}

for line in table_text.splitlines():

    line = line.strip()

    # Only process actual data rows
    if not (
        line.startswith("FCCee_")
        or line.startswith("p8_")
        or line.startswith("wzp6_")
    ):
        continue

    line = line.replace(
        r"\hline",
        ""
    )
    line = re.sub(
        r"\\\\\s*$",
        "",
        line
    )

    parts = [
        x.strip()
        for x in line.split("&")
    ]

    if len(parts) < len(header):
        print(
            f"WARNING: skipping malformed row:\n{line}"
        )
        continue

    process = parts[0]

    # Store ALL selection values dynamically
    yields[process] = {}

    for i, column in enumerate(
        header,
        start=1
    ):

        yields[process][column] = parts[i]


# ============================================================
# Signal process name
# ============================================================

def signal_name(mass, lifetime):

    return (
        f"FCCee_{mass}_stau_"
        f"{lifetime}_ctau_ecm_365"
    )


# ============================================================
# Check available processes
# ============================================================

print("\n" + "=" * 70)
print("Signals found")
print("=" * 70)

for process in yields:

    if process.startswith("FCCee_"):
        print(
            f"  {process}"
        )


print("\n" + "=" * 70)
print("Backgrounds")
print("=" * 70)

for process in backgrounds:

    if process in yields:
        print(
            f"  {process}"
        )
    else:
        print(
            f"  {process}  <-- NOT FOUND"
        )


# ============================================================
# Build LaTeX
# ============================================================

latex = []


# ------------------------------------------------------------
# Number of columns
#
# 1 process column
# + 1 before-selection column
# + N cuts
# ------------------------------------------------------------

n_columns = (
    2 + len(cut_columns)
)


column_format = (
    "|l|"
    + "c|" * (n_columns - 1)
)


latex.append(
    r"\begin{table}[ht]"
)

latex.append(
    r"    \centering"
)

latex.append(
    r"    \caption{Event yields after applying different independent selection cuts.}"
)

latex.append(
    r"    \vspace{.5em}"
)

latex.append(
    r"    \renewcommand{\arraystretch}{1.3}"
)

latex.append(
    f"    \\begin{{tabular}}{{{column_format}}}"
)

latex.append(
    r"        \hline"
)


# ============================================================
# Header
# ============================================================

header_latex = [
    "Process",
    "Before selection",
]

for cut in cut_columns:
    header_latex.append(
        latex_escape(cut)
    )


latex.append(
    "        "
    + " & ".join(header_latex)
    + r" \\"
)

latex.append(
    r"        \hline"
)


# ============================================================
# Signal rows
# ============================================================

for lifetime in lifetimes:

    for mass in masses:

        process = signal_name(
            mass,
            lifetime
        )

        row = [
            f"Stau\\_{mass}\\_{lifetime}"
        ]

        if process in yields:

            # Before selection = selNone
            row.append(
                format_yield(
                    yields[process]["selNone"]
                )
            )

            # Add ALL cuts dynamically
            for cut in cut_columns:

                row.append(
                    format_yield(
                        yields[process].get(
                            cut
                        )
                    )
                )

        else:

            # Process not available
            row.extend(
                ["--"] * (
                    1 + len(cut_columns)
                )
            )

        latex.append(
            "        "
            + " & ".join(row)
            + r" \\"
        )

    latex.append(
        r"        \hline"
    )


# ============================================================
# Background header
# ============================================================

latex.append(
    f"        \\multicolumn{{{n_columns}}}"
    r"{|c|}{Background processes} \\"
)

latex.append(
    r"        \hline"
)


# ============================================================
# Background rows
# ============================================================

for process in backgrounds:

    row = [
        latex_escape(re.sub(
            r"^(?:p8_|wzp6_)|_ecm365$",
            "",
            process
        ))
    ]

    if process in yields:

        # Before selection
        row.append(
            format_yield(
                yields[process]["selNone"]
            )
        )

        # All cuts
        for cut in cut_columns:

            row.append(
                format_yield(
                    yields[process].get(
                        cut
                    )
                )
            )

    else:

        row.extend(
            ["--"] * (
                1 + len(cut_columns)
            )
        )

    latex.append(
        "        "
        + " & ".join(row)
        + r" \\"
    )


# ============================================================
# Finish table
# ============================================================

latex.append(
    r"        \hline"
)

latex.append(
    r"    \end{tabular}"
)

latex.append(
    r"\end{table}"
)


# ============================================================
# Write file
# ============================================================

with open(
    output_file,
    "w"
) as f:

    f.write(
        "\n".join(latex)
    )


# ============================================================
# Summary
# ============================================================

print("\n" + "=" * 70)
print("LaTeX table generated successfully")
print("=" * 70)

print(
    f"Number of cuts: {len(cut_columns)}"
)

for i, cut in enumerate(
    cut_columns,
    start=1
):

    print(
        f"  Cuts {i} = {cut}"
    )

print()
print(
    f"Output: {output_file}"
)
