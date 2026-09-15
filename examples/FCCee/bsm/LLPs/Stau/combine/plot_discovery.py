import json
import ROOT
import os
from array import array

colors = [
    ROOT.kRed, ROOT.kBlue, ROOT.kGreen+2, ROOT.kMagenta, ROOT.kOrange,
    ROOT.kCyan+1, ROOT.kPink+1, ROOT.kViolet, ROOT.kTeal+1
]

lifetimes = ["0.5m", "1m","2m", "5m", "10m", "20m", "50m"]
SCALE_FACTOR = 0.01

cross_sections = {
    "120": 8.36226000e-02,
    "130": 6.76073000e-02,
    "140": 5.16252000e-02,
    "150": 3.61405000e-02,
    "160": 2.41349000e-02,
    "170": 1.58984000e-02,
    "180": 8.77581000e-03,
}

masses = ["120", "130", "140", "150", "160", "170", "180"]
xvals  = array('d', [float(m) for m in masses])

# my folder
# limits_dir = "/afs/desy.de/user/m/mrandria/DUST/output/KV_DV_all/limits4years/"
# json_path  = os.path.join(limits_dir, "limits.json")
# plots_dir  = "/afs/desy.de/user/m/mrandria/DUST/output/KV_DV_all/plots"

# BETA 
# input_json = "/afs/desy.de/user/m/mrandria/ThomasData/FCCAna/Final/BetaCut/root/results.json"
plots_dir = "/afs/desy.de/user/m/mrandria/DUST/COMBINE/beta/plots"
limits_dir = "/afs/desy.de/user/m/mrandria/DUST/COMBINE/beta/limits4years"
json_path  = os.path.join(limits_dir, "limits.json")

# thomas cuts folder
# limits_dir = "/afs/desy.de/user/m/mrandria/DUST/COMBINE/limits4years"
# json_path  = os.path.join(limits_dir, "limits.json")
# plots_dir  = "/afs/desy.de/user/m/mrandria/DUST/COMBINE/combine_plots"

os.makedirs(plots_dir, exist_ok=True)

with open(json_path) as f:
    data = json.load(f)

def get_entry(mass, lt):
    key = f"{mass}_{lt}"
    if key not in data:
        raise KeyError(f"Key {key} not found in limits.json")
    return data[key]

L_current = 2.70e6 / 4  # 4 years 1 IP pb^-1
L_1y = 0.67e6 / 4  # 1 year 1 IP pb^-1
L_1d = 0.67e6 / 4 / 365  # 1 day 1 IP pb^-1

# Create canvas for overlay
c = ROOT.TCanvas("c_overlay", "Lumi required for Discovery", 1200, 900)
c.SetLogy()
c.SetGrid()
c.SetTickx()
c.SetTicky()
frame = ROOT.TH2F("frame", "5 #sigma discovery reach; m_{#tilde{#tau}} [GeV]; Required Lumi [pb^{-1}]", 
                  100, 110, 190, 100, 1.1, 1e9)
frame.SetStats(0)
frame.SetMinimum(1.5)
frame.SetMaximum(1e14)
frame.Draw()
c.SetLogy()  # apply log scale after drawing
graphs = []

for idx, lifetime in enumerate(lifetimes):

    exp_y = array('d', [
        get_entry(m, lifetime)["exp0"] * SCALE_FACTOR  * cross_sections[m]
        for m in masses
    ])
    theory_y = array('d', [cross_sections[m] for m in masses])


    lumi_required = []
    for i, m in enumerate(masses):
        sigma_lim = exp_y[i]   # expected limit on sigma at L_current
        sigma_th  = theory_y[i]
        max_L5    = 1e10        # cap at 1e9 pb^-1 (upper plot boundary)
        min_L5    = 1e1       # floor — points below this are "already discoverable"

        if sigma_lim <= 0:
            lumi_required.append(max_L5)
            continue

        # Z at L_current ~ sigma_th / sigma_lim  (Asimov approximation)
        Z_current = sigma_th / sigma_lim
        L5 = L_current * (5.0 / Z_current) ** 2

        # print(f"  mass={m}, ct={lifetime}: sigma_th={sigma_th:.4g} pb, "
        #       f"sigma_lim={sigma_lim:.4g} pb, Z_now={Z_current:.3f}, L5={L5:.3g} pb^-1")

        L5 = max(min_L5, min(L5, max_L5))
        lumi_required.append(L5)

    print()
    lumi_arr = array('d', lumi_required)

    gr = ROOT.TGraph(len(masses), xvals, lumi_arr)
    gr.SetLineColor(colors[idx % len(colors)])
    gr.SetLineWidth(2)
    gr.SetMarkerStyle(20)
    gr.SetMarkerSize(1.0)
    gr.SetMarkerColor(colors[idx % len(colors)])
    gr.Draw("PL same")
    graphs.append((gr, lifetime))

