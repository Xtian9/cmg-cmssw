import CMGTools.RootTools.fwlite.Config as cfg
from CMGTools.RootTools.RootTools import *
from CMGTools.RootTools.fwlite.Config import printComps

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cfg import *
from CMGTools.TTHAnalysis.config.config_cfi import alphaTPSet
import sys

puRegime = alphaTPSet.puRegime
cutFlow = alphaTPSet.cutFlow
test = alphaTPSet.test

if cutFlow=='SingleMu':
    ttHLepAna.loose_muon_pt   = 30.
    ttHLepAna.loose_muon_eta  = 2.1
    ttHMuonSkim.minObjects  = 1
    ttHMuonSkim.maxObjects  = 1
    ttHIsoTrackSkim.allowedMuon  = 1 #
    ttHAlphaTSkim.alphaTCuts = [(0.0, 200,99999 )]   #Turn off AlphaT cut 
    ttHAlphaTSkim.mhtDivMetCut = ('mhtJet50j','metNoMu',1.25)
    ttHAlphaTControlSkim.mtwCut = (30,125)
    ttHAlphaTControlSkim.lepDeltaRCut = 0.5

elif cutFlow=='DoubleMu':
    ttHLepAna.loose_muon_pt   = 30.
    ttHLepAna.loose_muon_eta  = 2.1
    ttHMuonSkim.minObjects  = 2
    ttHMuonSkim.maxObjects  = 2
    ttHIsoTrackSkim.allowedMuon  = 2 #
    ttHAlphaTSkim.alphaTCuts = [(0.0, 200,99999 )]   #Turn off AlphaT cut
    ttHAlphaTSkim.mhtDivMetCut = ('mhtJet50j','metNoMu',1.25)
    ttHAlphaTControlSkim.mllCut = (66.2,116.2)
    ttHAlphaTControlSkim.lepDeltaRCut = 0.5

elif cutFlow=='SinglePhoton':
    ttHPhoAna.ptMin = 165
    ttHPhoAna.etaMax = 1.45
    ttHPhotonSkim.minObjects  = 1
    ttHPhotonSkim.maxObjects  = 1 
    ttHAlphaTSkim.alphaTCuts = [(0.55, 375,99999 )]   
    ttHAlphaTControlSkim.photonDeltaRCut = 1.0
    ttHAlphaTSkim.mhtDivMetCut = ('mhtJet50j','met',9999) #turn off MHT/MET cut

elif cutFlow=='SingleEle':
    ttHElectronSkim.minObjects  = 1
    ttHElectronSkim.maxObjects  = 1
    ttHIsoTrackSkim.allowedElectron  = 1 #

elif cutFlow=='DoubleEle':
    ttHElectronSkim.minObjects  = 2
    ttHElectronSkim.maxObjects  = 2
    ttHIsoTrackSkim.allowedElectron  = 2 #

elif cutFlow=='MultiJetEnriched':
    ttHAlphaTSkim.invertAlphaT = True

elif cutFlow=='Inclusive':
    ttHJetMETSkim.jetPtCuts   = [0] # require the lead two jets to be above 100GeV
    ttHJetMETSkim.htCut       = ('htJet50j', -1000)
    ttHJetMETSkim.mhtCut      = ('mhtJet50j', -1000)
    ttHElectronSkim.minObjects  = 0 
    ttHElectronSkim.maxObjects  = 9999
    ttHMuonSkim.minObjects  = 0
    ttHMuonSkim.maxObjects  = 9999
    ttHPhotonSkim.minObjects  = 0
    ttHPhotonSkim.maxObjects  = 9999 
    ttHIsoTrackSkim.minObjects = 0
    ttHIsoTrackSkim.maxObjects = 9999
    ttHAlphaTSkim.alphaTCuts = [(0.0, -1000,99999 )]   #Turn off AlphaT cut
    ttHAlphaTSkim.mhtDivMetCut = ('mhtJet50j','met',9999) #turn off MHT/MET cut

elif cutFlow=='Test':
    ttHMuonSkim.maxObjects     = 99
    ttHMuonSkim.minObjects     = 0
    ttHElectronSkim.maxObjects     = 99
    ttHElectronSkim.minObjects     = 0
    ttHAlphaTSkim.invertAlphaT = True
    ttHPhotonSkim.minPhotons  = 0
    ttHPhotonSkim.maxPhotons  = 9999
    ttHPhotonSkim.ptCuts = [25]
    ttHIsoTrackSkim.minObjects  = 0 # 
    ttHIsoTrackSkim.maxObjects  = 9999 #

##------------------------------------------
##  PRODUCER
##------------------------------------------

from CMGTools.TTHAnalysis.samples.samples_8TeV_v517 import triggers_RA1_Bulk, triggers_RA1_Prompt, triggers_RA1_Parked, triggers_RA1_Single_Mu, triggers_RA1_Photon, triggers_RA1_Muon

