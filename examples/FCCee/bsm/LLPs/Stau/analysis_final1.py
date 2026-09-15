'''
Final stage of the stau analysis
'''
import argparse
import os

parser = argparse.ArgumentParser(description="FolderNames")
parser.add_argument("-o", "--output_folder_name", type=str, default="")

args, _ = parser.parse_known_args()

inputDir       = "/afs/desy.de/user/m/mrandria/DUST/STAGE1"
outputDir      = "/afs/desy.de/user/m/mrandria/DUST/FINAL/" + args.output_folder_name + "/"

os.makedirs(outputDir, exist_ok=True)

# inputDir  = "/data/dust/user/creusett/SummerSchool/Data/FCCAna/Stage1"
# outputDir = "/afs/desy.de/user/m/mrandria/DUST/output/" + args.output_folder_name + "/"

# List of datasets used in the analysis
processList = {
        ###################################################
        #                     SIGNAL                      #
        ###################################################
        ###################################################
        #             FCCee: 365 GeV - 0.5 m                #
        # ###################################################
        # 'FCCee_120_stau_0.5m_ctau_ecm_365': {'fraction': 1.0},
        'FCCee_130_stau_0.5m_ctau_ecm_365': {'fraction': 1.0},
        # 'FCCee_140_stau_0.5m_ctau_ecm_365': {'fraction': 1.0},
        # "FCCee_150_stau_0.5m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_160_stau_0.5m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_170_stau_0.5m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_180_stau_0.5m_ctau_ecm_365": {'fraction': 1.0},

        # ###################################################
        # #             FCCee: 365 GeV - 1 m                #
        # # ###################################################
        # 'FCCee_120_stau_1m_ctau_ecm_365': {'fraction': 1.0},
        # 'FCCee_130_stau_1m_ctau_ecm_365': {'fraction': 1.0},
        # 'FCCee_140_stau_1m_ctau_ecm_365': {'fraction': 1.0},
        # "FCCee_150_stau_1m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_160_stau_1m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_170_stau_1m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_180_stau_1m_ctau_ecm_365": {'fraction': 1.0},

        # ###################################################
        # #             FCCee: 365 GeV - 2 m                #
        # # ###################################################
        # 'FCCee_120_stau_2m_ctau_ecm_365': {'fraction': 1.0},
        # 'FCCee_130_stau_2m_ctau_ecm_365': {'fraction': 1.0},
        # 'FCCee_140_stau_2m_ctau_ecm_365': {'fraction': 1.0},        
        # "FCCee_150_stau_2m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_160_stau_2m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_170_stau_2m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_180_stau_2m_ctau_ecm_365": {'fraction': 1.0},


        # ###################################################
        # #             FCCee: 365 GeV - 5 m                #
        # # ###################################################
        # 'FCCee_120_stau_5m_ctau_ecm_365': {'fraction': 1.0},
        # 'FCCee_130_stau_5m_ctau_ecm_365': {'fraction': 1.0},
        # 'FCCee_140_stau_5m_ctau_ecm_365': {'fraction': 1.0},        
        # "FCCee_150_stau_5m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_160_stau_5m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_170_stau_5m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_180_stau_5m_ctau_ecm_365": {'fraction': 1.0},

        # ###################################################
        # #             FCCee: 365 GeV - 10 m               #
        # ###################################################
        # 'FCCee_120_stau_10m_ctau_ecm_365': {'fraction': 1.0},
        # 'FCCee_130_stau_10m_ctau_ecm_365': {'fraction': 1.0},
        # 'FCCee_140_stau_10m_ctau_ecm_365': {'fraction': 1.0},
        # "FCCee_150_stau_10m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_160_stau_10m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_170_stau_10m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_180_stau_10m_ctau_ecm_365": {'fraction': 1.0},

        # ###################################################
        # #             FCCee: 365 GeV - 20 m               #
        # ###################################################
        # 'FCCee_120_stau_20m_ctau_ecm_365': {'fraction': 1.0},
        # 'FCCee_130_stau_20m_ctau_ecm_365': {'fraction': 1.0},
        # 'FCCee_140_stau_20m_ctau_ecm_365': {'fraction': 1.0},
        # "FCCee_150_stau_20m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_160_stau_20m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_170_stau_20m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_180_stau_20m_ctau_ecm_365": {'fraction': 1.0},

        # ###################################################
        # #             FCCee: 365 GeV - 50 m               #
        # ###################################################
        # 'FCCee_120_stau_50m_ctau_ecm_365': {'fraction': 1.0},
        # 'FCCee_130_stau_50m_ctau_ecm_365': {'fraction': 1.0},
        # 'FCCee_140_stau_50m_ctau_ecm_365': {'fraction': 1.0},
        # "FCCee_150_stau_50m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_160_stau_50m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_170_stau_50m_ctau_ecm_365": {'fraction': 1.0},
        # "FCCee_180_stau_50m_ctau_ecm_365": {'fraction': 1.0},

        # ###################################################
        # #                   BACKGROUND                    #
        # ###################################################
        # ###################################################
        # #          Background - WINTER 2023               #
        # ###################################################
        # 'p8_ee_WW_ecm365': {'fraction': 0.1,'chunks':100},
        # 'p8_ee_ZZ_ecm365': {'fraction': 1.0,'chunks':100},
        # 'wzp6_ee_nuenueH_Htautau_ecm365': {'fraction':0.1,'chunks':100},
        # 'wzp6_ee_bbH_Htautau_ecm365': {'fraction': 0.1,'chunks':100},
        # 'p8_ee_tt_ecm365': {'fraction': 1.0,'chunks':100},
        # 'wzp6_ee_tautau_ecm365': {'fraction': 1.0,'chunks':100},
        } 

prodTag = "FCCee/winter2023/IDEA/"
procDict = "FCCee_procDict_winter2023_IDEA.json"
# procDict = "FCCee_procDict_spring2021_IDEA.json"


