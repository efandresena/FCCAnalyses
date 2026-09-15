'''
Plotting stage of the Stau analysis
'''
import os
import ROOT
import argparse
# use this : source /cvmfs/sw.hsf.org/key4hep/setup.sh -r 2024-03-10
intLumi        = 0.67e6 / 4 # lumi for 1 year per IP
###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
scaleSig       = 1
scaleBkg       = 1.

ana_tex        = ''
delphesVersion = ''
energy         = 365.
collider       = 'FCC-ee'

# Input/output directories
parser = argparse.ArgumentParser(description="FolderNames")
parser.add_argument("-i", "--input_folder_name", type=str, default="")
parser.add_argument("-o", "--output_folder_name", type=str, default="")

args, _ = parser.parse_known_args()

inputDir       = "/data/dust/user/creusett/SummerSchool/Data/FCCAna/Final/" + args.input_folder_name + "/root/"
outdir         = "/data/dust/user/creusett/SummerSchool/Data/FCCAna/Final/" + args.output_folder_name + "/plots/"
os.makedirs(outdir, exist_ok=True)

formats  = ['png', 'pdf']
yaxis    = ['log', 'lin']
stacksig = ['nostack']

splitLeg = True

# Variables to plots
variables = [
    # ===============================
    # Gen-level stau
    # ===============================
    # "n_GenStau",
    # "GenStau_vx",
    # "GenStau_vy",
    # "GenStau_vz",
    # "GenStau_Lxy",
    # "GenStau_Lxyz",

    # Generated gravitino
    # "GenGravitino_e",
    

    # ===============================
    # Gen taus
    # ===============================
    # "GenTau_e",
    # "GenTau_pt",
    # "GenTau_eta",
    # "GenTau_phi",
    # "GenTau_px",
    # "GenTau_py",
    # "GenTau_pz",
    # "GenTau_vx",
    # "GenTau_vy",
    # "GenTau_vz",
    # "GenTau_cTau",
    # "decayLengthTau",

    # ===============================
    # Final-state muons
    # ===============================
    # "n_FSGenMuon",
    # "FSGenMuon_e",
    # "FSGenMuon_pt",
    # "FSGenMuon_px",
    # "FSGenMuon_py",
    # "FSGenMuon_pz",
    # "FSGenMuon_eta",
    # "FSGenMuon_phi",
    # "FSGenMuon_charge",
    # "FSGenMuon_vx",
    # "FSGenMuon_vy",
    # "FSGenMuon_vz",

    # ===============================
    # Final-state electrons
    # ===============================
    # "n_FSGenElectron",
    # "FSGenElectron_e",
    # "FSGenElectron_pt",
    # "FSGenElectron_px",
    # "FSGenElectron_py",
    # "FSGenElectron_pz",
    # "FSGenElectron_eta",
    # "FSGenElectron_phi",
    # "FSGenElectron_charge",
    # "FSGenElectron_vx",
    # "FSGenElectron_vy",
    # "FSGenElectron_vz",

    # ===============================
    # Final-state neutrinos
    # ===============================
    # "n_FSGenNeutrino",
    # "FSGenNeutrino_e",
    # "FSGenNeutrino_pt",
    # "FSGenNeutrino_px",
    # "FSGenNeutrino_py",
    # "FSGenNeutrino_pz",
    # "FSGenNeutrino_eta",
    # "FSGenNeutrino_phi",

    # Time variables
    # "GenStau_time",
    # "GenTau_time",
    # "FSGenElectron_time",
    # "FSGenMuon_time",
    # "GenTau_status",
    # "GenTau_cTau",

    # ===============================
    # Reco jets
    # ===============================
    # "n_RecoJets",
    # "RecoJet_e",
    # "RecoJet_pt",
    # "RecoJet_px",
    # "RecoJet_py",
    # "RecoJet_pz",
    # "RecoJet_eta",
    # "RecoJet_phi",
    # "RecoJet_charge",

    # ===============================
    # Reco electrons
    # ===============================
    "n_RecoElectrons",
    "RecoElectrons_e",
    "RecoElectrons_p",
    "RecoElectrons_pt",
    "RecoElectrons_px",
    "RecoElectrons_py",
    "RecoElectrons_pz",
    "RecoElectrons_eta",
    "RecoElectrons_phi",
    "RecoElectrons_theta",
    "RecoElectrons_charge",

    # ===============================
    # Reco muons
    # ===============================
    "n_RecoMuons",
    "RecoMuons_e",
    "RecoMuons_p",
    "RecoMuons_pt",
    "RecoMuons_px",
    "RecoMuons_py",
    "RecoMuons_pz",
    "RecoMuons_eta",
    "RecoMuons_phi",
    "RecoMuons_theta",
    "RecoMuons_charge",

    # ===============================
    # Missing energy
    # ===============================
    # "RecoMissingEnergy_e",
    # "RecoMissingEnergy_pt",
    # "RecoMissingEnergy_eta",
    # "RecoMissingEnergy_phi",

    # ===============================
    # Track
    # ===============================
    # "n_AcceptedTracks",
    # "n_RecoTracks",

    # ===============================
    # Reco particles
    # ===============================
    "RecoParticles_firstHitLoc",
    "RecoParticles_lastHitLoc",
    "RecoParticles_nHits",
    "RecoParticles_nDriftChamberHits",

    # ===============================
    # Displaced vertices
    # ===============================
    "nDisplaced_Vertices",
    "n_nonprimary_tracks",

    "invMass_seltracks_DVs",
    # "invMass_seltracks_DVs_zoom",

    "DV_evt_seltracks_chi2",
    "DV_evt_seltracks_normchi2",

    # "sel_tracks_pt_DV",
    # "sel_tracks_D0_DV",
    # "sel_tracks_Z0_DV",

    "nDisplacedVertices_failInnerHitVeto",
    "nTracks_DV_failInnerHitVeto",

    # "Reco_seltracks_DVs_Lxy",
    # "Reco_seltracks_DVs_Lxyz",
    
    # ===============================
    # Recoed Primary Tracks
    # ===============================
    "n_RecoedPrimaryTracks",
    "RecoedPrimaryTracks_theta",
    "RecoedPrimaryTracks_p",
    "RecoedPrimaryTracks_pt",
    "RecoedPrimaryTracks_firstHitLoc",
    "RecoedPrimaryTracks_lastHitLoc",
    "RecoedPrimaryTrack_mass",

    # ===============================
    # Event quantities
    # ===============================
    # "RecoVisibleEnergy",
    # "RecoMissingEnergy3D",

    # ===============================
    # Kink vertices
    # ===============================
    "KinkCandidates_passInnerHitVeto",
    "nKinkCandidates_passVeto",
    "KinkVertex_invMass",
    "KinkVertex_dxy",
    "KinkVertex_d3d",
    "KinkVertex_ntracks",
    "nKinkVertices",
    "KinkAngle",
    "PV2V0Cos",
    
    # ===============================
    # Escaping tracks
    # ===============================
    "n_EscapingTracks",
    "EscapingTracks_pt",
    "EscapingTracks_p",
    "EscapingTracks_theta",
    "EscapingTracks_phi",
    "EscapingTracks_mass",

    # ===============================
    # TOF
    # ===============================
    "TOF_AcceptedTracks",
    "TOF_RecoedPrimaryTracks",
    "TOF_sel_tracks",
    "TOF_EscapingTracks",

]
# Define selections, labels, colors, plots, legends
selections = {}

