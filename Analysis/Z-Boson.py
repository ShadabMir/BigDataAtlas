import hist 
from hist import Hist
import uproot
import numpy as np
import matplotlib.pyplot as plt
from TLorentzVector import TLorentzVector
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
file1 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/exactly2lep/Data/data_D.exactly2lep.root:mini")
file2 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/exactly2lep/Data/data_C.exactly2lep.root:mini")
file3 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/exactly2lep/Data/data_B.exactly2lep.root:mini")
file4 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/exactly2lep/Data/data_A.exactly2lep.root:mini")
file5 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/3lep/Data/data_D.3lep.root:mini")
file6 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/3lep/Data/data_C.3lep.root:mini")
file7 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/3lep/Data/data_B.3lep.root:mini")
file8 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/3lep/Data/data_A.3lep.root:mini")
file9 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/4lep/Data/data_D.4lep.root:mini")
file10 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/4lep/Data/data_C.4lep.root:mini")
file11 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/4lep/Data/data_B.4lep.root:mini")
file12 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/4lep/Data/data_A.4lep.root:mini")
filejeta = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1largeRjet1lep/Data/data_A.1largeRjet1lep.root:mini")
filejetb= uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1largeRjet1lep/Data/data_B.1largeRjet1lep.root:mini")
filejetc = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1largeRjet1lep/Data/data_C.1largeRjet1lep.root:mini")
filejetd = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1largeRjet1lep/Data/data_D.1largeRjet1lep.root:mini")
filetaua = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1lep1tau/Data/data_A.1lep1tau.root:mini")
filetaub = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1lep1tau/Data/data_B.1lep1tau.root:mini")
filetauc = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1lep1tau/Data/data_C.1lep1tau.root:mini")
filetaud = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1lep1tau/Data/data_D.1lep1tau.root:mini")
firstlepton = TLorentzVector()
secondlepton = TLorentzVector()
thirdlepton = TLorentzVector()
fourthlepton = TLorentzVector()

