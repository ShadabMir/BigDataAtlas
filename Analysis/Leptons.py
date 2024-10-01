import uproot
import hist
from hist import Hist
import numpy as np
import matplotlib.pyplot as plt
from Helpers.TLorentzVector import TLorentzVector

file2= uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/2lep/Data/data_B.2lep.root:mini")
events2 = file2.arrays(["lep_eta","lep_phi","lep_n","lep_type","lep_charge","lep_pt","lep_E"])
histnew = Hist(hist.axis.Regular(30,40,140,label = "Mass(Gev)"))
histeta = Hist(hist.axis.Regular(70, -3, 3, label = "Pseudorapidity"))
histphi = Hist(hist.axis.Regular(110, -5,5, label = "azimuhal angle"))
histpt = Hist(hist.axis.Regular(100,-0.5,99.5,label = "Transverse momentum"))

firstlepton2 = TLorentzVector()
secondlepton2 = TLorentzVector()
for event in events2:
    lep_n = event["lep_n"]
    if lep_n >= 2:
        
        lep_charge = event["lep_charge"]
        if lep_charge[0]!= lep_charge[1]:
            lep_type = event["lep_type"]
            if lep_type[0] == lep_type[1]:
                lep_eta = event["lep_eta"]
                lep_phi = event["lep_phi"]
                lep_pt = event["lep_pt"]
                lep_E = event["lep_E"]
                firstlepton2.SetPtEtaPhiE(lep_pt[0]/1000.,lep_eta[0],lep_phi[0],lep_E[0]/1000.)
                secondlepton2.SetPtEtaPhiE(lep_pt[1]/1000.,lep_eta[1],lep_phi[1],lep_E[1]/1000.)
                Z0_boson = firstlepton2 + secondlepton2
                histnew.fill(Z0_boson.M())

histnew.plot(histtype = "fill")
plt.plot()
plt.show()


file= uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/2lep/MC/mc_364127.Zee_PTV1000_E_CMS.2lep.root:mini")
events = file.arrays(["lep_eta","lep_phi","lep_n","lep_type","lep_charge","lep_pt","lep_E"])
histnew2 = Hist(hist.axis.Regular(30,70,110,label = "Mass(Gev)"))
firstlepton = TLorentzVector()
secondlepton = TLorentzVector()
for event in events:
    lep_n = event["lep_n"]
    if lep_n >= 2:
        
        lep_charge = event["lep_charge"]
        if lep_charge[0]!= lep_charge[1]:
            lep_type = event["lep_type"]
            if lep_type[0] == lep_type[1]:
                lep_eta = event["lep_eta"]
                lep_phi = event["lep_phi"]
                lep_pt = event["lep_pt"]
                lep_E = event["lep_E"]
                firstlepton.SetPtEtaPhiE(lep_pt[0]/1000.,lep_eta[0],lep_phi[0],lep_E[0]/1000.)
                secondlepton.SetPtEtaPhiE(lep_pt[1]/1000.,lep_eta[1],lep_phi[1],lep_E[1]/1000.)
                Z0_boson = firstlepton + secondlepton
                histnew2.fill(Z0_boson.M())

file2= uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/2lep/Data/data_A.2lep.root:mini")
events2 = file.arrays(["lep_eta","lep_phi","lep_n","lep_type","lep_charge","lep_pt","lep_E"])
histnew = Hist(hist.axis.Regular(30,70,110,label = "Mass(Gev)"))
firstlepton2 = TLorentzVector()
secondlepton2 = TLorentzVector()
for event in events2:
    lep_n = event["lep_n"]
    if lep_n >= 2:
        
        lep_charge = event["lep_charge"]
        if lep_charge[0]!= lep_charge[1]:
            lep_type = event["lep_type"]
            if lep_type[0] == lep_type[1]:
                lep_eta = event["lep_eta"]
                lep_phi = event["lep_phi"]
                lep_pt = event["lep_pt"]
                lep_E = event["lep_E"]
                firstlepton2.SetPtEtaPhiE(lep_pt[0]/1000.,lep_eta[0],lep_phi[0],lep_E[0]/1000.)
                secondlepton2.SetPtEtaPhiE(lep_pt[1]/1000.,lep_eta[1],lep_phi[1],lep_E[1]/1000.)
                Z0_boson = firstlepton2 + secondlepton2
                if Z0_boson.M() < 111 and Z0_boson.M()>69:
                    
                    histnew.fill(Z0_boson.M())