selections[''] = [
    "selNone",
    "semiLep_KV",
    "semiLep_DV",
    "hadronic_KV",
    "hadronic_DV",
    "escaping",
    "escaping_Staus",
]

extralabel = {}
extralabel['selNone'] = "Before selection"
extralabel["semiLep_KV"] = "Semi-lep + KV"
extralabel["semiLep_DV"] = "Semi-lep + DV"
extralabel["hadronic_KV"] = "Had + KV"
extralabel["hadronic_DV"] = "Had + DV"
extralabel["escaping"] = "Escaping"
extralabel["escaping_Staus"] = "Escaping Staus"

# color_wheel = [

#     # colors from DESY color guide
#     "#E41034",  # Red
#     "#8CBE23",  # Light green
#     "#127604",  # Turquoise
#     "#D2006E",  # Magenta
#     "#917DB9",  # Violet
#     "#C3B700",  # Olive
#     "#FAC800",  # Yellow
#     "#B92D41",  # Dark red
#     "#00A64B",  # Green
#     "#006987",  # Petrol
#     "#8C3C5B",  # Aubergine
#     "#504F8F",  # Purple
#     "#828F2B",  # Dark olive
#     "#004A6F"   # Dark blue
# ]

color_wheel = [
    # ==========================
    # SIGNAL COLORS
    # ==========================

    "#E41A1C",  # Vivid red
    "#FF7F00",  # Vivid orange
    "#F2C500",  # Vivid yellow
    "#4DAF4A",  # Vivid green
    "#00A6A6",  # Vivid teal
    "#00A6D6",  # Vivid cyan
    "#377EB8",  # Vivid blue
    "#5E4FA2",  # Vivid violet
    "#D81B8A",  # Vivid magenta
    "#A65628",  # Vivid brown

    # ==========================
    # BACKGROUND COLORS
    # Pale, distinct, low saturation
    # ==========================

    "#FFF3C4",  # Pale yellow
    "#FDE2C5",  # Pale peach
    "#DDF0D8",  # Pale green
    "#E78587",  # Pale red
    "#DCE8F7",  # Pale blue
    "#E8DDF2",  # Pale violet
]
colors = {}
# =====================================================
# Signal parameters
# =====================================================