# Add samples which are not part of the offical process
procDictAdd = {
    # ###################################################
    # #             FCCee: 365 GeV - 0.5 m                #
    # ###################################################
    'FCCee_120_stau_0.5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.36360000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_130_stau_0.5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 6.76073000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_140_stau_0.5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 5.16252000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_150_stau_0.5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 3.61405000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_160_stau_0.5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.17642000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_170_stau_0.5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 9.40993000e-03, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_180_stau_0.5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.77721000e-04, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # ###################################################
    # #             FCCee: 365 GeV - 1 m               #
    ###################################################
    'FCCee_120_stau_1m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.36360000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_130_stau_1m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 6.76073000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_140_stau_1m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 5.16252000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_150_stau_1m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 3.61405000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_160_stau_1m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.17642000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_170_stau_1m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 9.40993000e-03, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_180_stau_1m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.77721000e-04, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # ###################################################
    # #             FCCee: 365 GeV - 2 m               #
    ###################################################
    'FCCee_120_stau_2m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.36360000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_130_stau_2m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 6.76073000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_140_stau_2m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 5.16252000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_150_stau_2m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 3.61405000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_160_stau_2m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.17642000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_170_stau_2m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 9.40993000e-03, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_180_stau_2m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.77721000e-04, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # ###################################################
    # #             FCCee: 365 GeV - 5 m               #
    ###################################################
    'FCCee_120_stau_5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.36226000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_130_stau_5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 6.75979000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_140_stau_5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 5.16167000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_150_stau_5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 3.61349000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_160_stau_5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.17607000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_170_stau_5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 9.40847000e-03, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_180_stau_5m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.77581000e-04, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # ###################################################
    # #             FCCee: 365 GeV - 10 m              #
    ###################################################
    'FCCee_120_stau_10m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.36226000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_130_stau_10m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 6.75979000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_140_stau_10m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 5.16167000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_150_stau_10m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 3.61349000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_160_stau_10m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.17607000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_170_stau_10m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 9.40847000e-03, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_180_stau_10m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.77581000e-04, "kfactor": 1.0, "matchingEfficiency": 1.0},

    # ###################################################
    # #             FCCee: 365 GeV - 20 m              #
    ###################################################
    'FCCee_120_stau_20m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.36226000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_130_stau_20m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 6.75979000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_140_stau_20m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 5.16167000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_150_stau_20m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 3.61349000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_160_stau_20m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.17607000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_170_stau_20m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 9.40847000e-03, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_180_stau_20m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.77581000e-04, "kfactor": 1.0, "matchingEfficiency": 1.0},
    # ###################################################
    # #             FCCee: 365 GeV - 50 m              #
    ###################################################
    'FCCee_120_stau_50m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.36226000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_130_stau_50m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 6.75979000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_140_stau_50m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 5.16167000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_150_stau_50m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 3.61349000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_160_stau_50m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 2.17607000e-02, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_170_stau_50m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 9.40847000e-03, "kfactor": 1.0, "matchingEfficiency": 1.0},
    'FCCee_180_stau_50m_ctau_ecm_365': {"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 8.77581000e-04, "kfactor": 1.0, "matchingEfficiency": 1.0},
}

# intLumi = 1 #test and comparison
intLumi = 2.70e6 / 4  # 4 year for 1IP pb-1

doScale = True
# saveMetaData = True

# # Required for plots
# writeOutScales = True
# writeMetaDataToFile = True

# Number of threads to use
# nCPUS = 2

# Whether to produce ROOT TTrees, default is False
doTree = False

# Save cut yields and efficiencies in LaTeX table
saveTabular = True

# Save cut yields and efficiencies in JSON file
saveJSON = True

# Dictionary with the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {

    "selNone": "n_RecoTracks > -1",

    "semiLep_KV": (
        "n_RecoTracks > -1"
        " && ((n_RecoElectrons == 1 && n_RecoMuons == 0) || (n_RecoElectrons ==0 && n_RecoMuons == 1))"
        " && (Any(RecoElectrons_pt > 10) || Any(RecoMuons_pt > 10))"
        " && nKinkCandidates_passVeto > 0"
        " && Any(abs(KinkAngle) > 20)"
    ),

    "semiLep_DV": (
        "n_RecoTracks > -1"
        " && ((n_RecoElectrons == 1 && n_RecoMuons == 0) || (n_RecoElectrons == 0 && n_RecoMuons == 1))"
        " && (Any(RecoElectrons_pt > 10) || Any(RecoMuons_pt > 10))"
        " && nKinkCandidates_passVeto == 0"
        " && nDisplacedVertices_failInnerHitVeto > 0 && nDisplacedVertices_failInnerHitVeto < 3"
        " && Any(PV2V0Cos < 0.95)"
    ),

    "hadronic_KV": (
        " n_RecoTracks > -1"
        " && n_RecoElectrons == 0"
        " && n_RecoMuons == 0"
        " && nKinkCandidates_passVeto > 0"
        " && Any(abs(KinkAngle) > 20)"
    ),

    "hadronic_DV": (
        "n_RecoTracks > -1"
        " && n_RecoElectrons == 0"
        " && n_RecoMuons == 0"
        " && nKinkCandidates_passVeto == 0"
        " && nDisplacedVertices_failInnerHitVeto > 0 && nDisplacedVertices_failInnerHitVeto < 3"
        " && Any(PV2V0Cos < 0.95)"
    ),

    "escaping": (
        "n_RecoTracks > -1"
        " && nKinkCandidates_passVeto == 0"
        " && nDisplacedVertices_failInnerHitVeto == 0"
    ),

    "escaping_Staus": (
        "n_RecoTracks > -1"
        #" && n_RecoedPrimaryTracks < 3"
        " && nKinkCandidates_passVeto == 0"
        " && nDisplacedVertices_failInnerHitVeto == 0"
        " && Any(TOF_AcceptedTracks > 12500)"
        #" && Any(RecoedPrimaryTracks_pt > 50)"
    ),
}

cutLabels = {
    "selNone": "selNone",
    "semiLep_KV": "semiLep_KV",
    "semiLep_DV": "semiLep_DV",
    "hadronic_KV": "hadronic_KV",
    "hadronic_DV": "hadronic_DV",
    "escaping": "escaping",
    "escaping_Staus": "escaping_Staus",
}