histnew2.plot(histtype = "fill")
histnew.plot()
plt.plot()
plt.show()


file1 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/2lep/Data/data_D.2lep.root:mini")
lep_n1 = file1["lep_n"].array(library = "np")
lep_eta1 = file1["lep_phi"].array(library = "np")
file2 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/2lep/Data/data_C.2lep.root:mini")
lep_n2 = file2["lep_n"].array(library = "np")
lep_eta2 = file2["lep_phi"].array(library = "np")
file3 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/2lep/Data/data_B.2lep.root:mini")
lep_n3 = file3["lep_n"].array(library = "np")
lep_eta3 = file3["lep_phi"].array(library = "np")
file4 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/2lep/Data/data_A.2lep.root:mini")
lep_n4 = file4["lep_n"].array(library = "np")
lep_eta4 = file4["lep_phi"].array(library = "np")
lep_eta = [lep_eta1, lep_eta2,lep_eta3, lep_eta4]
print(len(lep_n1))
print(len(lep_n2))
print(len(lep_n3))
print(len(lep_n4))
print(lep_eta1)
ax = hist.axis.Regular(5, -0.5, 9.5, flow=False, name = "Number of leptons")
ax2 = hist.axis.Regular(50,0,4,flow=False ,name = "PSeudorapidity")

cax = hist.axis.StrCategory(["2lepd", "2lepc", "2lepb","2lepa"], name = "c")
cax2 = hist.axis.StrCategory(["2lepetad","2lepetac","2lepetab","2lepetaa"] , name = "d")
full_hist1 = Hist(ax,cax)
full_hist2 = Hist(ax2,cax2)
full_hist1.fill(lep_n1, c = "2lepd")
full_hist1.fill(lep_n2, c = "2lepc")
full_hist1.fill(lep_n3, c = "2lepb")
full_hist1.fill(lep_n4, c = "2lepa")
for event in lep_eta1:
    if event[0]> 0 and event[0]<4:
        
        full_hist2.fill(lep_eta1[0], d = "2lepetad")
    if event[1]>0 and event[1]<4:
        
        full_hist2.fill(lep_eta1[1], d = "2lepetad")
 
for event in lep_eta2:
    if event[0]> 0 and event[0]<4:         
        full_hist2.fill(lep_eta2[0], d = "2lepetac")
    if event[1]>0 and event[1]<4:
        full_hist2.fill(lep_eta2[1], d = "2lepetac")
 
for event in lep_eta3:
    if event[0]> 0 and event[0]<4:
        full_hist2.fill(lep_eta3[0], d = "2lepetab")
    if event[1]>0 and event[1]<4:
        full_hist2.fill(lep_eta3[1], d = "2lepetab")

for event in lep_eta4:
    if event[0]> 0 and event[0]<4:
        full_hist2.fill(lep_eta4[0], d = "2lepetaa")
    if event[1]>0 and event[1]<4:
        full_hist2.fill(lep_eta4[1], d = "2lepetaa")

    sax = full_hist1.stack("c")
    sax2 = full_hist2.stack("d")
    sax2.plot(histtype = "fill")
    plt.title("Pseudorapidity")
    plt.legend()
    plt.show()
    sax.plot(histtype = "fill")
    plt.title("Number of leptons released in the event file")
    plt.legend()
    plt.show()

file1 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1largeRjet1lep/Data/data_D.1largeRjet1lep.root:mini")
lep_n1 = file1["lep_n"].array(library = "np")
file2 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1largeRjet1lep/Data/data_C.1largeRjet1lep.root:mini")
lep_n2 = file2["lep_n"].array(library = "np")
file3 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1largeRjet1lep/Data/data_B.1largeRjet1lep.root:mini")
lep_n3 = file3["lep_n"].array(library = "np")
file4 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1largeRjet1lep/Data/data_A.1largeRjet1lep.root:mini")
lep_n4 = file4["lep_n"].array(library = "np")

