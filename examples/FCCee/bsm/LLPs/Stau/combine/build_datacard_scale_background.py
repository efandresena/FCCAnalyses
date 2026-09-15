#!/usr/bin/env python3
import json
import os
import subprocess

json_limits = {}

# my cuts folder
# input_json = "/afs/desy.de/user/m/mrandria/DUST/output/KV_DV_all/results.json"
# output_dir = "/afs/desy.de/user/m/mrandria/DUST/output/KV_DV_all/datacards"
# limits_dir = "/afs/desy.de/user/m/mrandria/DUST/output/KV_DV_all/limits4years"

# thomas cuts folder'
input_json = "/afs/desy.de/user/m/mrandria/ThomasData/FCCAna/Final/BetaCut/root/results.json"
# output_dir = "/afs/desy.de/user/m/mrandria/ThomasData/FCCAna/Final/BetaCut/combine/datacards"
# limits_dir = "/afs/desy.de/user/m/mrandria/ThomasData/FCCAna/Final/BetaCut/combine/limits4years"

# input_json = "/afs/desy.de/user/m/mrandria/ThomasData/FCCAna/Final/fullset/root/results.json"
output_dir = "/afs/desy.de/user/m/mrandria/DUST/COMBINE/beta/datacards"
limits_dir = "/afs/desy.de/user/m/mrandria/DUST/COMBINE/beta/limits4years"

os.makedirs(output_dir, exist_ok=True)
os.makedirs(limits_dir, exist_ok=True)


# lumi = 2.70e6 / 4 # integrated lumi for 1IP over 4 years in pb^-1
lumi = 0.67e6 / 4  # 1 year 1 IP pb^-1
# lumi = 0.67e6 / 4 / 365  # 1 day 1 IP pb^-1

SCALE_FACTOR = 100    # signal always divided by this in the datacard

# my channels
# channels = ["KV_region", "DV_region"]

# thomas channels
# channels = ["semiLep_KV", "semiLep_DV", "hadronic_KV", "hadronic_DV"]
# full
channels =  ["semiLep_KV", "semiLep_DV", "hadronic_KV", "hadronic_DV", "escaping_Staus", "Beta_Cut"]

backgrounds = [
    "p8_ee_WW_ecm365",
    "p8_ee_ZZ_ecm365",
    "wzp6_ee_nuenueH_Htautau_ecm365",
    "wzp6_ee_bbH_Htautau_ecm365",
    "p8_ee_tt_ecm365",
    "wzp6_ee_tautau_ecm365",
]

signals = [
    # 0.5 m
    'FCCee_120_stau_0.5m_ctau_ecm_365',
    'FCCee_130_stau_0.5m_ctau_ecm_365',
    'FCCee_140_stau_0.5m_ctau_ecm_365',
    'FCCee_150_stau_0.5m_ctau_ecm_365',
    'FCCee_160_stau_0.5m_ctau_ecm_365',
    'FCCee_170_stau_0.5m_ctau_ecm_365',
    'FCCee_180_stau_0.5m_ctau_ecm_365',
    # 1 m
    'FCCee_120_stau_1m_ctau_ecm_365',
    'FCCee_130_stau_1m_ctau_ecm_365',
    'FCCee_140_stau_1m_ctau_ecm_365',
    'FCCee_150_stau_1m_ctau_ecm_365',
    'FCCee_160_stau_1m_ctau_ecm_365',
    'FCCee_170_stau_1m_ctau_ecm_365',
    'FCCee_180_stau_1m_ctau_ecm_365',
    # 2 m
    'FCCee_120_stau_2m_ctau_ecm_365',
    'FCCee_130_stau_2m_ctau_ecm_365',
    'FCCee_140_stau_2m_ctau_ecm_365',
    'FCCee_150_stau_2m_ctau_ecm_365',
    'FCCee_160_stau_2m_ctau_ecm_365',
    'FCCee_170_stau_2m_ctau_ecm_365',
    'FCCee_180_stau_2m_ctau_ecm_365',
    # 5 m
    'FCCee_120_stau_5m_ctau_ecm_365',
    'FCCee_130_stau_5m_ctau_ecm_365',
    'FCCee_140_stau_5m_ctau_ecm_365',
    'FCCee_150_stau_5m_ctau_ecm_365',
    'FCCee_160_stau_5m_ctau_ecm_365',
    'FCCee_170_stau_5m_ctau_ecm_365',
    'FCCee_180_stau_5m_ctau_ecm_365',
    # 10 m
    'FCCee_120_stau_10m_ctau_ecm_365',
    'FCCee_130_stau_10m_ctau_ecm_365',
    'FCCee_140_stau_10m_ctau_ecm_365',
    'FCCee_150_stau_10m_ctau_ecm_365',
    'FCCee_160_stau_10m_ctau_ecm_365',
    'FCCee_170_stau_10m_ctau_ecm_365',
    'FCCee_180_stau_10m_ctau_ecm_365',
    # 20 m
    'FCCee_120_stau_20m_ctau_ecm_365',
    'FCCee_130_stau_20m_ctau_ecm_365',
    'FCCee_140_stau_20m_ctau_ecm_365',
    'FCCee_150_stau_20m_ctau_ecm_365',
    'FCCee_160_stau_20m_ctau_ecm_365',
    'FCCee_170_stau_20m_ctau_ecm_365',
    'FCCee_180_stau_20m_ctau_ecm_365',
    # 50 m
    'FCCee_120_stau_50m_ctau_ecm_365',
    'FCCee_130_stau_50m_ctau_ecm_365',
    'FCCee_140_stau_50m_ctau_ecm_365',
    'FCCee_150_stau_50m_ctau_ecm_365',
    'FCCee_160_stau_50m_ctau_ecm_365',
    'FCCee_170_stau_50m_ctau_ecm_365',
    'FCCee_180_stau_50m_ctau_ecm_365',
]