# Tree Producer
treeProducer = cfg.Analyzer(
        'treeProducerSusyAlphaT',
        vectorTree = True,
        PDFWeights = PDFWeights,
        triggerBits = {
            'Bulk'     : triggers_RA1_Bulk,
            'Prompt'   : triggers_RA1_Prompt,
            'Parked'   : triggers_RA1_Parked,
            'SingleMu' : triggers_RA1_Single_Mu,
            'Photon'   : triggers_RA1_Photon,
            'Muon'     : triggers_RA1_Muon,
            }
        )

    #-------- SAMPLES AND TRIGGERS -----------
    # from CMGTools.TTHAnalysis.samples.samples_13TeV_CSA14 import *

#if __name__ is not "run_susyAlphaT_cfg": 
     #If running pybatch make sure naming isn't messed up by config
from CMGTools.TTHAnalysis.samples.samples_13TeV_AlphaT import *

selectedComponents = []

if cutFlow == 'Signal':
    if puRegime == 'PU40bx50':
        selectedComponents = WJetsToLNu + ZJetsToNuNu + TTbar + SusySignalSamples + QCD
    elif puRegime == 'PU20bx25':
        selectedComponents = WJetsToLNu_PU20bx25 + TTbar_PU20bx25 + SusySignalSamples_PU20bx25

elif cutFlow == 'SingleMu':
    if puRegime == 'PU40bx50':
        selectedComponents = WJetsToLNu + TTbar + QCD
    elif puRegime == 'PU20bx25':
        selectedComponents = WJetsToLNu_PU20bx25 + TTbar_PU20bx25

elif cutFlow == 'DoubleMu':
    if puRegime == 'PU40bx50':
        selectedComponents = DYJetsToLL + QCD
    elif puRegime == 'PU20bx25':
        selectedComponents = DYJetsToLL_PU20bx25

elif cutFlow == 'SinglePhoton':
    if puRegime == 'PU40bx50':
        selectedComponents = GJets + QCD
    elif puRegime == 'PU20bx25':
        selectedComponents = GJets_PU20bx25 

elif cutFlow == 'MultiJetEnriched':
    if puRegime == 'PU40bx50':
        selectedComponents = QCD
    elif puRegime == 'PU20bx25':
        selectedComponents = []

elif cutFlow == 'Inclusive':
    if puRegime == 'PU40bx50':
        selectedComponents = WJetsToLNu + ZJetsToNuNu + TTbar + SusySignalSamples + QCD + GJets + DYJetsToLL
    elif puRegime == 'PU20bx25':
        selectedComponents = WJetsToLNu_PU20bx25 + TTbar_PU20bx25 + SusySignalSamples_PU20bx25 + DYJetsToLL_PU20bx25 + GJets_PU20bx25 


else:
    print 'Please choose correct cutFlow and PU regime'
    #selectedComponents.extend( mcSamples )

#-------- SEQUENCE

sequence = cfg.Sequence(susyCoreSequence + [
                        ttHPhotonSkim,
                        ttHMuonSkim,
                        ttHElectronSkim,
                        ttHIsoTrackAna,
                        ttHIsoTrackSkim,
                        ttHAlphaTAna,
                        ttHAlphaTControlAna,
                        ttHAlphaTSkim,
                        ttHAlphaTControlSkim,
                        treeProducer,
                        ])


#-------- HOW TO RUN
# test = 0 for batch submission
# test = n != 0 for interactive mucking about

if alphaTPSet.limitFiles:
    for comp in selectedComponents:
        comp.splitFactor = 2
        comp.files = comp.files[:2]

# Test a single component, using a single thread.
#--------------------------------------------------
if test==1:
    comp               = SMS_T1tttt_2J_mGl1200_mLSP800_PU_S14_POSTLS170
    #comp = DYJetsM50_HT200to400_PU_S14_POSTLS170
    #comp = ZJetsToNuNu_HT200to400_PU_S14_POSTLS170
    #comp = WJetsToLNu_HT400to600_PU_S14_POSTLS170
    if cutFlow == 'SinglePhoton':
        comp = GJets_HT600toInf_PU_S14_POSTLS170  
    #comp.files = ['/afs/cern.ch/work/p/pandolf/CMSSW_7_0_6_patch1_2/src/CMGTools/TTHAnalysis/cfg/pickevents.root']
    comp.files         = comp.files[:1]
    
    selectedComponents = [comp]
    comp.splitFactor   = 1
#--------------------------------------------------

# Test all components (1 thread per component).
#--------------------------------------------------
elif test==2:
    selectedComponents=QCD
    for comp in selectedComponents:
        comp.splitFactor = 4
        comp.files       = comp.files[:1]
#--------------------------------------------------


# Run on local files
#--------------------------------------------------
elif test==4:
    comp = TTbar_PU20bx25 

#    comp.name = 'TTJets'
    #    comp.files = [ '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/063013AD-9907-E411-8135-0026189438BD.root' ]

    comp.files = [ '/afs/cern.ch/user/m/mbaber/WORK/public/CSA14Samples/TT_Tune4C_13TeV-pythia8_PU20bx25.root' ]

    selectedComponents = [comp]
    comp.splitFactor = 1
#--------------------------------------------------

config = cfg.Config( components = selectedComponents,
                     sequence = sequence )

if __name__ == "pycfg":
    if not test == alphaTPSet.test or not cutFlow == alphaTPSet.cutFlow or not puRegime == alphaTPSet.puRegime:
        sys.exit("Stop fannying about with variable names")

printComps(config.components, True)