print(len(lep_n1))
print(len(lep_n2))
print(len(lep_n3))
print(len(lep_n4))
ax = hist.axis.Regular(5, -0.5, 4.5, flow=False, name = "Number of leptons")
cax = hist.axis.StrCategory(["1lepjetd", "1lepjetc", "1lepjetb","1lepjeta"], name = "c")
full_hist1 = Hist(ax,cax)
full_hist1.fill(lep_n1, c = "1lepjetd")
full_hist1.fill(lep_n2, c = "1lepjetc")
full_hist1.fill(lep_n3, c = "1lepjetb")
full_hist1.fill(lep_n4, c = "1lepjeta")
sax = full_hist1.stack("c")
sax.plot(stack = True, histtype = "fill")
plt.title("Number of leptons released in the 1 lep 1 jet event file")
plt.legend()
plt.show()

file1 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/3lep/Data/data_D.3lep.root:mini")
lep_n1 = file1["lep_n"].array(library = "np")
file2 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/3lep/Data/data_C.3lep.root:mini")
lep_n2 = file2["lep_n"].array(library = "np")
file3 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/3lep/Data/data_B.3lep.root:mini")
lep_n3 = file3["lep_n"].array(library = "np")
file4 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/3lep/Data/data_A.3lep.root:mini")
lep_n4 = file4["lep_n"].array(library = "np")
print(len(lep_n1))
print(len(lep_n2))
print(len(lep_n3))
print(len(lep_n4))
fileall = [file1,file2,file3,file4]
for tree in fileall:
    parameters = tree.arrays["lep_eta","lep_phi","lep_E","lep_pt","lep_charge","lep_type"]
    for event in parameters:
        lep_eta = event["lep_eta"]
        lep_phi = event["lep_phi"]
        lep_E = event["lep_E"]
        lep_pt = event["lep_pt"]
        for i in range(3):
            histeta.fill(lep_eta[i])
            histphi.fill(lep_phi[i])
            histpt.fill(lep_pt[i])
        next 
    next 
next
#ax = hist.axis.Regular(5, -0.5, 4.5, flow=False, name = "Number of leptons")
#cax = hist.axis.StrCategory(["3lepd", "3lepc", "3lepb","3lepa"], name = "c")
#full_hist1 = Hist(ax,cax)
#full_hist1.fill(lep_n1, c = "3lepd")
#full_hist1.fill(lep_n2, c = "3lepc")
#full_hist1.fill(lep_n3, c = "3lepb")
#full_hist1.fill(lep_n4, c = "3lepa")
#sax = full_hist1.stack("c")
#sax.plot(histtype = "fill")
#plt.title("Number of leptons released in the 3 lep event file")
#plt.legend()
#plt.show()
histeta.plot(histtype = "fill")
plt.title("Number of leptons released in the 1 lep 1 tau event file")
plt.plot()
plt.show()
histphi.plot(histtype = "fill")
plt.plot()
plt.show()
histpt.plot(histtype = "fill")
plt.plot()
plt.show()

file1 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1lep1tau/Data/data_D.1lep1tau.root:mini")
lep_n1 = file1["lep_n"].array(library = "np")
file2 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1lep1tau/Data/data_C.1lep1tau.root:mini")
lep_n2 = file2["lep_n"].array(library = "np")
file3 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1lep1tau/Data/data_B.1lep1tau.root:mini")
lep_n3 = file3["lep_n"].array(library = "np")
file4 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/1lep1tau/Data/data_A.1lep1tau.root:mini")
lep_n4 = file4["lep_n"].array(library = "np")
print(len(lep_n1))
print(len(lep_n2))
print(len(lep_n3))
print(len(lep_n4))
 
#ax = hist.axis.Regular(5, -0.5, 4.5, flow=False, name = "Number of leptons")
#cax = hist.axis.StrCategory(["1leptaud", "1leptauc", "1leptaub","1leptaua"], name = "c")
#full_hist1 = Hist(ax,cax)
#full_hist1.fill(lep_n1, c = "1leptaud")
#full_hist1.fill(lep_n2, c = "1leptauc")
#full_hist1.fill(lep_n3, c = "1leptaub")
#full_hist1.fill(lep_n4, c = "1leptaua")
#sax = full_hist1.stack("c")
#sax.plot(histtype = "fill")
plt.title("Number of leptons released in the 1 lep 1 tau event file")
plt.plot()
plt.show()