mc_info = {
    "p8_ee_WW_ecm365": {"N_MC": 25454213, "sigma": 10.7165},
    "p8_ee_ZZ_ecm365": {"N_MC": 1900000, "sigma": 0.643}, 
    "p8_ee_tt_ecm365": {"N_MC": 2700000, "sigma": 0.800}, 
    "wzp6_ee_nuenueH_Htautau_ecm365": {"N_MC": 1200000, "sigma": 0.002},
    "wzp6_ee_bbH_Htautau_ecm365": {"N_MC": 1000000, "sigma": 0.001},
    "wzp6_ee_tautau_ecm365": {"N_MC": 6400000, "sigma": 2.017},
}

# Signal MC - should also be scaled
signal_mc_info = {
    # 0.5 m
    "FCCee_120_stau_0.5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.36360000e-02},
    "FCCee_130_stau_0.5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  6.76073000e-02},
    "FCCee_140_stau_0.5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  5.16252000e-02},
    "FCCee_150_stau_0.5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  3.61405000e-02},
    "FCCee_160_stau_0.5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  2.17642000e-02},
    "FCCee_170_stau_0.5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  9.40847000e-03},
    "FCCee_180_stau_0.5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.77721000e-04},

    # # 1 m
    "FCCee_120_stau_1m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.36360000e-02},
    "FCCee_130_stau_1m_ctau_ecm_365": {"N_MC": 100000, "sigma":  6.76073000e-02},
    "FCCee_140_stau_1m_ctau_ecm_365": {"N_MC": 100000, "sigma":  5.16252000e-02},
    "FCCee_150_stau_1m_ctau_ecm_365": {"N_MC": 100000, "sigma":  3.61405000e-02},
    "FCCee_160_stau_1m_ctau_ecm_365": {"N_MC": 100000, "sigma":  2.17642000e-02},
    "FCCee_170_stau_1m_ctau_ecm_365": {"N_MC": 100000, "sigma":  9.40847000e-03},
    "FCCee_180_stau_1m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.77721000e-04},

    # # 2 m
    "FCCee_120_stau_2m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.36360000e-02},
    "FCCee_130_stau_2m_ctau_ecm_365": {"N_MC": 100000, "sigma":  6.76073000e-02},
    "FCCee_140_stau_2m_ctau_ecm_365": {"N_MC": 100000, "sigma":  5.16252000e-02},
    "FCCee_150_stau_2m_ctau_ecm_365": {"N_MC": 100000, "sigma":  3.61405000e-02},
    "FCCee_160_stau_2m_ctau_ecm_365": {"N_MC": 100000, "sigma":  2.17642000e-02},
    "FCCee_170_stau_2m_ctau_ecm_365": {"N_MC": 100000, "sigma":  9.40847000e-03},
    "FCCee_180_stau_2m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.77721000e-04},

    # # 5 m
    "FCCee_120_stau_5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.36360000e-02},
    "FCCee_130_stau_5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  6.76073000e-02},
    "FCCee_140_stau_5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  5.16252000e-02},
    "FCCee_150_stau_5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  3.61405000e-02},
    "FCCee_160_stau_5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  2.17642000e-02},
    "FCCee_170_stau_5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  9.40847000e-03},
    "FCCee_180_stau_5m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.77721000e-04},

    # # 10 m
    "FCCee_120_stau_10m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.36360000e-02},
    "FCCee_130_stau_10m_ctau_ecm_365": {"N_MC": 100000, "sigma":  6.76073000e-02},
    "FCCee_140_stau_10m_ctau_ecm_365": {"N_MC": 100000, "sigma":  5.16252000e-02},
    "FCCee_150_stau_10m_ctau_ecm_365": {"N_MC": 100000, "sigma":  3.61405000e-02},
    "FCCee_160_stau_10m_ctau_ecm_365": {"N_MC": 100000, "sigma":  2.17642000e-02},
    "FCCee_170_stau_10m_ctau_ecm_365": {"N_MC": 100000, "sigma":  9.40847000e-03},
    "FCCee_180_stau_10m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.77721000e-04},

    # # 20 m
    "FCCee_120_stau_20m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.36360000e-02},
    "FCCee_130_stau_20m_ctau_ecm_365": {"N_MC": 100000, "sigma":  6.76073000e-02},
    "FCCee_140_stau_20m_ctau_ecm_365": {"N_MC": 100000, "sigma":  5.16252000e-02},
    "FCCee_150_stau_20m_ctau_ecm_365": {"N_MC": 100000, "sigma":  3.61405000e-02},
    "FCCee_160_stau_20m_ctau_ecm_365": {"N_MC": 100000, "sigma":  2.17642000e-02},
    "FCCee_170_stau_20m_ctau_ecm_365": {"N_MC": 100000, "sigma":  9.40847000e-03},
    "FCCee_180_stau_20m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.77721000e-04},

    # # 50 m
    "FCCee_120_stau_50m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.36360000e-02},
    "FCCee_130_stau_50m_ctau_ecm_365": {"N_MC": 100000, "sigma":  6.76073000e-02},
    "FCCee_140_stau_50m_ctau_ecm_365": {"N_MC": 100000, "sigma":  5.16252000e-02},
    "FCCee_150_stau_50m_ctau_ecm_365": {"N_MC": 100000, "sigma":  3.61405000e-02},
    "FCCee_160_stau_50m_ctau_ecm_365": {"N_MC": 100000, "sigma":  2.17642000e-02},
    "FCCee_170_stau_50m_ctau_ecm_365": {"N_MC": 100000, "sigma":  9.40847000e-03},
    "FCCee_180_stau_50m_ctau_ecm_365": {"N_MC": 100000, "sigma":  8.77721000e-04},

}