fileaa = [file4,file5,file6,file7,file8,file9,file10,file11,file12]
histexact = Hist(hist.axis.Regular(50,40,140,label = "Mass(GeV)"))
for tree in fileaa:
    parameters = tree.arrays(["lep_n","lep_charge","lep_type","lep_pt","lep_eta","lep_phi","lep_E","lep_isTightID","lep_ptcone30","lep_etcone20"])
    for event in parameters:
        lep_n = event["lep_n"]
        if lep_n >= 2 and lep_n <= 2:
            lep_charge = event["lep_charge"]
            if lep_charge[0] != lep_charge[1]:
                lep_type = event["lep_type"]
                if lep_type[0] == lep_type[1]:
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_pt = event["lep_pt"]
                    lep_E = event["lep_E"]
                    lep_istight = event["lep_isTightID"]
                    lep_ptcone = event["lep_ptcone30"]
                    lep_etcone = event["lep_etcone20"]
                    if np.abs(lep_eta[0])<2.4 and np.abs(lep_eta[1])<2.4:
                        if (lep_istight[0]) and (lep_istight[1]):
                            if ((lep_ptcone[0] / lep_pt[0] < 0.15) and (lep_etcone[0]/lep_pt[0] < 0.15)) and ((lep_ptcone[1] / lep_pt[1] < 0.15) and (lep_etcone[1]/lep_pt[1] < 0.15)):
                                 if lep_pt[0]/1000. >25 and lep_pt[1]/1000. >20:
                                        
                                    firstlepton.SetPtEtaPhiE(lep_pt[0]/1000.,lep_eta[0],lep_phi[0],lep_E[0]/1000.)
                                    secondlepton.SetPtEtaPhiE(lep_pt[1]/1000.,lep_eta[1],lep_phi[1],lep_E[1]/1000.)
                                    Z0_boson = firstlepton + secondlepton
                                    histexact.fill(Z0_boson.M())
        elif lep_n >= 3 and lep_n <= 3:
            lep_charge = event["lep_charge"]
            if lep_charge[0] != lep_charge[1]:
                lep_type = event["lep_type"]
                if lep_type[0] == lep_type[1]:
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_pt = event["lep_pt"]
                    lep_E = event["lep_E"]
                    lep_istight = event["lep_isTightID"]
                    lep_ptcone = event["lep_ptcone30"]
                    lep_etcone = event["lep_etcone20"]
                    if np.abs(lep_eta[0])<2.4 and np.abs(lep_eta[1])> 2.4 :
                         if (lep_istight[0]) and (lep_istight[1]):
                            if ((lep_ptcone[0] / lep_pt[0] < 0.15) and (lep_etcone[0]/lep_pt[0] < 0.15)) and ((lep_ptcone[1] / lep_pt[1] < 0.15) and (lep_etcone[1]/lep_pt[1] < 0.15)):
                                 if lep_pt[0]/1000. >25 and lep_pt[1]/1000. >20:
                                        
                                    firstlepton.SetPtEtaPhiE(lep_pt[0]/1000.,lep_eta[0],lep_phi[0],lep_E[0]/1000.)
                                    secondlepton.SetPtEtaPhiE(lep_pt[1]/1000.,lep_eta[1],lep_phi[1],lep_E[1]/1000.)
                                    Z0_boson = firstlepton + secondlepton
                                    histexact.fill(Z0_boson.M())
            if lep_charge[1] != lep_charge[2]:
                lep_type = event["lep_type"]
                if lep_type[1] == lep_type[2]:
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_pt = event["lep_pt"]
                    lep_E = event["lep_E"]
                    lep_istight = event["lep_isTightID"]
                    lep_ptcone = event["lep_ptcone30"]
                    lep_etcone = event["lep_etcone20"]
                    if np.abs(lep_eta[2])<2.4 and np.abs(lep_eta[1])<2.4 :
                         if (lep_istight[2]) and (lep_istight[1]):
                            if ((lep_ptcone[1] / lep_pt[1] < 0.15) and (lep_etcone[1]/lep_pt[1] < 0.15)) and ((lep_ptcone[2] / lep_pt[2] < 0.15) and (lep_etcone[2]/lep_pt[2] < 0.15)):
                                 if lep_pt[1]/1000. >25 and lep_pt[2]/1000. >20:
                                        
                                    thirdlepton.SetPtEtaPhiE(lep_pt[2]/1000.,lep_eta[2],lep_phi[2],lep_E[2]/1000.)
                                    secondlepton.SetPtEtaPhiE(lep_pt[1]/1000.,lep_eta[1],lep_phi[1],lep_E[1]/1000.)
                                    Z0_boson = thirdlepton + secondlepton
                                    histexact.fill(Z0_boson.M())
            if lep_charge[0] != lep_charge[2]:
                lep_type = event["lep_type"]
                if lep_type[0] == lep_type[2]:
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_pt = event["lep_pt"]
                    lep_E = event["lep_E"]
                    lep_istight = event["lep_isTightID"]
                    lep_ptcone = event["lep_ptcone30"]
                    lep_etcone = event["lep_etcone20"]
                    if np.abs(lep_eta[0])<2.4 and np.abs(lep_eta[2])< 2.4:
                         if (lep_istight[0]) and (lep_istight[2]):
                            if ((lep_ptcone[0] / lep_pt[0] < 0.15) and (lep_etcone[0]/lep_pt[0] < 0.15)) and ((lep_ptcone[1] / lep_pt[1] < 0.15) and (lep_etcone[1]/lep_pt[1] < 0.15)):
                                 if lep_pt[0]/1000. >25 and lep_pt[1]/1000. >20:
                                        
                                    firstlepton.SetPtEtaPhiE(lep_pt[0]/1000.,lep_eta[0],lep_phi[0],lep_E[0]/1000.)
                                    thirdlepton.SetPtEtaPhiE(lep_pt[2]/1000.,lep_eta[2],lep_phi[2],lep_E[2]/1000.)
                                    Z0_boson = firstlepton + thirdlepton
                                    histexact.fill(Z0_boson.M())
        elif lep_n >= 4 and lep_n <= 4:
            
            lep_charge = event["lep_charge"]
            if (lep_charge[0] != lep_charge[1]):
                lep_type = event["lep_type"]
                if (lep_type[0] == lep_type[1]):
                    lep_pt = event["lep_pt"]
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_E = event["lep_E"]
                    lep_istight = event["lep_isTightID"]
                    lep_ptcone = event["lep_ptcone30"]
                    lep_etcone = event["lep_etcone20"]
                    if np.abs(lep_eta[0])<2.4 and np.abs(lep_eta[1])< 2.4:
                         if (lep_istight[0]) and (lep_istight[1]):
                            if ((lep_ptcone[0] / lep_pt[0] < 0.15) and (lep_etcone[0]/lep_pt[0] < 0.15)) and ((lep_ptcone[1] / lep_pt[1] < 0.15) and (lep_etcone[1]/lep_pt[1] < 0.15)):
                                 if lep_pt[0]/1000. >25 and lep_pt[1]/1000. >20:
                                        
                                    firstlepton.SetPtEtaPhiE(lep_pt[0]/1000,lep_eta[0],lep_phi[0],lep_E[0]/1000)
                                    secondlepton.SetPtEtaPhiE(lep_pt[1]/1000,lep_eta[1],lep_phi[1],lep_E[1]/1000)
                                    Z0_boson1 = firstlepton + secondlepton
                                    histexact.fill(Z0_boson1.M())   
            if (lep_charge[2] != lep_charge[3]):
                lep_type = event["lep_type"]
                if  (lep_type[2] == lep_type[3]):
                    lep_pt = event["lep_pt"]
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_E = event["lep_E"]
                    lep_istight = event["lep_isTightID"]
                    lep_ptcone = event["lep_ptcone30"]
                    lep_etcone = event["lep_etcone20"]
                    if np.abs(lep_eta[3])<2.4 and np.abs(lep_eta[2])< 2.4:
                         if (lep_istight[3]) and (lep_istight[2]):
                            if ((lep_ptcone[3] / lep_pt[3] < 0.15) and (lep_etcone[3]/lep_pt[3] < 0.15)) and ((lep_ptcone[2] / lep_pt[2] < 0.15) and (lep_etcone[2]/lep_pt[2] < 0.15)):
                                 if lep_pt[2]/1000. >25 and lep_pt[3]/1000. >20:
                                    thirdlepton.SetPtEtaPhiE(lep_pt[2]/1000,lep_eta[2],lep_phi[2],lep_E[2]/1000)
                                    fourthlepton.SetPtEtaPhiE(lep_pt[3]/1000,lep_eta[3],lep_phi[3],lep_E[3]/1000)
                                    Z0_boson2 = thirdlepton + fourthlepton
                                    histexact.fill(Z0_boson2.M())
            
            if (lep_charge[0] != lep_charge[2]):
                lep_type = event["lep_type"]
                if (lep_type[0]== lep_type[2]) :
                    lep_pt = event["lep_pt"]
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_E = event["lep_E"]
                    lep_istight = event["lep_isTightID"]
                    lep_ptcone = event["lep_ptcone30"]
                    lep_etcone = event["lep_etcone20"]
                    if np.abs(lep_eta[0])<2.4 and np.abs(lep_eta[2])< 2.4:
                         if (lep_istight[0]) and (lep_istight[2]):
                            if ((lep_ptcone[0] / lep_pt[0] < 0.15) and (lep_etcone[0]/lep_pt[0] < 0.15)) and ((lep_ptcone[2] / lep_pt[2] < 0.15) and (lep_etcone[2]/lep_pt[2] < 0.15)):
                                 if lep_pt[0]/1000. >25 and lep_pt[2]/1000. >20:
                                    firstlepton.SetPtEtaPhiE(lep_pt[0]/1000,lep_eta[0],lep_phi[0],lep_E[0]/1000)
                                    thirdlepton.SetPtEtaPhiE(lep_pt[2]/1000,lep_eta[2],lep_phi[2],lep_E[2]/1000)
                                    Z0_boson1 = firstlepton + thirdlepton
                                    histexact.fill(Z0_boson1.M())
            if (lep_charge[1] != lep_charge[3]):
                lep_type = event["lep_type"]
                if (lep_type[1] == lep_type[3]):
                    lep_pt = event["lep_pt"]
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_E = event["lep_E"]
                    lep_istight = event["lep_isTightID"]
                    lep_ptcone = event["lep_ptcone30"]
                    lep_etcone = event["lep_etcone20"]
                    if np.abs(lep_eta[1])<2.4 and np.abs(lep_eta[3])< 2.4: 
                         if (lep_istight[3]) and (lep_istight[1]):
                            if ((lep_ptcone[1] / lep_pt[1] < 0.15) and (lep_etcone[1]/lep_pt[1] < 0.15)) and ((lep_ptcone[3] / lep_pt[3] < 0.15) and (lep_etcone[3]/lep_pt[3] < 0.15)):
                                 if lep_pt[1]/1000. >25 and lep_pt[3]/1000. >20:
                                        
                                    secondlepton.SetPtEtaPhiE(lep_pt[1]/1000,lep_eta[1],lep_phi[1],lep_E[1]/1000)
                                    fourthlepton.SetPtEtaPhiE(lep_pt[3]/1000,lep_eta[3],lep_phi[3],lep_E[3]/1000)
                                    Z0_boson2 = secondlepton + fourthlepton
                                    histexact.fill(Z0_boson2.M())
        
            if (lep_charge[0] != lep_charge[3]):
                lep_type = event["lep_type"]
                if (lep_type[0] == lep_type[3]) :
                    lep_pt = event["lep_pt"]
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_E = event["lep_E"]
                    lep_istight = event["lep_isTightID"]
                    lep_ptcone = event["lep_ptcone30"]
                    lep_etcone = event["lep_etcone20"]
                    if np.abs(lep_eta[0])<2.4 and np.abs(lep_eta[3])< 2.4:
                         if (lep_istight[0]) and (lep_istight[3]):
                            if ((lep_ptcone[0] / lep_pt[0] < 0.15) and (lep_etcone[0]/lep_pt[0] < 0.15)) and ((lep_ptcone[3] / lep_pt[3] < 0.15) and (lep_etcone[3]/lep_pt[3] < 0.15)):
                                 if lep_pt[0]/1000. >25 and lep_pt[3]/1000. >20:
                                        
                                    firstlepton.SetPtEtaPhiE(lep_pt[0]/1000,lep_eta[0],lep_phi[0],lep_E[0]/1000)
                                    fourthlepton.SetPtEtaPhiE(lep_pt[3]/1000,lep_eta[3],lep_phi[3],lep_E[3]/1000)
                                    Z0_boson1 = firstlepton + fourthlepton
                                    histexact.fill(Z0_boson1.M())    
            if (lep_charge[1] != lep_charge[2]):
                lep_type = event["lep_type"]
                if (lep_type[1] == lep_type[2]):
                    lep_pt = event["lep_pt"]
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_E = event["lep_E"]
                    lep_istight = event["lep_isTightID"]
                    lep_ptcone = event["lep_ptcone30"]
                    lep_etcone = event["lep_etcone20"]
                    if np.abs(lep_eta[1])<2.4 and np.abs(lep_eta[2])< 2.4:
                         if (lep_istight[2]) and (lep_istight[1]):
                            if ((lep_ptcone[2] / lep_pt[2] < 0.15) and (lep_etcone[2]/lep_pt[2] < 0.15)) and ((lep_ptcone[1] / lep_pt[1] < 0.15) and (lep_etcone[1]/lep_pt[1] < 0.15)):
                                 if lep_pt[1]/1000. >25 and lep_pt[2]/1000. >20:
                                        
                                    secondlepton.SetPtEtaPhiE(lep_pt[1]/1000,lep_eta[1],lep_phi[1],lep_E[1]/1000)
                                    thirdlepton.SetPtEtaPhiE(lep_pt[2]/1000,lep_eta[2],lep_phi[2],lep_E[2]/1000)
                                    Z0_boson2 =  secondlepton + thirdlepton
                                    histexact.fill(Z0_boson2.M())
 
