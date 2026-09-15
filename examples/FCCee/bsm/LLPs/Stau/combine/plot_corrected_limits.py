import json
import ROOT
import os
from array import array

pastel_green  = ROOT.TColor.GetColor("#A6CEE3")
pastel_yellow = ROOT.TColor.GetColor("#FFF2A8")

lifetimes = ["0.5m", "1m", "2m", "5m", "10m", "20m", "50m"]

SCALE_FACTOR = 0.001 # taken from datacards

cross_sections = {
    "120": 8.36226000e-02,
    "130": 6.76073000e-02,
    "140": 5.16252000e-02,
    "150": 3.61405000e-02,
    "160": 2.17642000e-02,
    "170": 9.40847000e-03,
    "180": 8.77721000e-04,
}

masses = ["120", "130", "140", "150", "160", "170", "180"]
xvals  = array('d', [float(m) for m in masses])

# plots_dir  = "/afs/desy.de/user/m/mrandria/DUST/output/KV_DV_all/plots"
# limits_dir = "/afs/desy.de/user/m/mrandria/DUST/output/KV_DV_all/limits4years"
# json_path  = os.path.join(limits_dir, "limits.json")

# thomas cuts folder
plots_dir = "/afs/desy.de/user/m/mrandria/DUST/COMBINE/beta/plots"
limits_dir = "/afs/desy.de/user/m/mrandria/DUST/COMBINE/beta/limits4years"
json_path  = os.path.join(limits_dir, "limits.json")


# output_dir = "/afs/desy.de/user/m/mrandria/DUST/output/thomas_cuts/friday/datacards"
# limits_dir = "/afs/desy.de/user/m/mrandria/DUST/COMBINE/limits4years"
# json_path  = os.path.join(limits_dir, "limits.json")
# plots_dir  = "/afs/desy.de/user/m/mrandria/DUST/COMBINE/combine_plots"

os.makedirs(plots_dir, exist_ok=True)

with open(json_path) as f:
    data = json.load(f)

# For each mass, look up the entry for this lifetime
def get_entry(mass, lt):
    key = f"{mass}_{lt}"
    if key not in data:
        raise KeyError(f"Key {key} not found in limits.json")
    return data[key]

for lifetime in lifetimes:

    def sigma_limit(mass, key): # rescale the limits with the scalefactor
        entry = get_entry(mass, lifetime)
        return entry[key] * SCALE_FACTOR * cross_sections[mass]

    n = len(masses)

    # obs_y  = array('d', [sigma_limit(m, "obs")   for m in masses])
    exp_y  = array('d', [sigma_limit(m, "exp0")  for m in masses])
    exp_m1 = array('d', [sigma_limit(m, "exp-1") for m in masses])
    exp_p1 = array('d', [sigma_limit(m, "exp+1") for m in masses])
    exp_m2 = array('d', [sigma_limit(m, "exp-2") for m in masses])
    exp_p2 = array('d', [sigma_limit(m, "exp+2") for m in masses])

    # Theory curve — one point per mass
    theory_y = array('d', [cross_sections[m] for m in masses])

    # Graph
    # gr_obs    = ROOT.TGraph(n, xvals, obs_y)
    gr_exp    = ROOT.TGraph(n, xvals, exp_y)
    gr_theory = ROOT.TGraph(n, xvals, theory_y)

    gr_1sigma = ROOT.TGraph(2*n)
    for i in range(n):
        gr_1sigma.SetPoint(i,       xvals[i], exp_p1[i])
        gr_1sigma.SetPoint(2*n-i-1, xvals[i], exp_m1[i])
    gr_1sigma.SetFillColor(pastel_yellow)

    gr_2sigma = ROOT.TGraph(2*n)
    for i in range(n):
        gr_2sigma.SetPoint(i,       xvals[i], exp_p2[i])
        gr_2sigma.SetPoint(2*n-i-1, xvals[i], exp_m2[i])
    gr_2sigma.SetFillColor(pastel_green)

    # canvas
    c = ROOT.TCanvas("c", "Brazil plot vs mass", 1200, 900)
    c.SetLogy()

    if lifetime == "0.5m":
        lifetime = "50cm"
    gr_2sigma.SetTitle(
        f"Long-lived #tilde{{#tau}} in GMSB (c#tau = {lifetime});"
        "m_{#tilde{#tau}} [GeV];"
        "95% CL limit on #sigma [pb]"
    )

    gr_2sigma.Draw("AF") # fill the polygon- this gets the 2sig band
    gr_2sigma.GetXaxis().SetRangeUser(115, 185)
    gr_2sigma.GetYaxis().SetRangeUser(1e-7, 70.0)

    gr_1sigma.Draw("F same") # on same canvas get the 1sig band

    gr_exp.SetLineStyle(2)
    gr_exp.SetLineWidth(2)
    gr_exp.Draw("L same") # draw line between points in the same canvas

    # gr_obs.SetMarkerStyle(20)
    # gr_obs.SetLineWidth(3)
    # gr_obs.Draw("PL same") # markers and line

    gr_theory.SetLineColor(ROOT.kRed)
    gr_theory.SetLineWidth(3)
    gr_theory.SetLineStyle(1)
    gr_theory.Draw("L same") # line

    # legend
    legend = ROOT.TLegend(0.70, 0.70, 0.88, 0.88) #x1, y1, x2, y2
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    # legend.AddEntry(gr_obs,    "Observed",            "pl")
    legend.AddEntry(gr_exp,    "Expected",            "l")
    legend.AddEntry(gr_1sigma, "Expected #pm1#sigma", "f")
    legend.AddEntry(gr_2sigma, "Expected #pm2#sigma", "f")
    legend.AddEntry(gr_theory, "Theory #sigma",       "l")
    legend.Draw()

    label = ROOT.TLatex()
    label.SetNDC()
    label.SetTextSize(0.035)
    label.DrawLatex(0.18, 0.85, "FCC-ee Simulation")
    label.DrawLatex(0.18, 0.80, "#sqrt{s} = 365 GeV")

    lumi_label = ROOT.TLatex()
    lumi_label.SetNDC()
    lumi_label.SetTextSize(0.035)
    lumi_label.SetTextAlign(31)  # right-aligned
    lumi_label.DrawLatex(0.88, 0.15, "L = 0.67ab^{-1} (4 years, 1 IP)")  # Adjust the position as needed
    # lumi_label.DrawLatex(0.88, 0.15, "L = 2.7e6 pb^{-1} (3 years, 1 IP)")
    # lumi_label.DrawLatex(0.88, 0.15, "L = 0.9e6 pb^{-1} (1 year, 1 IP)")
    # lumi_label.DrawLatex(0.88, 0.15, "L = 6480 pb^{-1} (1 day, 1 IP)")


    # save the file
    # plots_dir = "/afs/desy.de/user/m/mrandria/DUST/output/KV_DV_all/plots"
    outfile = os.path.join(plots_dir, f"brazil_plot_lifetime_all_channels_{lifetime}.png")
    outfile_pdf = os.path.join(plots_dir, f"brazil_plot_lifetime_all_channels_{lifetime}.pdf")
    c.SaveAs(outfile)
    c.SaveAs(outfile_pdf)
    c.Close()
    print(f"Saved: {outfile}")