# # scaling all signals with lifetime > 2m : pythia issue
# scale_large_ctau = {
#     "20cm" : 1.0,
#     "50cm" : 1.0,
#     "1m" : 1.0,
#     "2m": 0.9996,
#     "3m": 0.9944,
#     "4m": 0.9795,
#     "6m": 0.9251,
#     "10m": 0.7888,
#     "20m": 0.5404
# }

signals = list(signal_mc_info.keys())

def make_label(s):
    parts = s.split("_")
    return f"sig_{parts[1]}_{parts[3]}"

def extract_mass_lifetime(sig_name):
    parts = sig_name.split("_")
    return parts[1], parts[3]

with open(input_json) as f:
    results = json.load(f)

def get_rate(proc, chan):
    """
    Return expected event yield for proc in chan.
    Both backgrounds and signals use: raw * (sigma * L / N_MC)
    For 0 events left: use 95% CL Poisson upper limit = 3/N_MC * sigma * L
    Signal is additionally divided by SCALE_FACTOR.
    """
    raw = float(results.get(proc, {}).get(chan, {}).get("n_events_raw", 0))

    if proc in mc_info:  # background
        info = mc_info[proc]
        if raw == 0:
            scaled = (3.0 / info["N_MC"]) * info["sigma"] * lumi # this is the upper bond
        else:
            scaled = raw * (info["sigma"] * lumi / info["N_MC"])
            # print(scaled)

    else:  # signal
        info = signal_mc_info[proc]
        # get the lifetime
        # _, lifetime = extract_mass_lifetime(proc)
        # scale_factor_ctau = scale_large_ctau.get(lifetime, 1.0)

        if raw == 0:
            scaled = 0
            # scaled = (3.0 / info["N_MC"]) * info["sigma"] * lumi / SCALE_FACTOR
        else:
            scaled_lumi = raw * (info["sigma"] * lumi / info["N_MC"])
            scaled = scaled_lumi/ SCALE_FACTOR
            
    return max(scaled, 1e-9)