histexact.plot(histtype = "fill")
plt.plot()
plt.show()

filey = [filejeta,filejetb,filejetc,filejetd]
hist1lep1jet = Hist(hist.axis.Regular(50,40,140,label = "Mass(GeV)"))
for tree in filey:
    parameters = tree.arrays(["lep_n","lep_charge","lep_type","lep_eta","lep_phi","lep_pt","lep_E"])
    for event in parameters:
        lep_n = event["lep_n"]
        if lep_n >= 2 and lep_n <= 2:
            lep_charge = event["lep_charge"]
            if lep_charge[0] != lep_charge[1]:
                lep_type = event["lep_type"]
                if lep_type[0] == lep_type[1]:
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_pt = event["lep_pt"]
                    lep_E = event["lep_E"]
                    if np.abs(lep_eta[0])<2.4 and np.abs(lep_eta[1])<2.4:
                        if ((lep_ptcone[0] / lep_pt[0] < 0.15) and (lep_etcone[0]/lep_pt[0] < 0.15)) and ((lep_ptcone[1] / lep_pt[1] < 0.15) and (lep_etcone[1]/lep_pt[1] < 0.15)):
                            if lep_pt[0]/1000. >25 and lep_pt[1]/1000. >20:
                                if (lep_istight[0]) and (lep_istight[1]):
                                    firstlepton.SetPtEtaPhiE(lep_pt[0]/1000.,lep_eta[0],lep_phi[0],lep_E[0]/1000.)
                                    secondlepton.SetPtEtaPhiE(lep_pt[1]/1000.,lep_eta[1],lep_phi[1],lep_E[1]/1000.)
                                    Z0_boson = firstlepton + secondlepton
                                    hist1lep1jet.fill(Z0_boson.M())
        elif lep_n >= 3 and lep_n <= 3:
            lep_charge = event["lep_charge"]
            if lep_charge[0] != lep_charge[1]:
                lep_type = event["lep_type"]
                if lep_type[0] == lep_type[1]:
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_pt = event["lep_pt"]
                    lep_E = event["lep_E"]
                    if np.abs(lep_eta[0])<2.4 and np.abs(lep_eta[1])< 2.4 :
                        if lep_pt[0]/1000. >25 and lep_pt[1]/1000. >20:
                            if (lep_istight[0]) and (lep_istight[1]):
                                if ((lep_ptcone[0] / lep_pt[0] < 0.15) and (lep_etcone[0]/lep_pt[0] < 0.15)) and ((lep_ptcone[1] / lep_pt[1] < 0.15) and (lep_etcone[1]/lep_pt[1] < 0.15)):  
                                    firstlepton.SetPtEtaPhiE(lep_pt[0]/1000.,lep_eta[0],lep_phi[0],lep_E[0]/1000.)
                                    secondlepton.SetPtEtaPhiE(lep_pt[1]/1000.,lep_eta[1],lep_phi[1],lep_E[1]/1000.)
                                    Z0_boson = firstlepton + secondlepton
                                    hist1lep1jet.fill(Z0_boson.M())
            if lep_charge[1] != lep_charge[2]:
                lep_type = event["lep_type"]
                if lep_type[1] == lep_type[2]:
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_pt = event["lep_pt"]
                    lep_E = event["lep_E"]
                    if np.abs(lep_eta[2])<2.4 and np.abs(lep_eta[1])<2.4 :
                        if lep_pt[1]/1000. >25 and lep_pt[2]/1000. >20:
                            if (lep_istight[2]) and (lep_istight[1]):
                                if ((lep_ptcone[2] / lep_pt[2] < 0.15) and (lep_etcone[2]/lep_pt[2] < 0.15)) and ((lep_ptcone[1] / lep_pt[1] < 0.15) and (lep_etcone[1]/lep_pt[1] < 0.15)):
                                    thirdlepton.SetPtEtaPhiE(lep_pt[2]/1000.,lep_eta[2],lep_phi[2],lep_E[2]/1000.)
                                    secondlepton.SetPtEtaPhiE(lep_pt[1]/1000.,lep_eta[1],lep_phi[1],lep_E[1]/1000.)
                                    Z0_boson = thirdlepton + secondlepton
                                    hist1lep1jet.fill(Z0_boson.M())
            if lep_charge[0] != lep_charge[2]:
                lep_type = event["lep_type"]
                if lep_type[0] == lep_type[2]:
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_pt = event["lep_pt"]
                    lep_E = event["lep_E"]
                    if np.abs(lep_eta[0])<2.4 and np.abs(lep_eta[2])< 2.4:
                        if lep_pt[0]/1000. >25 and lep_pt[2]/1000. >20:
                            if (lep_istight[2]) and (lep_istight[0]):
                                if ((lep_ptcone[0] / lep_pt[0] < 0.15) and (lep_etcone[0]/lep_pt[0] < 0.15)) and ((lep_ptcone[2] / lep_pt[2] < 0.15) and (lep_etcone[2]/lep_pt[2] < 0.15)):
                                    firstlepton.SetPtEtaPhiE(lep_pt[0]/1000.,lep_eta[0],lep_phi[0],lep_E[0]/1000.)
                                    thirdlepton.SetPtEtaPhiE(lep_pt[2]/1000.,lep_eta[2],lep_phi[2],lep_E[2]/1000.)
                                    Z0_boson = firstlepton + thirdlepton
                                    hist1lep1jet.fill(Z0_boson.M())