histoList = {
    # Gen-level stau
    "n_GenStau":           {"name":"n_GenStau",          "title":"Number of gen staus",             "bin":5,   "xmin":-0.5,  "xmax":4.5},
    "GenStau_vx":          {"name":"GenStau_vx",         "title":"Stau vertex x",                   "bin":50,  "xmin":-10,   "xmax":10},
    "GenStau_vy":          {"name":"GenStau_vy",         "title":"Stau vertex y",                   "bin":50,  "xmin":-10,   "xmax":10},
    "GenStau_vz":          {"name":"GenStau_vz",         "title":"Stau vertex z",                   "bin":50,  "xmin":-50,   "xmax":50},
    "GenStau_Lxy":         {"name":"GenStau_Lxy",        "title":"Transverse decay length Lxy",     "bin":50,  "xmin":0,     "xmax":10},
    "GenStau_Lxyz":        {"name":"GenStau_Lxyz",       "title":"3D decay length Lxyz",            "bin":50,  "xmin":0,     "xmax":10},
    "GenStau_time":        {"name":"GenStau_time",       "title":"Stau time",            "bin":50,  "xmin":0,     "xmax":10},
    # "GenStau_observed_lifetime_xyz":   {"name":"GenStau_observed_lifetime_xyz",   "title":"Observed stau lifetime (xyz)",    "bin":50,  "xmin":0,     "xmax":100},
    # "n_StauDaughters":       {"name":"n_StauDaughters",        "title":"Number of Stau Daughters",        "bin":5,   "xmin":-0.5, "xmax":9.5},
    "GenGravitino_e":        {"name":"GenGravitino_e",        "title":"Gen Gravitino energy",            "bin":100,  "xmin":0,    "xmax":200},
    
    # Tau
    "GenTau_e":              {"name":"GenTau_e",              "title":"Gen Tau energy",                  "bin":100,  "xmin":0,    "xmax":200},
    "GenTau_px":             {"name":"GenTau_px",             "title":"Gen Tau px",                      "bin":100,  "xmin":-200, "xmax":200},
    "GenTau_py":             {"name":"GenTau_py",             "title":"Gen Tau py",                      "bin":100,  "xmin":-200, "xmax":200},
    "GenTau_pz":             {"name":"GenTau_pz",             "title":"Gen Tau pz",                      "bin":100,  "xmin":-500, "xmax":500},
    "GenTau_pt":             {"name":"GenTau_pt",             "title":"Gen Tau pt",                      "bin":100,  "xmin":0,    "xmax":200},
    "GenTau_eta":            {"name":"GenTau_eta",            "title":"Gen Tau eta",                     "bin":100,  "xmin":-5,   "xmax":5},
    "GenTau_phi":            {"name":"GenTau_phi",            "title":"Gen Tau phi",                     "bin":100,  "xmin":-3.2, "xmax":3.2},
    "GenTau_theta":          {"name":"GenTau_theta",          "title":"Gen Tau theta",                   "bin":100,  "xmin":0,    "xmax":3.2},
    "GenTau_vx":             {"name":"GenTau_vx",             "title":"Gen Tau vx",                      "bin":100,  "xmin":-10,  "xmax":10},
    "GenTau_vy":             {"name":"GenTau_vy",             "title":"Gen Tau vy",                      "bin":100,  "xmin":-10,  "xmax":10},
    "GenTau_vz":             {"name":"GenTau_vz",             "title":"Gen Tau vz",                      "bin":100,  "xmin":-50,  "xmax":50},
    "GenTau_cTau":           {"name":"GenTau_cTau",           "title":"cTau",                    "bin":150,   "xmin":0,    "xmax":4},
    "decayLengthTau":        {"name": "decayLengthTau",    "title":"Gen Tau decay length",           "bin":50,   "xmin":0,    "xmax":50},
    "GenStau_theta":          {"name":"GenStau_theta",          "title":"Gen Stau theta",                   "bin":100,  "xmin":0,    "xmax":3.2},
    
    # Final-state muons
    "n_FSGenMuon":       {"name":"n_FSGenMuon",     "title":"Number of FS muons", "bin":11,   "xmin":-0.5,  "xmax":10.5},
    "FSGenMuon_e":      {"name":"FSGenMuon_e",      "title":"FS muon energy",     "bin":50, "xmin":0, "xmax":200},
    "FSGenMuon_px":     {"name":"FSGenMuon_px",     "title":"FS muon px",         "bin":50, "xmin":-100, "xmax":100},
    "FSGenMuon_py":     {"name":"FSGenMuon_py",     "title":"FS muon py",         "bin":50, "xmin":-100, "xmax":100},
    "FSGenMuon_pz":     {"name":"FSGenMuon_pz",     "title":"FS muon pz",         "bin":50, "xmin":-200, "xmax":200},
    "FSGenMuon_pt":     {"name":"FSGenMuon_pt",     "title":"FS muon pt",         "bin":50, "xmin":0, "xmax":100},
    "FSGenMuon_eta":    {"name":"FSGenMuon_eta",    "title":"FS muon eta",        "bin":50, "xmin":-5, "xmax":5},
    "FSGenMuon_phi":    {"name":"FSGenMuon_phi",    "title":"FS muon phi",        "bin":64, "xmin":-3.2, "xmax":3.2},
    "FSGenMuon_vx":{"name":"FSGenMuon_vx","title":"FS muon vertex x","bin":50,"xmin":-10,"xmax":10},
    "FSGenMuon_vy":{"name":"FSGenMuon_vy","title":"FS muon vertex y","bin":50,"xmin":-10,"xmax":10},
    "FSGenMuon_vz":{"name":"FSGenMuon_vz","title":"FS muon vertex z","bin":50,"xmin":-50,"xmax":50},
    "FSGenMuon_charge": {"name":"FSGenMuon_charge", "title":"FS muon charge", "bin":3, "xmin":-1.5, "xmax":1.5},

    # Final-state electrons
    "n_FSGenElectron": {"name":"n_FSGenElectron","title":"Number of FS electrons","bin":11,"xmin":-0.5,"xmax":10.5},
    "FSGenElectron_e":    {"name":"FSGenElectron_e",    "title":"FS electron energy", "bin":50, "xmin":0, "xmax":200},
    "FSGenElectron_px":   {"name":"FSGenElectron_px",   "title":"FS electron px",     "bin":50, "xmin":-100, "xmax":100},
    "FSGenElectron_py":   {"name":"FSGenElectron_py",   "title":"FS electron py",     "bin":50, "xmin":-100, "xmax":100},
    "FSGenElectron_pz":   {"name":"FSGenElectron_pz",   "title":"FS electron pz",     "bin":50, "xmin":-200, "xmax":200},
    "FSGenElectron_pt":   {"name":"FSGenElectron_pt",   "title":"FS electron pt",     "bin":50, "xmin":0, "xmax":100},
    "FSGenElectron_eta":  {"name":"FSGenElectron_eta",  "title":"FS electron eta",    "bin":50, "xmin":-5, "xmax":5},
    "FSGenElectron_phi":  {"name":"FSGenElectron_phi",  "title":"FS electron phi",    "bin":64, "xmin":-3.2, "xmax":3.2},
    "FSGenElectron_vx": {"name":"FSGenElectron_vx","title":"FS electron vertex x","bin":50,"xmin":-10,"xmax":10},
    "FSGenElectron_vy": {"name":"FSGenElectron_vy","title":"FS electron vertex y","bin":50,"xmin":-10,"xmax":10},
    "FSGenElectron_vz": {"name":"FSGenElectron_vz","title":"FS electron vertex z","bin":50,"xmin":-50,"xmax":50},
    "FSGenElectron_charge": {"name":"FSGenElectron_charge", "title":"FS electron charge", "bin":3, "xmin":-1.5, "xmax":1.5},

    # Final-state neutrinos
    "n_FSGenNeutrino": {"name":"n_FSGenNeutrino","title":"Number of FS neutrinos","bin":11,"xmin":-0.5,"xmax":10.5},
    "FSGenNeutrino_e":    {"name":"FSGenNeutrino_e",    "title":"FS neutrino energy", "bin":160, "xmin":0, "xmax":160},
    "FSGenNeutrino_px":     {"name":"FSGenNeutrino_px",   "title":"FS neutrino px",     "bin":50, "xmin":-100, "xmax":100},
    "FSGenNeutrino_py":     {"name":"FSGenNeutrino_py",   "title":"FS neutrino py",     "bin":50, "xmin":-100, "xmax":100},
    "FSGenNeutrino_pz":     {"name":"FSGenNeutrino_pz",   "title":"FS neutrino pz",     "bin":50, "xmin":-200, "xmax":200},
    "FSGenNeutrino_pt":     {"name":"FSGenNeutrino_pt",   "title":"FS neutrino pt",    "bin":50, "xmin":0, "xmax":100},
    "FSGenNeutrino_eta":    {"name":"FSGenNeutrino_eta",  "title":"FS neutrino eta",    "bin":50, "xmin":-5, "xmax":5},
    "FSGenNeutrino_phi":    {"name":"FSGenNeutrino_phi",  "title":"FS neutrino phi",    "bin":64, "xmin":-3.2, "xmax":3.2},

    # Reco Jets
    "n_RecoJets":     {"name":"n_RecoJets","title":"Number of reconstructed jets","bin":10,"xmin":-0.5,"xmax":9.5},
    "RecoJet_e":      {"name":"RecoJet_e",      "title":"Jet energy", "bin":50,"xmin":0,"xmax":200},
    "RecoJet_px":     {"name":"RecoJet_px",     "title":"Jet px",     "bin":50,"xmin":-100,"xmax":100},
    "RecoJet_py":     {"name":"RecoJet_py",     "title":"Jet py",     "bin":50,"xmin":-100,"xmax":100},
    "RecoJet_pz":     {"name":"RecoJet_pz",     "title":"Jet pz",     "bin":50,"xmin":-200,"xmax":200},
    "RecoJet_pt":     {"name":"RecoJet_pt",     "title":"Jet pt",     "bin":50,"xmin":0,"xmax":100},
    "RecoJet_eta":    {"name":"RecoJet_eta",    "title":"Jet eta",    "bin":50,"xmin":-5,"xmax":5},
    "RecoJet_phi":    {"name":"RecoJet_phi",    "title":"Jet phi",    "bin":64,"xmin":-3.2,"xmax":3.2},
    "RecoJet_charge": {"name":"RecoJet_charge", "title":"Jet charge", "bin":3,"xmin":-1.5,"xmax":1.5},
    "RecoJet_mvis": {"name":"RecoJet_mvis", "title":"Jet mvis", "bin":50,"xmin":-100,"xmax":100},
    "RecoJetTrack_absD0": {"name":"RecoJetTrack_absD0", "title":"Jet abs D0", "bin":50,"xmin":-100,"xmax":100},
    "RecoJetTrack_Z0cov": {"name":"RecoJetTrack_Z0cov", "title":"Jet Z0 cov", "bin":50,"xmin":-100,"xmax":100},

    # Reco Electrons
    "n_RecoElectrons":     {"name":"n_RecoElectrons",   "title":"Number of reconstructed electrons","bin":5,"xmin":-0.5,"xmax":4.5},
    "RecoElectrons_e":      {"name":"RecoElectrons_e",      "title":"Reco electron energy", "bin":50,"xmin":0,"xmax":200},
    "RecoElectrons_px":     {"name":"RecoElectrons_px",     "title":"Reco electron px",     "bin":50,"xmin":-100,"xmax":100},
    "RecoElectrons_py":     {"name":"RecoElectrons_py",     "title":"Reco electron py",     "bin":50,"xmin":-100,"xmax":100},
    "RecoElectrons_pz":     {"name":"RecoElectrons_pz",     "title":"Reco electron pz",     "bin":50,"xmin":-200,"xmax":200},
    "RecoElectrons_pt":     {"name":"RecoElectrons_pt",     "title":"Reco electron pt",     "bin":50,"xmin":0,"xmax":100},
    "RecoElectrons_eta":    {"name":"RecoElectrons_eta",    "title":"Reco electron eta",    "bin":50,"xmin":-5,"xmax":5},
    "RecoElectrons_phi":    {"name":"RecoElectrons_phi",    "title":"Reco electron phi",    "bin":64,"xmin":-3.2,"xmax":3.2},
    "RecoElectrons_charge": {"name":"RecoElectrons_charge", "title":"Reco electron charge","bin":3,"xmin":-1.5,"xmax":1.5},

    # # Reco Muons
    "n_RecoMuons":      {"name":"n_RecoMuons","title":"Number of reconstructed muons","bin":5,"xmin":-0.5,"xmax":4.5},
    "RecoMuons_e":      {"name":"RecoMuons_e",      "title":"Reco muon energy", "bin":50,"xmin":0,"xmax":200},
    "RecoMuons_px":     {"name":"RecoMuons_px",     "title":"Reco muon px",     "bin":50,"xmin":-100,"xmax":100},
    "RecoMuons_py":     {"name":"RecoMuons_py",     "title":"Reco muon py",     "bin":50,"xmin":-100,"xmax":100},
    "RecoMuons_pz":     {"name":"RecoMuons_pz",     "title":"Reco muon pz",     "bin":50,"xmin":-200,"xmax":200},
    "RecoMuons_pt":     {"name":"RecoMuons_pt",     "title":"Reco muon pt",     "bin":50,"xmin":0,"xmax":100},
    "RecoMuons_eta":    {"name":"RecoMuons_eta",    "title":"Reco muon eta",    "bin":50,"xmin":-5,"xmax":5},
    "RecoMuons_phi":    {"name":"RecoMuons_phi",    "title":"Reco muon phi",    "bin":64,"xmin":-3.2,"xmax":3.2},
    "RecoMuons_charge": {"name":"RecoMuons_charge", "title":"Reco muon charge", "bin":3,"xmin":-1.5,"xmax":1.5},

    # MET
    "RecoMissingEnergy_e":   {"name":"RecoMissingEnergy_e",   "title":"Missing ET energy", "bin":50,"xmin":0,"xmax":200},
    "RecoMissingEnergy_pt":  {"name":"RecoMissingEnergy_pt",  "title":"Missing ET pt",     "bin":50,"xmin":0,"xmax":200},
    "RecoMissingEnergy_eta": {"name":"RecoMissingEnergy_eta", "title":"Missing ET eta",    "bin":50,"xmin":-5,"xmax":5},
    "RecoMissingEnergy_phi": {"name":"RecoMissingEnergy_phi", "title":"Missing ET phi",    "bin":64,"xmin":-3.2,"xmax":3.2},

    # Track
    "TOF_AcceptedTracks": {"name":"TOF_AcceptedTracks", "title":"Time of flight [ps]", "bin":5000,"xmin":0,"xmax":50000},

    # Reco DVs from selected tracks
    "nDisplaced_Vertices": {"name":"nDisplaced_Vertices",   "title":"Number of reconstructed DVs",  "bin":11 , "xmin":-0.5, "xmax":10.5},
    "n_nonprimary_tracks": {"name":"n_nonprimary_tracks",   "title":"Number of non-primary tracks DVs",  "bin":20, "xmin":-0.5, "xmax":19.5},
    "n_RecoedPrimaryTracks": {"name":"n_RecoedPrimaryTracks",   "title":"Number of primary tracks DVs",  "bin":25, "xmin":-0.5, "xmax":50.5},
    "RecoParticles_firstHitLoc": {"name":"RecoParticles_firstHitLoc", "title":"First hit location", "bin":100, "xmin":0, "xmax":2000},
    "RecoParticles_lastHitLoc": {"name":"RecoParticles_lastHitLoc", "title":"Last hit location", "bin":100, "xmin":0, "xmax":2000},
    "RecoParticles_nHits": {"name":"RecoParticles_nHits", "title":"Number of hits on track", "bin":100, "xmin":0, "xmax":100},
    "RecoParticles_nDriftChamberHits": {"name":"RecoParticles_nDriftChamberHits", "title":"Number of drift chamber hits", "bin":100, "xmin":0, "xmax":100},
    "RecoedPrimaryTracks_firstHitLoc": {"name":"RecoedPrimaryTracks_firstHitLoc", "title":"First hit location of primary tracks", "bin":100, "xmin":0, "xmax":2000},
    "RecoedPrimaryTracks_lastHitLoc": {"name":"RecoedPrimaryTracks_lastHitLoc", "title":"Last hit location of primary tracks", "bin":100, "xmin":0, "xmax":2000},
    
    # Reco Primary Tracks momentums
    "RecoedPrimaryTracks_p": {"name": "RecoedPrimaryTracks_p", "title": "Reconstructed primary tracks: p [GeV/c]", "bin": 100, "xmin": 0, "xmax": 365},
    "RecoedPrimaryTracks_pt": {"name": "RecoedPrimaryTracks_pt", "title": "Reconstructed primary tracks: p_{T} [GeV/c]", "bin": 100, "xmin": 0, "xmax": 365},
    
    "nDisplacedVertices_failInnerHitVeto" :  {"name":"nDisplacedVertices_failInnerHitVeto",  "title":"#DV failing the hit veto",   "bin":10, "xmin":-0.5, "xmax":9.5},
    "nTracks_DV_failInnerHitVeto": {"name":"nTracks_DV_failInnerHitVeto",  "title":"Number of tracks per DV (fail hit veto)",   "bin":10, "xmin":-0.5, "xmax":9.5},
    "invMass_seltracks_DVs": {"name":"invMass_seltracks_DVs",  "title":"DV invariant mass [GeV]",    "bin":100, "xmin":0,    "xmax":10},
    "DV_evt_seltracks_chi2": {"name":"DV_evt_seltracks_chi2",    "title":"DV fit chi2",    "bin":10, "xmin":0, "xmax":10},
    "DV_evt_seltracks_normchi2": {"name":"DV_evt_seltracks_normchi2",    "title":"DV fit normalized chi2",    "bin":50, "xmin":0, "xmax":10},
    "Reco_seltracks_DVs_Lxy": {"name":"Reco_seltracks_DVs_Lxy","title":"DV L_{xy} [mm]","bin":100,"xmin":0,"xmax":250},
    "Reco_seltracks_DVs_Lxyz": {"name":"Reco_seltracks_DVs_Lxyz","title":"DV L_{xyz} [mm]","bin":100,"xmin":0,"xmax":250},

    "KinkCandidates_passInnerHitVeto": {"name":"KinkCandidates_passInnerHitVeto", "title":"Number of kink vertices", "bin":5, "xmin":-0.5, "xmax":4.5},
    "nKinkCandidates_passVeto" : {"name":"nKinkCandidates_passVeto", "title":"Number of kink vertices passing the hit veto", "bin":5, "xmin":-0.5, "xmax":4.5},
    "KinkVertex_invMass": {"name":"KinkVertex_invMass", "title":"Invariant mass of kink vertex", "bin":150, "xmin":0, "xmax":150},
    "KinkVertex_dxy": {"name":"KinkVertex_dxy", "title":"dxy of kink vertex", "bin":100, "xmin":0, "xmax":2000},
    "KinkVertex_d3d": {"name":"KinkVertex_d3d", "title":"d3d of kink vertex", "bin":100, "xmin":0, "xmax":2000},
    "KinkVertex_ntracks": {"name":"KinkVertex_ntracks", "title":"Number of tracks in kink vertex", "bin":10, "xmin":-0.5, "xmax":9.5},
    "nKinkVertices": {"name":"nKinkVertices", "title":"Number of kink vertices before hit veto", "bin":5, "xmin":-0.5, "xmax":4.5},
    "KinkAngle": {"name": "KinkAngle", "title": "angle between the r_pvkv and P_kv", "bin":180, "xmin":0, "xmax":180},
    "PV2V0Cos": {"name":"PV2V0Cos", "title":"Cos between displaced verticies and primary vertex", "bin":100, "xmin":-1, "xmax":1},

    "RecoedPrimaryTrack_mass": {"name": "RecoedPrimaryTrack_mass", "title": "Mass of escaping tracks [GeV]", "bin":50, "xmin":100, "xmax":200},
    "TOF_RecoedPrimaryTracks": {"name": "TOF_RecoedPrimaryTracks", "title": "Time of flight of recoed primary tracks [ps]", "bin":200, "xmin":0, "xmax":50000},
    "TOF_sel_tracks": {"name": "TOF_sel_tracks", "title": "Time of flight of sel tracks [ps]", "bin":200, "xmin":0, "xmax":50000},
}