# Horizontal reference line at L_current
ref_line = ROOT.TLine(110, L_current, 190, L_current)
ref_line.SetLineColor(ROOT.kBlack)
ref_line.SetLineStyle(2)
ref_line.SetLineWidth(2)
ref_line.Draw()

ref_label = ROOT.TLatex()
ref_label.SetNDC(False)
ref_label.SetTextSize(0.028)
ref_label.SetTextColor(ROOT.kBlack)
ref_label.DrawLatex(140, L_current * 1.5, "L = 0.67ab^{-1} (4 years, 1 IP)")

# 1-year line
ref_line_1y = ROOT.TLine(110, L_1y, 190, L_1y)
ref_line_1y.SetLineColor(ROOT.kBlue)
ref_line_1y.SetLineStyle(2)
ref_line_1y.SetLineWidth(2)
ref_line_1y.Draw()

ref_label_1y = ROOT.TLatex()
ref_label_1y.SetNDC(False)
ref_label_1y.SetTextSize(0.028)
ref_label_1y.SetTextColor(ROOT.kBlue)
ref_label_1y.DrawLatex(140, L_1y * 0.50, "L = 0.16ab^{-1} (1 year, 1 IP)")

# 1-day line
ref_line_1d = ROOT.TLine(110, L_1d, 190, L_1d)
ref_line_1d.SetLineColor(ROOT.kGreen+2)
ref_line_1d.SetLineStyle(2)
ref_line_1d.SetLineWidth(2)
ref_line_1d.Draw()

ref_label_1d = ROOT.TLatex()
ref_label_1d.SetNDC(False)
ref_label_1d.SetTextSize(0.028)
ref_label_1d.SetTextColor(ROOT.kGreen+2)
ref_label_1d.DrawLatex(140, L_1d * 1.50, "L = 456 pb^{-1} (1 day, 1 IP)")

# Legend
legend = ROOT.TLegend(0.15, 0.60, 0.40, 0.88)
legend.SetBorderSize(0)
legend.SetFillStyle(0)
legend.SetTextSize(0.028)
for gr, lt in graphs:
    legend.AddEntry(gr, f"c#tau = {lt}", "lp")
legend.Draw()

# Labels
label = ROOT.TLatex()
label.SetNDC()
label.SetTextSize(0.035)
label.DrawLatex(0.68, 0.20, "FCC-ee Simulation")
label.DrawLatex(0.68, 0.15, "#sqrt{s} = 365 GeV")

lumi_label = ROOT.TLatex()
lumi_label.SetNDC()
lumi_label.SetTextSize(0.030)
lumi_label.SetTextAlign(31)
# lumi_label.DrawLatex(0.88, 0.12, "L_{ref} = 2.7#times10^{6} pb^{-1} (3 years, 1 IP)")


c.RedrawAxis()
c.Update()

# Save
outfile = os.path.join(plots_dir, "discovery_lumi_all_lifetimes_2003.png")
outfile_pdf = os.path.join(plots_dir, "discovery_lumi_all_lifetimes_2003.pdf")
c.SaveAs(outfile)
c.SaveAs(outfile_pdf)
c.Close()
print(f"Saved overlay plot: {outfile}")