hist1lep1jet.plot(histtype = "fill")
print(hist1lep1jet.values())
plt.plot()
plt.show()

filez = [filetaua,filetaub,filetauc,filetaud]
hist1lep1tau = Hist(hist.axis.Regular(50,40,140,label = "Mass(GeV)"))
for tree in filey:
    parameters = tree.arrays(["lep_n","lep_charge","lep_type","lep_eta","lep_phi","lep_pt","lep_E"])
    for event in parameters:
        lep_n = event["lep_n"]
        if lep_n >= 2 and lep_n <= 2:
            lep_charge = event["lep_charge"]
            if lep_charge[0] != lep_charge[1]:
                lep_type = event["lep_type"]
                if lep_type[0] == lep_type[1]:
                    lep_eta = event["lep_eta"]
                    lep_phi = event["lep_phi"]
                    lep_pt = event["lep_pt"]
                    lep_E = event["lep_E"]
                    if np.abs(lep_eta[0])<2.4 and np.abs(lep_eta[1])<2.4:
                        if lep_pt[0]/1000. >25 and lep_pt[1]/1000. >20:
                            if (lep_istight[0]) and (lep_istight[1]):
                                if ((lep_ptcone[0] / lep_pt[0] < 0.15) and (lep_etcone[0]/lep_pt[0] < 0.15)) and ((lep_ptcone[1] / lep_pt[1] < 0.15) and (lep_etcone[1]/lep_pt[1] < 0.15)):
                                    firstlepton.SetPtEtaPhiE(lep_pt[0]/1000.,lep_eta[0],lep_phi[0],lep_E[0]/1000.)
                                    secondlepton.SetPtEtaPhiE(lep_pt[1]/1000.,lep_eta[1],lep_phi[1],lep_E[1]/1000.)
                                    Z0_boson = firstlepton + secondlepton
                                    hist1lep1tau.fill(Z0_boson.M())
                        