for sig_proc in signals:

    sig_label = make_label(sig_proc)
    print(f"\n[INFO] Processing {sig_label}  (signal divided by {SCALE_FACTOR})")

    obs_per_chan = {ch: sum(get_rate(b, ch) for b in backgrounds) for ch in channels}

    all_proc_names = backgrounds + [sig_label]
    all_proc_keys  = backgrounds + [sig_proc]
    all_proc_nums  = list(range(1, len(backgrounds) + 1)) + [0]

    n_cols = len(channels) * len(all_proc_names)
    fname  = os.path.join(output_dir, f"datacard_{sig_label}.txt")

    with open(fname, "w") as dc:
        dc.write(f"# Datacard for signal: {sig_label}\n")
        dc.write(f"# Signal scaled down by {SCALE_FACTOR} -- multiply r by {SCALE_FACTOR} to get true signal strength\n\n")
        dc.write(f"imax {len(channels)}\n")
        dc.write("jmax *\n")
        dc.write("kmax *\n")
        dc.write("------------\n")

        dc.write("bin".ljust(15)         + "  ".join(channels) + "\n")
        dc.write("observation".ljust(15) + "  ".join(f"{obs_per_chan[c]:.0f}" for c in channels) + "\n")
        dc.write("------------\n")

        col_chans = [c for c in channels for _ in all_proc_names]
        col_keys  = all_proc_keys * len(channels)
        col_names = all_proc_names * len(channels)
        col_nums  = all_proc_nums  * len(channels)

        dc.write("bin".ljust(15)     + "  ".join(col_chans)                + "\n")
        dc.write("process".ljust(15) + "  ".join(col_names)                + "\n")
        dc.write("process".ljust(15) + "  ".join(str(x) for x in col_nums) + "\n")

        rates = [get_rate(k, c) for k, c in zip(col_keys, col_chans)]
        dc.write("rate".ljust(15) + "  ".join(f"{r:.6f}" for r in rates) + "\n")
        dc.write("------------\n")
        dc.write("lumi  lnN  " + "  ".join(["1.02"] * n_cols) + "\n") # considered 2% uncertainity on lumi- integrated
        # lumi uncertainity per day: 3\%

    # Run Combine
    result = subprocess.run(
        ["combine", "-M", "AsymptoticLimits", fname],
        capture_output=True, text=True
    )

    exp0 = exp_m1 = exp_p1 = exp_m2 = exp_p2 = obs = None
    for line in result.stdout.split("\n"):
        if   "Expected 50.0%" in line: exp0   = float(line.split()[-1])
        elif "Expected 16.0%" in line: exp_m1 = float(line.split()[-1])
        elif "Expected 84.0%" in line: exp_p1 = float(line.split()[-1])
        elif "Expected  2.5%" in line: exp_m2 = float(line.split()[-1])
        elif "Expected 97.5%" in line: exp_p2 = float(line.split()[-1])
        elif "Observed Limit:" in line: obs   = float(line.split()[-1])

    if exp0 is None:
        print(f"[WARNING] Combine failed for {sig_label}. stderr:\n{result.stderr}")

    mass, lifetime = extract_mass_lifetime(sig_proc)
    json_limits[f"{mass}_{lifetime}"] = {
        "exp-2": exp_m2 or 0,
        "exp-1": exp_m1 or 0,
        "exp0":  exp0   or 0,
        "exp+1": exp_p1 or 0,
        "exp+2": exp_p2 or 0,
        "obs":   obs    or 0,
    }

json_path = os.path.join(limits_dir, "limits.json") 
with open(json_path, "w") as f:
    json.dump(json_limits, f, indent=2)

print(f"\nAll limits saved to {json_path}")