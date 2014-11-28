from CMGTools.RootTools.fwlite.Config import printComps
from CMGTools.RootTools.RootTools import *
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

##------------------------------------------
## Redefine analyzer parameters
##------------------------------------------

# Muons
#------------------------------
ttHLepAna.loose_muon_pt               = 10.
ttHLepAna.loose_muon_eta              = 2.5
ttHLepAna.loose_muon_id               = "POG_ID_Tight"
ttHLepAna.loose_muon_dxy              = 0.2
ttHLepAna.loose_muon_dz               = 0.5
ttHLepAna.loose_muon_relIso           = 0.12
#
## Electrons
##------------------------------
ttHLepAna.loose_electron_id           = "POG_Cuts_ID_2012_Loose"
#ttHLepAna.loose_electron_id          = "POG_CSA14_25ns_v1_Loose"  

ttHLepAna.loose_electron_pt           = 10
ttHLepAna.loose_electron_eta          = 2.5
ttHLepAna.loose_electron_dxy          = 0.02
ttHLepAna.loose_electron_dz           = 0.2
ttHLepAna.loose_electron_relIso       = 0.15
ttHLepAna.loose_electron_lostHits     = 1 
# ttHLepAna.inclusive_electron_lostHits = 999 # no cut
ttHLepAna.ele_isoCorr                 = "rhoArea"
ttHLepAna.ele_tightId                 = "Cuts_2012"

# Photons
#------------------------------
ttHPhoAna.ptMin                       = 25
ttHPhoAna.etaMax                      = 2.5
#ttHPhoAna.gammaID                     = "PhotonCutBasedIDLoose"
ttHPhoAna.gammaID                     = "PhotonCutBasedIDTight"

# Taus 
#------------------------------
ttHTauAna.etaMax         = 2.3
ttHTauAna.dxyMax         = 99999.
ttHTauAna.dzMax          = 99999.
ttHTauAna.vetoLeptons    = False
ttHTauAna.vetoLeptonsPOG = True


# Jets (for event variables do apply the jetID and not PUID yet)
#------------------------------
ttHJetAna.relaxJetId      = False
ttHJetAna.doPuId          = False
ttHJetAna.jetEta          = 5.
ttHJetAna.jetEtaCentral   = 3.
ttHJetAna.jetPt           = 50.
ttHJetAna.recalibrateJets = False
ttHJetAna.jetLepDR        = 0.4
ttHJetMCAna.smearJets     = False

#Sums
#-------------------------------
#Make the met without muons
ttHMetAna.doMetNoMu = True


##------------------------------------------
##  ISOLATED TRACK
##------------------------------------------

# those are the cuts for the nonEMu
ttHIsoTrackAna = cfg.Analyzer(
            'ttHIsoTrackAnalyzer',
#            candidates='cmgCandidates',
#            candidatesTypes='std::vector<cmg::Candidate>',
            candidates      ='packedPFCandidates',
            candidatesTypes ='std::vector<pat::PackedCandidate>',
            ptMin           = 10, ### for pion 
            ptMinEMU        = 10, ### for EMU
            dzMax           = 0.05,
            #####
            isoDR           = 0.3,
            ptPartMin       = 0,
            dzPartMax       = 0.1,
            maxAbsIso       = 8,
            #####
            MaxIsoSum       = 0.1, ### unused
            MaxIsoSumEMU    = 0.2, ### unused
            doSecondVeto    = False,
            )


##------------------------------------------
##  ALPHAT VARIABLES
##------------------------------------------

# Make alphaT and biased delta phi
ttHAlphaTAna = cfg.Analyzer(
            'ttHAlphaTVarAnalyzer'
            )

# Make mtw, z mass and deltaR between leptons and jet
ttHAlphaTControlAna = cfg.Analyzer(
            'ttHAlphaTControlAnalyzer'
            )

#-------------------------------------------
# CUTS AND VETOS
#-------------------------------------------

#Start with the signal region default cut flow

#ESums
ttHJetMETSkim.jetPtCuts   = [100,100] # require the lead two jets to be above 100GeV
ttHJetMETSkim.htCut       = ('htJet50j', 200)
ttHJetMETSkim.mhtCut      = ('mhtJet50j', 0)
ttHJetMETSkim.nBJet       = ('CSVM', 0, "jet.pt() > 50")     # require at least 0 jets passing CSVM and pt > 50


#Photons
ttHPhotonSkim = cfg.Analyzer(
    'ttHObjectSkimmer',
    skimmerName = 'ttHPhotonSkimmer',
    objects = 'selectedPhotons',
    minObjects = 0,
    maxObjects = 0,
    #idCut  = "object.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the objects
    )

#Muons
ttHMuonSkim = cfg.Analyzer(
    'ttHObjectSkimmer',
    skimmerName = 'ttHMuonSkimmer',
    objects = 'selectedMuons',
    minObjects = 0,
    maxObjects = 0,
    #idCut  = "object.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the objects
    )

#Electrons
ttHElectronSkim = cfg.Analyzer(
    'ttHObjectSkimmer',
    skimmerName = 'ttHElectronSkimmer',
    objects = 'selectedElectrons',
    minObjects = 0,
    maxObjects = 0,
    #idCut  = "object.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the objects
    )

#Isolated tracks
ttHIsoTrackSkim = cfg.Analyzer(
    'ttHIsoTrackSkimmer',
    objects = 'selectedIsoTrack',
    minObjects = 0,
    maxObjects = 0,
    allowedMuon = 0,
    allowedElectron = 0,
    #idCut  = "object.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the objects
    )

#AlphaT Specific cuts

ttHAlphaTSkim = cfg.Analyzer(
            'ttHAlphaTSkimmer',
            forwardJetVeto = True,
            alphaTCuts = [(0.65, 200, 275),   #AlphaT cut in HT region
                          (0.60, 275, 325),   #(aT, HTlow, HThigh)
                          (0.55, 325, 99999)],#Any region not specified will be vetoed
            invertAlphaT = False, #Invert the alphaT requirement
            mhtDivMetCut = ('mhtJet50j','met',1.25), #MHT/MET cut
            )

ttHAlphaTControlSkim = cfg.Analyzer(
            'ttHAlphaTControlSkimmer',
            mtwCut = (-99999,99999),
            mllCut = (-99999,99999),
            lepDeltaRCut = 0,
            photonDeltaRCut = 0,
            )