hist1lep1tau.plot(histtype = "fill")
plt.plot()
plt.show()

histgrand = Hist(hist.axis.Regular(50,40,140, label = "Mass(GeV)"))
histgrand = hist1lep1jet + hist1lep1tau + histexact
histgrand.plot(histtype = "fill")
plt.plot()
plt.show()

def breitwigner(E, gamma, M, a, b, A):
    return a*E+b+A*( (2*np.sqrt(2)*M*gamma*np.sqrt(M**2*(M**2+gamma**2)))/(np.pi*np.sqrt(M**2+np.sqrt(M**2*(M**2+gamma**2)))) )/((E**2-M**2)**2+M**2*gamma**2)
print(dir(Hist))

x = histgrand.axes[0].centers
qw= (40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140)
z = np.mat(z)
j=   (493,    631,    623,    716,    924,   1058,   1328,   1371,   1430, 1502,   1581,   1686,   1759,   1905,   2163,   2431,   2823,   3429, 4252,   5674,   8414,  13225,  24111,  47476,  90061, 114657,  75437, 32248,  13674,   7012,   4272,   3057,   2220,   1716,   1492,   12361127,    908,    772,    704,    631,    570,    541,    459,    492,431,    406,    354,   337,   355)
y = histgrand.values()
print(x)
print(y)

initials = [10, 91, -2, 200, 13000]

best, covariance = curve_fit(breitwigner, x, y, p0=initials, sigma=np.sqrt(y))

print(best)
print(covariance)
error = np.sqrt(np.diag(covariance))
print(error)
print("The values and the uncertainties from the optimization")
print("")
first = "The value of the decay width (gamma) = {} +- {}".format(best[0], error[0])
second = "The value of the maximum of the distribution (M) = {} +- {}".format(best[1], error[1])
third = "a = {} +- {}".format(best[2], error[2])
fourth = "b = {} +- {}".format(best[3], error[3])
fifth = "A = {} +- {}".format(best[4], error[4])
print(first)
print(second)
print(third)
print(fourth)
print(fifth)
plt.plot(x, breitwigner(x, *best), 'r-', label='gamma = {}, M = {}'.format(best[0], best[1]))
plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of event')
plt.title('The Breit-Wigner fit')
plt.legend()
plt.show()