# TEST
ctaus = [0.5, 50] # in meters
stau_masses = [150,180]
# All
# ctaus = [0.5, 1, 2, 5, 10, 20, 50]
# stau_masses = [120, 130, 140, 150, 160, 170, 180]

# =====================================================
# Color assignment
# =====================================================

colors = {}

# Convert hex colors to ROOT colors
root_colors = [ROOT.TColor.GetColor(c) for c in color_wheel]

# Assign unique colors to all signal samples
color_index = 0

for ctau in ctaus:
    for mass in stau_masses:
        process = f'FCCee_{mass}_stau_{ctau}m_ctau_ecm_365'
        colors[process] = root_colors[color_index]
        color_index += 1


# =====================================================
# Background colors
# Last 6 colors in color_wheel are yellow/gold
# =====================================================

backgrounds = {
    'p8_ee_WW_ecm365': color_wheel[10],
    'p8_ee_ZZ_ecm365': color_wheel[11],
    'wzp6_ee_nuenueH_Htautau_ecm365': color_wheel[12],
    'wzp6_ee_bbH_Htautau_ecm365': color_wheel[13],
    'p8_ee_tt_ecm365': color_wheel[14],
    'wzp6_ee_tautau_ecm365': color_wheel[15],
}

for process, color in backgrounds.items():
    colors[process] = ROOT.TColor.GetColor(color)

# =====================================================
# Plot and legend structure
# =====================================================

plots = {
    '': {
        'signal': {},
        'backgrounds': {}
    }
}

legend = {}

# Signal plots + legends
for ctau in ctaus:
    for mass in stau_masses:
        process = f'FCCee_{mass}_stau_{ctau}m_ctau_ecm_365'
        plots['']['signal'][process] = [process]
        legend[process] = f'm_{{#tilde{{#tau}}}} = {mass} GeV, c#tau = {ctau} m'

# Background plots + legends
for process in backgrounds:
    plots['']['backgrounds'][process] = [process]

legend['p8_ee_WW_ecm365'] = 'e^{+}e^{-} #rightarrow WW'
legend['p8_ee_ZZ_ecm365'] = 'e^{+}e^{-} #rightarrow ZZ'
legend['wzp6_ee_nuenueH_Htautau_ecm365'] = 'e^{+}e^{-} #rightarrow #nu#nuH, H#rightarrow#tau#tau'
legend['wzp6_ee_bbH_Htautau_ecm365'] = 'e^{+}e^{-} #rightarrow bbH, H#rightarrow#tau#tau'
legend['p8_ee_tt_ecm365'] = 'e^{+}e^{-} #rightarrow tt'
legend['wzp6_ee_tautau_ecm365'] = 'e^{+}e^{-} #rightarrow #tau#tau'


# =====================================================
# Legend formatting
# =====================================================

# Legend inside the plot (x1, y1, x2, y2)
# legendCoord = [0.59, 0.45, 0.89, 0.88]

# Legend outside the plot on the right
leg = ROOT.TLegend(0.75, 0.10, 0.99, 0.90)

# Remove box/background
leg.SetBorderSize(0)
leg.SetFillStyle(0)
