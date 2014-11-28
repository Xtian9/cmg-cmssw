from CMGTools.TTHAnalysis.samples.getFiles import getFiles
from CMGTools.TTHAnalysis.samples.getMyFiles import getMyFiles
import CMGTools.RootTools.fwlite.Config as cfg
import os

from CMGTools.TTHAnalysis.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

#AlphaT sample (see https://twiki.cern.ch/twiki/bin/viewauth/CMS/AlphaT#MC_samples_for_CSA14_exercise)

#========================================================PU20bx25 ===================================================


#Component for DYJets
DYJetsToLL_PU20bx25_single = kreator.makeMCComponent("DYJetsToLL_PU20bx25","/DYJetsToLL_M-50_13TeV-pythia6/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS" , "*.root")
DYJetsM50_PU20bx25 = kreator.makeMCComponent("DYJetsM50_PU20bx25", "/DYJetsToLL_M-50_13TeV-madgraph-pythia8/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
DYJetsM50pythia6_PU20bx25 = kreator.makeMCComponent("DYJetsM50pythia6_PU20bx25", "/DYJetsToLL_M-50_13TeV-pythia6/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
DYJetsM50_HT200to400_PU20bx25 = kreator.makeMCComponent("DYJetsM50_HT200to400_PU20bx25", "/DYJetsToLL_M-50_HT-200to400_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
DYJetsM50_HT400to600_PU20bx25 = kreator.makeMCComponent("DYJetsM50_HT400to600_PU20bx25", "/DYJetsToLL_M-50_HT-400to600_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
DYJetsM50_HT600toInf_PU20bx25 = kreator.makeMCComponent("DYJetsM50_HT600toInf_PU20bx25", "/DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
DYJetsMuMuM50_PtZ180_PU20bx25 = kreator.makeMCComponent("DYJetsMuMuM50_PtZ180_PU20bx25", "/DYJetsToMuMu_PtZ-180_M-50_13TeV-madgraph/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
DYJetsMuMuM6pythia8_PU20bx25 = kreator.makeMCComponent("DYJetsMuMuM6pythia8_PU20bx25", "/DYToMuMu_M-6To15_Tune4C_13TeV-pythia8/Spring14miniaod-castor_PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
DYJetsMuMuM15pythia8_PU20bx25 = kreator.makeMCComponent("DYJetsMuMuM15pythia8_PU20bx25", "/DYToMuMu_M-15To50_Tune4C_13TeV-pythia8/Spring14miniaod-castor_PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
DYJetsMuMuM50pythia8_PU20bx25 = kreator.makeMCComponent("DYJetsMuMuM50pythia8_PU20bx25", "/DYToMuMu_M-50_Tune4C_13TeV-pythia8/Spring14miniaod-castor_PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
DYJetsEEpythia8_PU20bx25 = kreator.makeMCComponent("DYJetsEEpythia8_PU20bx25", "/DYToEE_Tune4C_13TeV-pythia8/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
DYJetsMuMupythia8_PU20bx25 = kreator.makeMCComponent("DYJetsMuMupythia8_PU20bx25", "/DYToMuMu_Tune4C_13TeV-pythia8/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
DYJetsToLL_PU20bx25 = [
#DYJetsToLL_PU20bx25_single,
DYJetsM50_PU20bx25,
#DYJetsM50pythia6_PU20bx25,
DYJetsM50_HT200to400_PU20bx25,
DYJetsM50_HT400to600_PU20bx25,
DYJetsM50_HT600toInf_PU20bx25,
#DYJetsMuMuM50_PtZ180_PU20bx25,
#DYJetsMuMuM6pythia8_PU20bx25, 
#DYJetsMuMuM15pythia8_PU20bx25,
#DYJetsMuMuM50pythia8_PU20bx25,
#DYJetsEEpythia8_PU20bx25,
#DYJetsMuMupythia8_PU20bx25,
]

#Components for TTbar
TTbar_PU20bx25_single = kreator.makeMCComponent("TTbar_PU20bx25","/TT_Tune4C_13TeV-pythia8-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
TTJets_PU20bx25 = kreator.makeMCComponent("TTJets_PU20bx25", "/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM", "CMS", ".*root")
TTbar_PU20bx25 =[
TTJets_PU20bx25
]

#Components for GJets
GJet_PU20bx25 = kreator.makeMCComponent("GJet_PU20bx25", "/GJet_Pt-15to3000_Tune4C_13TeV_pythia8/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
GJets_PU20bx25 = [
        GJet_PU20bx25
        ]

#Components for W+Jets
WJets_PU20bx25_single = kreator.makeMCComponent("WJets_PU20bx25", "/W1234JetsToLNu_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
WJetsToLNu_PU20bx25=[
WJets_PU20bx25_single 
        ]

#Susy signal
T1tttt_PU20bx25 = kreator.makeMCComponent("T1tttt_PU20bx25", "/SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
T2tt_PU20bx25_mStop_425_mLSP_325 = kreator.makeMCComponent("T2tt_mStop_425_mLSP_325","/SMS-T2tt_2J_mStop-425_mLSP-325_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS", ".*root")
SusySignalSamples_PU20bx25=[
        T1tttt_PU20bx25, 
        T2tt_PU20bx25_mStop_425_mLSP_325 
        ]
#=========================================================================================================

#===========================================PU40bx50 (PU_S14)============================================

#Components for QCD
QCD_Pt1000to1400_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt1000to1400_PU_S14_POSTLS170", "/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-1000to1400_Tune4C_13TeV_pythia8_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt10to15_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt10to15_PU_S14_POSTLS170", "/QCD_Pt-10to15_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-10to15_Tune4C_13TeV_pythia8_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt120to170_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt120to170_PU_S14_POSTLS170", "/QCD_Pt-120to170_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-120to170_Tune4C_13TeV_pythia8_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt1400to1800_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt1400to1800_PU_S14_POSTLS170", "/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-1400to1800_Tune4C_13TeV_pythia8_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt1800_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt1800_PU_S14_POSTLS170", "/QCD_Pt-1800_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-1800_Tune4C_13TeV_pythia8_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt300to470_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt300to470_PU_S14_POSTLS170", "/QCD_Pt-300to470_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-300to470_Tune4C_13TeV_pythia8_StoreResults-Spring14dr_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt30to50_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt30to50_PU_S14_POSTLS170", "/QCD_Pt-30to50_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-30to50_Tune4C_13TeV_pythia8_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt470to600_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt470to600_PU_S14_POSTLS170", "/QCD_Pt-470to600_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-470to600_Tune4C_13TeV_pythia8_Spring14dr-PU_S14_POSTLS170_t2-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt50to80_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt50to80_PU_S14_POSTLS170", "/QCD_Pt-50to80_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-50to80_Tune4C_13TeV_pythia8_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt5to10_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt5to10_PU_S14_POSTLS170", "/QCD_Pt-5to10_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-5to10_Tune4C_13TeV_pythia8_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt600to800_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt600to800_PU_S14_POSTLS170", "/QCD_Pt-600to800_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-600to800_Tune4C_13TeV_pythia8_StoreResults-Spring14dr_PU20Bx50_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt800to1000_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt800to1000_PU_S14_POSTLS170", "/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-800to1000_Tune4C_13TeV_pythia8_StoreResults-Spring14dr_PU20Bx50_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt80to120_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt80to120_PU_S14_POSTLS170", "/QCD_Pt-80to120_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-80to120_Tune4C_13TeV_pythia8_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt15to30_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt15to30_PU_S14_POSTLS170", "/QCD_Pt-15to30_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-15to30_Tune4C_13TeV_pythia8_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD_Pt170to300_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("QCD_Pt170to300_PU_S14_POSTLS170", "/QCD_Pt-170to300_Tune4C_13TeV_pythia8/phys_susy-miniAODforSusy_QCD_Pt-170to300_Tune4C_13TeV_pythia8_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
QCD = [
QCD_Pt1000to1400_PU_S14_POSTLS170,
#QCD_Pt10to15_PU_S14_POSTLS170,
QCD_Pt120to170_PU_S14_POSTLS170,
QCD_Pt1400to1800_PU_S14_POSTLS170,
QCD_Pt1800_PU_S14_POSTLS170,
QCD_Pt300to470_PU_S14_POSTLS170,
QCD_Pt30to50_PU_S14_POSTLS170,
QCD_Pt470to600_PU_S14_POSTLS170,
QCD_Pt50to80_PU_S14_POSTLS170,
#QCD_Pt5to10_PU_S14_POSTLS170,
QCD_Pt600to800_PU_S14_POSTLS170,
QCD_Pt800to1000_PU_S14_POSTLS170,
QCD_Pt80to120_PU_S14_POSTLS170,
#QCD_Pt15to30_PU_S14_POSTLS170,
QCD_Pt170to300_PU_S14_POSTLS170,
    ]


#Components for DYJets
DYJetsM50_HT100to200_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("DYJetsM50_HT100to200_PU_S14_POSTLS170", "/DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
DYJetsM50_HT200to400_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("DYJetsM50_HT200to400_PU_S14_POSTLS170", "/DYJetsToLL_M-50_HT-200to400_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_DYJetsToLL_M-50_HT-200to400_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
DYJetsM50_HT400to600_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("DYJetsM50_HT400to600_PU_S14_POSTLS170", "/DYJetsToLL_M-50_HT-400to600_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_DYJetsToLL_M-50_HT-400to600_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
DYJetsM50_HT600toInf_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("DYJetsM50_HT600toInf_PU_S14_POSTLS170", "/DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
DYJetsToLL = [
DYJetsM50_HT100to200_PU_S14_POSTLS170,
DYJetsM50_HT200to400_PU_S14_POSTLS170,
DYJetsM50_HT400to600_PU_S14_POSTLS170,
DYJetsM50_HT600toInf_PU_S14_POSTLS170,
]

#Components for TTBar
TTJets_MSDecaysCKM_central_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("TTJets_MSDecaysCKM_central_PU_S14_POSTLS170", "/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola_Spring14dr_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
TTbar=[
    TTJets_MSDecaysCKM_central_PU_S14_POSTLS170         
    ]

#Component for WJetsToLNu
WJetsToLNu_HT100to200_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("WJetsToLNu_HT100to200_PU_S14_POSTLS170", "/WJetsToLNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_WJetsToLNu_HT-100to200_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
WJetsToLNu_HT200to400_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("WJetsToLNu_HT200to400_PU_S14_POSTLS170", "/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
WJetsToLNu_HT400to600_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("WJetsToLNu_HT400to600_PU_S14_POSTLS170", "/WJetsToLNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_WJetsToLNu_HT-400to600_Tune4C_13TeV-madgraph-tauola_Spring14dr_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
WJetsToLNu_HT600toInf_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("WJetsToLNu_HT600toInf_PU_S14_POSTLS170", "/WJetsToLNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_WJetsToLNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
WJetsToLNu = [
WJetsToLNu_HT100to200_PU_S14_POSTLS170,
WJetsToLNu_HT200to400_PU_S14_POSTLS170,
WJetsToLNu_HT400to600_PU_S14_POSTLS170,
WJetsToLNu_HT600toInf_PU_S14_POSTLS170,
]

#Component for ZJetsToNuNu
ZJetsToNuNu_HT100to200_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("ZJetsToNuNu_HT100to200_PU_S14_POSTLS170", "/ZJetsToNuNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_ZJetsToNuNu_HT-100to200_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
ZJetsToNuNu_HT200to400_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("ZJetsToNuNu_HT200to400_PU_S14_POSTLS170", "/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
ZJetsToNuNu_HT400to600_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("ZJetsToNuNu_HT400to600_PU_S14_POSTLS170", "/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
ZJetsToNuNu_HT600toInf_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("ZJetsToNuNu_HT600toInf_PU_S14_POSTLS170", "/ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
ZJetsToNuNu = [
ZJetsToNuNu_HT100to200_PU_S14_POSTLS170,
ZJetsToNuNu_HT200to400_PU_S14_POSTLS170,
ZJetsToNuNu_HT400to600_PU_S14_POSTLS170,
ZJetsToNuNu_HT600toInf_PU_S14_POSTLS170,
]

#Component for GJets
GJets_HT100to200_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("GJets_HT100to200_PU_S14_POSTLS170", "/GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola_Spring14dr_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
GJets_HT200to400_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("GJets_HT200to400_PU_S14_POSTLS170", "/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
GJets_HT400to600_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("GJets_HT400to600_PU_S14_POSTLS170", "/GJets_HT-400to600_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_GJets_HT-400to600_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
GJets_HT600toInf_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("GJets_HT600toInf_PU_S14_POSTLS170", "/GJets_HT-600toInf_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_GJets_HT-600toInf_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
GJets = [
GJets_HT100to200_PU_S14_POSTLS170,
GJets_HT200to400_PU_S14_POSTLS170,
GJets_HT400to600_PU_S14_POSTLS170,
GJets_HT600toInf_PU_S14_POSTLS170,
]


#Components for SUSY samples
SMS_T1bbbb_2J_mGl1000_mLSP900_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("SMS_T1bbbb_2J_mGl1000_mLSP900_PU_S14_POSTLS170", "/SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
SMS_T1bbbb_2J_mGl1500_mLSP100_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("SMS_T1bbbb_2J_mGl1500_mLSP100_PU_S14_POSTLS170", "/SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
SMS_T1qqqq_2J_mGl1000_mLSP800_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("SMS_T1qqqq_2J_mGl1000_mLSP800_PU_S14_POSTLS170", "/SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
SMS_T1qqqq_2J_mGl1400_mLSP100_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("SMS_T1qqqq_2J_mGl1400_mLSP100_PU_S14_POSTLS170", "/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
SMS_T1tttt_2J_mGl1200_mLSP800_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("SMS_T1tttt_2J_mGl1200_mLSP800_PU_S14_POSTLS170", "/SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
SMS_T1tttt_2J_mGl1500_mLSP100_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("SMS_T1tttt_2J_mGl1500_mLSP100_PU_S14_POSTLS170", "/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")

SusySignalSamples = [
    SMS_T1bbbb_2J_mGl1000_mLSP900_PU_S14_POSTLS170,
    SMS_T1bbbb_2J_mGl1500_mLSP100_PU_S14_POSTLS170,
    SMS_T1qqqq_2J_mGl1000_mLSP800_PU_S14_POSTLS170,
    SMS_T1qqqq_2J_mGl1400_mLSP100_PU_S14_POSTLS170,
    SMS_T1tttt_2J_mGl1200_mLSP800_PU_S14_POSTLS170,
    SMS_T1tttt_2J_mGl1500_mLSP100_PU_S14_POSTLS170,
    ]
#===========================================================================

#Combine different samples for running, modify to configure which sample you want to use
mcSamples = WJetsToLNu+DYJetsToLL_PU20bx25+ZJetsToNuNu+GJets+TTbar_PU20bx25+QCD+TTbar+DYJetsToLL+SusySignalSamples + SusySignalSamples_PU20bx25+WJetsToLNu_PU20bx25 + GJets_PU20bx25
mcSamples_PU20bx25 = DYJetsToLL_PU20bx25+TTbar_PU20bx25+SusySignalSamples_PU20bx25+WJetsToLNu_PU20bx25 + GJets_PU20bx25 
mcSamples_PU40bx50 =  WJetsToLNu+ZJetsToNuNu+DYJetsToLL+GJets+QCD+TTbar+SusySignalSamples

dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"

from CMGTools.TTHAnalysis.setup.Efficiencies import *

#Define splitting
for comp in mcSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 100 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012




# samples below don't work now as some are not at Tier-2 CERN, need fix later
# WJetsToLNu_PU20bx25 = kreator.makeMCComponent("WJetsToLNu_PU20bx25","/WJetsToLNu_13TeV-madgraph-pythia8-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS" , "*.root")
# # "/DYJetsToLL_M-50_13TeV-pythia6/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# # "/DYJetsToLL_M-50_13TeV-madgraph-pythia8-tauola_v2/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# # "/DYJetsToLL_M-50_13TeV-madgraph-pythia8/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# ZJetsToNuNu_HT100to200_PU20bx25 = kreator.makeMCComponent("ZJetsToNuNu_HT100to200_PU20bx25","/ZJetsToNuNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# ZJetsToNuNu_HT200to400_PU20bx25 = kreator.makeMCComponent("ZJetsToNuNu_HT200to400_PU20bx25","/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# ZJetsToNuNu_HT400to600_PU20bx25 = kreator.makeMCComponent("ZJetsToNuNu_HT400to600_PU20bx25","/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# ZJetsToNuNu_HT600toInf_PU20bx25 = kreator.makeMCComponent("ZJetsToNuNu_HT600toInf_PU20bx25","/ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# GJets_HT100to200_PU20bx25 = kreator.makeMCComponent("GJets_HT100to200_PU20bx25","/GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# GJets_HT200to400_PU20bx25 = kreator.makeMCComponent("GJets_HT200to400_PU20bx25","/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# GJets_HT400to600_PU20bx25 = kreator.makeMCComponent("GJets_HT400to600_PU20bx25","/GJets_HT-400to600_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# GJets_HT600toInf_PU20bx25 = kreator.makeMCComponent("GJets_HT600toInf_PU20bx25","/GJets_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# T1bbbb_mGl1000mLSP900_PU20bx25 = kreator.makeMCComponent("T1bbbb_mGl1000mLSP900_PU20bx25","/SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM","CMS","*.root")
# # "/SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# # "/SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM"
# # "/SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v3/MINIAODSIM"
# T1tttt_mGl1200mLSP800_PU20bx25 = kreator.makeMCComponent("T1tttt_mGl1200mLSP800_PU20bx25","/SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM","CMS","*.root")
# # "/SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# # "/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# # "/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM"
# T1qqqq_mGl1000mLSP800_PU20bx25 = kreator.makeMCComponent("SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauolaLSP800_PU20bx25","/SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM","CMS","*root")
# # "/SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM"
# # "/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# # "/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM"
# TToBLNu_schannelEMu_PU20bx25 = kreator.makeMCComponent("TToBLNu_schannelEMu_PU20bx25","/TToBLNu_s-channel-EMu_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# TToBLNu_tchannelEMu_PU20bx25 = kreator.makeMCComponent("TToBLNu_tchannelEMu_PU20bx25","/TToBLNu_t-channel-EMu_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# TToBLNu_tWchannelDREMu_PU20bx25 = kreator.makeMCComponent("TToBLNu_tWchannelDREMu_PU20bx25","/TToBLNu_tW-channel-DR-EMu_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM","CMS","*.root")

# samples below don't work now as some are not at Tier-2 CERN, need fix later
# WJetsToLNu_PU20bx25,
# DYJetsToLL_PU20bx25,
# ZJetsToNuNu_HT100to200_PU20bx25, 
# ZJetsToNuNu_HT200to400_PU20bx25, 
# ZJetsToNuNu_HT400to600_PU20bx25, 
# ZJetsToNuNu_HT600toInf_PU20bx25, 
# GJets_HT100to200_PU20bx25, 
# GJets_HT200to400_PU20bx25, 
# GJets_HT400to600_PU20bx25, 
# GJets_HT600toInf_PU20bx25, 
# TToBLNu_schannelEMu_PU20bx25,
# TToBLNu_tchannelEMu_PU20bx25,
# TToBLNu_tWchannelDREMu_PU20bx25, 
# T1qqqq_mGl1000mLSP800_PU20bx25,
# T1bbbb_mGl1000mLSP900_PU20bx25,
# T1tttt_mGl1200mLSP800_PU20bx25,