oldhistoList = {
    # Gen-level stau
    # "n_GenStau":           {"name":"n_GenStau",          "title":"Number of gen staus",             "bin":5,   "xmin":-0.5,  "xmax":4.5},
    # "GenStau_vx":          {"name":"GenStau_vx",         "title":"Stau vertex x",                   "bin":50,  "xmin":-10,   "xmax":10},
    # "GenStau_vy":          {"name":"GenStau_vy",         "title":"Stau vertex y",                   "bin":50,  "xmin":-10,   "xmax":10},
    # "GenStau_vz":          {"name":"GenStau_vz",         "title":"Stau vertex z",                   "bin":50,  "xmin":-50,   "xmax":50},
    # "GenStau_Lxy":         {"name":"GenStau_Lxy",        "title":"Transverse decay length Lxy",     "bin":50,  "xmin":0,     "xmax":10},
    # "GenStau_Lxyz":        {"name":"GenStau_Lxyz",       "title":"3D decay length Lxyz",            "bin":50,  "xmin":0,     "xmax":10},
    # "GenStau_time":        {"name":"GenStau_time",       "title":"Stau time",            "bin":50,  "xmin":0,     "xmax":10},
    # # "GenStau_observed_lifetime_xyz":   {"name":"GenStau_observed_lifetime_xyz",   "title":"Observed stau lifetime (xyz)",    "bin":50,  "xmin":0,     "xmax":100},
    # # "n_StauDaughters":       {"name":"n_StauDaughters",        "title":"Number of Stau Daughters",        "bin":5,   "xmin":-0.5, "xmax":9.5},
    # "GenGravitino_e":        {"name":"GenGravitino_e",        "title":"Gen Gravitino energy",            "bin":100,  "xmin":0,    "xmax":200},
    
    # # Tau
    # "GenTau_e":              {"name":"GenTau_e",              "title":"Gen Tau energy",                  "bin":100,  "xmin":0,    "xmax":200},
    # "GenTau_px":             {"name":"GenTau_px",             "title":"Gen Tau px",                      "bin":100,  "xmin":-200, "xmax":200},
    # "GenTau_py":             {"name":"GenTau_py",             "title":"Gen Tau py",                      "bin":100,  "xmin":-200, "xmax":200},
    # "GenTau_pz":             {"name":"GenTau_pz",             "title":"Gen Tau pz",                      "bin":100,  "xmin":-500, "xmax":500},
    # "GenTau_pt":             {"name":"GenTau_pt",             "title":"Gen Tau pt",                      "bin":100,  "xmin":0,    "xmax":200},
    # "GenTau_eta":            {"name":"GenTau_eta",            "title":"Gen Tau eta",                     "bin":100,  "xmin":-5,   "xmax":5},
    # "GenTau_phi":            {"name":"GenTau_phi",            "title":"Gen Tau phi",                     "bin":100,  "xmin":-3.2, "xmax":3.2},
    # # "GenTau_theta":          {"name":"GenTau_theta",          "title":"Gen Tau theta",                   "bin":100,  "xmin":0,    "xmax":3.2},
    # "GenTau_vx":             {"name":"GenTau_vx",             "title":"Gen Tau vx",                      "bin":100,  "xmin":-10,  "xmax":10},
    # "GenTau_vy":             {"name":"GenTau_vy",             "title":"Gen Tau vy",                      "bin":100,  "xmin":-10,  "xmax":10},
    # "GenTau_vz":             {"name":"GenTau_vz",             "title":"Gen Tau vz",                      "bin":100,  "xmin":-50,  "xmax":50},
    # "GenTau_cTau":           {"name":"GenTau_cTau",           "title":"cTau",                    "bin":150,   "xmin":0,    "xmax":4},
    # "decayLengthTau":        {"name": "decayLengthTau",    "title":"Gen Tau decay length",           "bin":50,   "xmin":0,    "xmax":50},
    # # "GenStau_theta":          {"name":"GenStau_theta",          "title":"Gen Stau theta",                   "bin":100,  "xmin":0,    "xmax":3.2},
    
    # Final-state muons
    # "n_FSGenMuon":       {"name":"n_FSGenMuon",     "title":"Number of FS muons", "bin":11,   "xmin":-0.5,  "xmax":10.5},
    # "FSGenMuon_e":      {"name":"FSGenMuon_e",      "title":"FS muon energy",     "bin":50, "xmin":0, "xmax":200},
    # "FSGenMuon_px":     {"name":"FSGenMuon_px",     "title":"FS muon px",         "bin":50, "xmin":-100, "xmax":100},
    # "FSGenMuon_py":     {"name":"FSGenMuon_py",     "title":"FS muon py",         "bin":50, "xmin":-100, "xmax":100},
    # "FSGenMuon_pz":     {"name":"FSGenMuon_pz",     "title":"FS muon pz",         "bin":50, "xmin":-200, "xmax":200},
    # "FSGenMuon_pt":     {"name":"FSGenMuon_pt",     "title":"FS muon pt",         "bin":50, "xmin":0, "xmax":100},
    # "FSGenMuon_eta":    {"name":"FSGenMuon_eta",    "title":"FS muon eta",        "bin":50, "xmin":-5, "xmax":5},
    # "FSGenMuon_phi":    {"name":"FSGenMuon_phi",    "title":"FS muon phi",        "bin":64, "xmin":-3.2, "xmax":3.2},
    # "FSGenMuon_vx":{"name":"FSGenMuon_vx","title":"FS muon vertex x","bin":50,"xmin":-10,"xmax":10},
    # "FSGenMuon_vy":{"name":"FSGenMuon_vy","title":"FS muon vertex y","bin":50,"xmin":-10,"xmax":10},
    # "FSGenMuon_vz":{"name":"FSGenMuon_vz","title":"FS muon vertex z","bin":50,"xmin":-50,"xmax":50},
    # "FSGenMuon_charge": {"name":"FSGenMuon_charge", "title":"FS muon charge", "bin":3, "xmin":-1.5, "xmax":1.5},

    # Final-state electrons
    # "n_FSGenElectron": {"name":"n_FSGenElectron","title":"Number of FS electrons","bin":11,"xmin":-0.5,"xmax":10.5},
    # "FSGenElectron_e":    {"name":"FSGenElectron_e",    "title":"FS electron energy", "bin":50, "xmin":0, "xmax":200},
    # "FSGenElectron_px":   {"name":"FSGenElectron_px",   "title":"FS electron px",     "bin":50, "xmin":-100, "xmax":100},
    # "FSGenElectron_py":   {"name":"FSGenElectron_py",   "title":"FS electron py",     "bin":50, "xmin":-100, "xmax":100},
    # "FSGenElectron_pz":   {"name":"FSGenElectron_pz",   "title":"FS electron pz",     "bin":50, "xmin":-200, "xmax":200},
    # "FSGenElectron_pt":   {"name":"FSGenElectron_pt",   "title":"FS electron pt",     "bin":50, "xmin":0, "xmax":100},
    # "FSGenElectron_eta":  {"name":"FSGenElectron_eta",  "title":"FS electron eta",    "bin":50, "xmin":-5, "xmax":5},
    # "FSGenElectron_phi":  {"name":"FSGenElectron_phi",  "title":"FS electron phi",    "bin":64, "xmin":-3.2, "xmax":3.2},
    # "FSGenElectron_vx": {"name":"FSGenElectron_vx","title":"FS electron vertex x","bin":50,"xmin":-10,"xmax":10},
    # "FSGenElectron_vy": {"name":"FSGenElectron_vy","title":"FS electron vertex y","bin":50,"xmin":-10,"xmax":10},
    # "FSGenElectron_vz": {"name":"FSGenElectron_vz","title":"FS electron vertex z","bin":50,"xmin":-50,"xmax":50},
    # "FSGenElectron_charge": {"name":"FSGenElectron_charge", "title":"FS electron charge", "bin":3, "xmin":-1.5, "xmax":1.5},

    # # Final-state neutrinos
    # "n_FSGenNeutrino": {"name":"n_FSGenNeutrino","title":"Number of FS neutrinos","bin":11,"xmin":-0.5,"xmax":10.5},
    # "FSGenNeutrino_e":    {"name":"FSGenNeutrino_e",    "title":"FS neutrino energy", "bin":160, "xmin":0, "xmax":160},
    # "FSGenNeutrino_px":     {"name":"FSGenNeutrino_px",   "title":"FS neutrino px",     "bin":50, "xmin":-100, "xmax":100},
    # "FSGenNeutrino_py":     {"name":"FSGenNeutrino_py",   "title":"FS neutrino py",     "bin":50, "xmin":-100, "xmax":100},
    # "FSGenNeutrino_pz":     {"name":"FSGenNeutrino_pz",   "title":"FS neutrino pz",     "bin":50, "xmin":-200, "xmax":200},
    # "FSGenNeutrino_pt":     {"name":"FSGenNeutrino_pt",   "title":"FS neutrino pt",    "bin":50, "xmin":0, "xmax":100},
    # "FSGenNeutrino_eta":    {"name":"FSGenNeutrino_eta",  "title":"FS neutrino eta",    "bin":50, "xmin":-5, "xmax":5},
    # "FSGenNeutrino_phi":    {"name":"FSGenNeutrino_phi",  "title":"FS neutrino phi",    "bin":64, "xmin":-3.2, "xmax":3.2},

    # # Reco Jets
    # "n_RecoJets":     {"name":"n_RecoJets","title":"Number of reconstructed jets","bin":10,"xmin":-0.5,"xmax":9.5},
    # "RecoJet_e":      {"name":"RecoJet_e",      "title":"Jet energy", "bin":50,"xmin":0,"xmax":200},
    # "RecoJet_px":     {"name":"RecoJet_px",     "title":"Jet px",     "bin":50,"xmin":-100,"xmax":100},
    # "RecoJet_py":     {"name":"RecoJet_py",     "title":"Jet py",     "bin":50,"xmin":-100,"xmax":100},
    # "RecoJet_pz":     {"name":"RecoJet_pz",     "title":"Jet pz",     "bin":50,"xmin":-200,"xmax":200},
    # "RecoJet_pt":     {"name":"RecoJet_pt",     "title":"Jet pt",     "bin":50,"xmin":0,"xmax":100},
    # "RecoJet_eta":    {"name":"RecoJet_eta",    "title":"Jet eta",    "bin":50,"xmin":-5,"xmax":5},
    # "RecoJet_phi":    {"name":"RecoJet_phi",    "title":"Jet phi",    "bin":64,"xmin":-3.2,"xmax":3.2},
    # "RecoJet_charge": {"name":"RecoJet_charge", "title":"Jet charge", "bin":3,"xmin":-1.5,"xmax":1.5},
    # "RecoJet_mvis": {"name":"RecoJet_mvis", "title":"Jet mvis", "bin":50,"xmin":-100,"xmax":100},
    # "RecoJetTrack_absD0": {"name":"RecoJetTrack_absD0", "title":"Jet abs D0", "bin":50,"xmin":-100,"xmax":100},
    # "RecoJetTrack_Z0cov": {"name":"RecoJetTrack_Z0cov", "title":"Jet Z0 cov", "bin":50,"xmin":-100,"xmax":100},

    # # Reco Electrons
    # "n_RecoElectrons":     {"name":"n_RecoElectrons",   "title":"Number of reconstructed electrons","bin":5,"xmin":-0.5,"xmax":4.5},
    # "RecoElectrons_e":      {"name":"RecoElectrons_e",      "title":"Reco electron energy", "bin":50,"xmin":0,"xmax":200},
    # "RecoElectrons_px":     {"name":"RecoElectrons_px",     "title":"Reco electron px",     "bin":50,"xmin":-100,"xmax":100},
    # "RecoElectrons_py":     {"name":"RecoElectrons_py",     "title":"Reco electron py",     "bin":50,"xmin":-100,"xmax":100},
    # "RecoElectrons_pz":     {"name":"RecoElectrons_pz",     "title":"Reco electron pz",     "bin":50,"xmin":-200,"xmax":200},
    # "RecoElectrons_pt":     {"name":"RecoElectrons_pt",     "title":"Reco electron pt",     "bin":50,"xmin":0,"xmax":100},
    # "RecoElectrons_eta":    {"name":"RecoElectrons_eta",    "title":"Reco electron eta",    "bin":50,"xmin":-5,"xmax":5},
    # "RecoElectrons_phi":    {"name":"RecoElectrons_phi",    "title":"Reco electron phi",    "bin":64,"xmin":-3.2,"xmax":3.2},
    # "RecoElectrons_charge": {"name":"RecoElectrons_charge", "title":"Reco electron charge","bin":3,"xmin":-1.5,"xmax":1.5},

    # # # Reco Muons
    # "n_RecoMuons":      {"name":"n_RecoMuons","title":"Number of reconstructed muons","bin":5,"xmin":-0.5,"xmax":4.5},
    # "RecoMuons_e":      {"name":"RecoMuons_e",      "title":"Reco muon energy", "bin":50,"xmin":0,"xmax":200},
    # "RecoMuons_px":     {"name":"RecoMuons_px",     "title":"Reco muon px",     "bin":50,"xmin":-100,"xmax":100},
    # "RecoMuons_py":     {"name":"RecoMuons_py",     "title":"Reco muon py",     "bin":50,"xmin":-100,"xmax":100},
    # "RecoMuons_pz":     {"name":"RecoMuons_pz",     "title":"Reco muon pz",     "bin":50,"xmin":-200,"xmax":200},
    # "RecoMuons_pt":     {"name":"RecoMuons_pt",     "title":"Reco muon pt",     "bin":50,"xmin":0,"xmax":100},
    # "RecoMuons_eta":    {"name":"RecoMuons_eta",    "title":"Reco muon eta",    "bin":50,"xmin":-5,"xmax":5},
    # "RecoMuons_phi":    {"name":"RecoMuons_phi",    "title":"Reco muon phi",    "bin":64,"xmin":-3.2,"xmax":3.2},
    # "RecoMuons_charge": {"name":"RecoMuons_charge", "title":"Reco muon charge", "bin":3,"xmin":-1.5,"xmax":1.5},

    # # MET
    # "RecoMissingEnergy_e":   {"name":"RecoMissingEnergy_e",   "title":"Missing ET energy", "bin":50,"xmin":0,"xmax":200},
    # "RecoMissingEnergy_pt":  {"name":"RecoMissingEnergy_pt",  "title":"Missing ET pt",     "bin":50,"xmin":0,"xmax":200},
    # "RecoMissingEnergy_eta": {"name":"RecoMissingEnergy_eta", "title":"Missing ET eta",    "bin":50,"xmin":-5,"xmax":5},
    # "RecoMissingEnergy_phi": {"name":"RecoMissingEnergy_phi", "title":"Missing ET phi",    "bin":64,"xmin":-3.2,"xmax":3.2},

    # Track
    "TOF_AcceptedTracks": {"name":"TOF_AcceptedTracks", "title":"Time of flight", "bin":200,"xmin":0,"xmax":50000},

    # Reco DVs from selected tracks
    "nDisplaced_Vertices": {"name":"nDisplaced_Vertices",   "title":"Number of reconstructed DVs",  "bin":11 , "xmin":-0.5, "xmax":10.5},
    "n_nonprimary_tracks": {"name":"n_nonprimary_tracks",   "title":"Number of non-primary tracks DVs",  "bin":20, "xmin":-0.5, "xmax":19.5},
    "n_RecoedPrimaryTracks": {"name":"n_RecoedPrimaryTracks",   "title":"Number of primary tracks DVs",  "bin":25, "xmin":-0.5, "xmax":50.5},
    
    # Reco Primary Tracks momentums
    # "RecoedPrimaryTracks_firstHitLocation": {"name": "RecoedPrimaryTracks_firstHitLocation", "title": "Reconstructed primary tracks: first hit location [mm]", "bin": 100, "xmin": 0, "xmax": 365},
    # "RecoedPrimaryTracks_lastHitLocation": {"name": "RecoedPrimaryTracks_lastHitLocation", "title": "Reconstructed primary tracks: last hit location [mm]", "bin": 100, "xmin": 0, "xmax": 365},
    "RecoedPrimaryTracks_p": {"name": "RecoedPrimaryTracks_p", "title": "Reconstructed primary tracks: p [GeV/c]", "bin": 100, "xmin": 0, "xmax": 365},
    "RecoedPrimaryTracks_pt": {"name": "RecoedPrimaryTracks_pt", "title": "Reconstructed primary tracks: p_{T} [GeV/c]", "bin": 100, "xmin": 0, "xmax": 365},
    
    # "sel_tracks_pt_DV": {"name": "sel_tracks_pt_DV", "title": "pt of non-primary tracks", "bin":40, "xmin":0.0, "xmax": 80},
    # "sel_tracks_D0_DV": {"name": "sel_tracks_D0_DV", "title": "D0 of non-primary tracks", "bin":200, "xmin":0.0, "xmax": 200.0},
    # "sel_tracks_Z0_DV": {"name": "sel_tracks_Z0_DV", "title": "Z0 of non-primary tracks", "bin":200, "xmin":0.0, "xmax": 200.0},

    # "nDisplacedVertices_failInnerHitVeto" :  {"name":"nDisplacedVertices_failInnerHitVeto",  "title":"#DV failing the hit veto",   "bin":10, "xmin":-0.5, "xmax":9.5},
    # "nTracks_DV_failInnerHitVeto": {"name":"nTracks_DV_failInnerHitVeto",  "title":"Number of tracks per DV (fail hit veto)",   "bin":10, "xmin":-0.5, "xmax":9.5},
    # "invMass_seltracks_DVs": {"name":"invMass_seltracks_DVs",  "title":"DV invariant mass [GeV]",    "bin":100, "xmin":0,    "xmax":10},
    # "invMass_seltracks_DVs_zoom": {"name":"invMass_seltracks_DVs",  "title":"DV invariant mass [GeV]",    "bin":10, "xmin":0,    "xmax":2},
    # "DV_evt_seltracks_chi2": {"name":"DV_evt_seltracks_chi2",    "title":"DV fit chi2",    "bin":10, "xmin":0, "xmax":10},
    # "DV_evt_seltracks_normchi2": {"name":"DV_evt_seltracks_normchi2",    "title":"DV fit normalized chi2",    "bin":50, "xmin":0, "xmax":10},
    # "Reco_seltracks_DVs_Lxy": {"name":"Reco_seltracks_DVs_Lxy","title":"DV L_{xy} [mm]","bin":100,"xmin":0,"xmax":250},
    # "Reco_seltracks_DVs_Lxyz": {"name":"Reco_seltracks_DVs_Lxyz","title":"DV L_{xyz} [mm]","bin":100,"xmin":0,"xmax":250},

    # "RecoVisibleEnergy": {"name":"RecoVisibleEnergy", "title":"Visible energy", "bin":120,"xmin":0,"xmax":365},
    # "RecoMissingEnergy3D": {"name":"RecoMissingEnergy3D", "title":"Calculated Missing energy", "bin":120,"xmin":0,"xmax":365},
    
    "KinkCandidates_passInnerHitVeto": {"name":"KinkCandidates_passInnerHitVeto", "title":"Number of kink vertices", "bin":5, "xmin":-0.5, "xmax":4.5},
    "nKinkCandidates_passVeto" : {"name":"nKinkCandidates_passVeto", "title":"Number of kink vertices passing the hit veto", "bin":5, "xmin":-0.5, "xmax":4.5},
    "KinkVertex_invMass": {"name":"KinkVertex_invMass", "title":"Invariant mass of kink vertex", "bin":150, "xmin":0, "xmax":150},
    "KinkVertex_dxy": {"name":"KinkVertex_dxy", "title":"dxy of kink vertex", "bin":100, "xmin":0, "xmax":2000},
    "KinkVertex_d3d": {"name":"KinkVertex_d3d", "title":"d3d of kink vertex", "bin":100, "xmin":0, "xmax":2000},
    "KinkVertex_ntracks": {"name":"KinkVertex_ntracks", "title":"Number of tracks in kink vertex", "bin":10, "xmin":-0.5, "xmax":9.5},
    "nKinkVertices": {"name":"nKinkVertices", "title":"Number of kink vertices before hit veto", "bin":5, "xmin":-0.5, "xmax":4.5},
    "KinkAngle": {"name": "KinkAngle", "title": "angle between the r_pvkv and P_kv", "bin":180, "xmin":0, "xmax":180},
    "PV2V0Cos": {"name":"PV2V0Cos", "title":"Cosine angle between displaced verticies and primary vertex", "bin":100, "xmin":-1, "xmax":1},

    "RecoedPrimaryTrack_mass": {"name": "RecoedPrimaryTrack_mass", "title": "Mass of escaping tracks", "bin":50, "xmin":100, "xmax":200},
    "TOF_RecoedPrimaryTracks": {"name": "TOF_RecoedPrimaryTracks", "title": "Time of flight of recoed primary tracks", "bin":200, "xmin":0, "xmax":50000},
    "TOF_sel_tracks": {"name": "TOF_sel_tracks", "title": "Time of flight of sel tracks", "bin":200, "xmin":0, "xmax":50000},
    "RecoedPrimaryTracks_theta": {"name": "RecoedPrimaryTracks_theta", "title": "Recoed primary tracks theta", "bin":30, "xmin":-4, "xmax":4},
    "EscapingTracks_mass": {"name": "EscapingTracks_mass", "title": "Mass of escaping tracks", "bin":50, "xmin":100, "xmax":200},
    "TOF_EscapingTracks": {"name": "TOF_EscapingTracks", "title": "Time of flight of escaping tracks", "bin":200, "xmin":0, "xmax":50000},
}
