import uproot
import hist
from hist import Hist
from TLorentzVector import TLorentzVector
import numpy as np
import matplotlib.pyplot as plt

def fit_function(x, a, b, c,):
    background = (a * x) +  (b * x * x) + (c * x * x * x)
    return (background)

def locateGoodPhotons(dat):
  
    
    ## Checking the event passes the photon trigger
    #trigP = tree["trigP"]
    trigP = dat["trigP"]
    if trigP == True:
        
        # Initialise (set up) the variables we want to return
        goodphoton_index = [] #Indices (position in list of event's photons) of our good photons
            
        ## Loop through all the photons in the event
        photon_n = dat["photon_n"]
        for j in range(0,photon_n):
            
            ## Check photon ID
            photon_isTight = dat["photon_isTightID"][j]
            if(photon_isTight):
                photon_pt = dat["photon_pt"][j]
                # Check photon has a large enough pT
                if (j==0 and photon_pt > 35000) or (j==1 and photon_pt > 25000):
                    photon_eta = dat["photon_eta"][j]
                    # Check photon eta is in the 'central' region
                    if (abs(photon_eta) < 2.37):
                  
                      # Exclude "transition region" between ID barrell and ECal endcap
                      if (abs(photon_eta) < 1.37 or abs(photon_eta) > 1.52):

                        goodphoton_index.append(j) # Store photon's index
                    
        return goodphoton_index # Return list of good photon indices
    
def photonIsolation(dat,photon_indices):
    """
    Function which returns True if all photons are well-isolated, otherwise returns false.
    
    A photon is considered 'isolated' if the transverse momentum and transverse energy in the detector, within 
    a particular radius around the photon (variables called 'ptcone30' and 'etcone20'), is below a certain threshold compared to the photon's 
    transverse momentum (don't worry too much about the details!).
    
    Parameters
    ----------
    dat : array from TTree for this event
    
    photon_indices : List containing the indices in the TTree of our photons of interest
    
    """
    
    # Loop through our list of photon indices
    for i in photon_indices:
        photon_ptcone30 = dat["photon_ptcone30"][i]
        photon_pt = dat["photon_pt"][i]
        photon_etcone20 = dat["photon_etcone20"][i]
        
        # If each photon passes isolation requirements...
        if((photon_ptcone30 / photon_pt < 0.065) and 
           (photon_etcone20 / photon_pt < 0.065)):
            continue #...keep the loop going 
        
        # If any fail, break the loop and return False
        else: 
            return False
    
    # If the loop is able to finish, i.e. all photons are well-isolated, return True
    return True


def photonFourMomentum(dat, photon_indices):
    
    
    photon_four_momenta = []
    
    # Loop through our list of photon indices
    for i in photon_indices:
    
        # Initialse (set up) an empty 4 vector for each photon
        Photon_i = TLorentzVector()
    
        photon_pt = dat["photon_pt"][i]
        photon_eta = dat["photon_eta"][i]
        photon_phi = dat["photon_phi"][i]
        photon_E = dat["photon_E"][i]
        # Retrieve the photon's 4 momentum components from the tree
        # Convert from MeV to GeV where needed by dividing by 1000
        Photon_i.SetPtEtaPhiE(photon_pt/1000., photon_eta, photon_phi, photon_E/1000.)
        
        # Store photon's 4 momentum
        photon_four_momenta.append(Photon_i)
        
        
    return photon_four_momenta


def sumFourMomentum(four_momenta):
    
    
    # Initialise (set up) TLorentzVector for our momentum sum
    four_mom_sum = TLorentzVector()
    
    for obj in four_momenta:
        four_mom_sum += obj
        
    return four_mom_sum

if __name__ == "main":
    file1 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/GamGam/Data/data_A.GamGam.root:mini")
    file2 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/GamGam/Data/data_B.GamGam.root:mini")
    file3 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/GamGam/Data/data_C.GamGam.root:mini")
    file4 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/GamGam/Data/data_D.GamGam.root:mini")
    histnew = Hist(hist.axis.Regular(30,105,160,label = "Mass invariant"))
    fileall = [file1,file2,file3]
    for tree in fileall:
        sel_events = tree.arrays(["photon_ptcone30","photon_etcone20","photon_isTightID","photon_eta","photon_phi","photon_n","photon_E","photon_pt","trigP"])
        for event in sel_events:
            goodphotonarray = locateGoodPhotons(event)
            if len(goodphotonarray) == 2:
                goodisolationphotons = photonIsolation(event,goodphotonarray)
                if goodisolationphotons:
                    photonmomarray = photonFourMomentum(event, goodphotonarray)
                    sumofphotonmomentum = sumFourMomentum(photonmomarray)
                    invmasshiggs = sumofphotonmomentum.M()
                    photon_pt = event["photon_pt"]
                    if (photon_pt[0]/invmasshiggs) > 0.35 and (photon_pt[1]/invmasshiggs) > 0.25:
                        histnew.fill(invmasshiggs)
                    
    histnew.plot()
    plt.plot()
    plt.show()
    hist2 = Hist(hist.axis.Regular(30,105,160, label = "Mass invariant"))
    file4 = uproot.open("https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/GamGam/Data/data_D.GamGam.root:mini")
    
    sel_events = file4.arrays(["photon_ptcone30","photon_etcone20","photon_isTightID","photon_eta","photon_phi","photon_n","photon_E","photon_pt","trigP"])
    n = 0
    for event in sel_events:
        n += 1
        if n < 2000000:
            goodphotonarray = locateGoodPhotons(event)
            if len(goodphotonarray) == 2:
                goodisolationphotons = photonIsolation(event,goodphotonarray)
                if goodisolationphotons:
                    photonmomarray = photonFourMomentum(event, goodphotonarray)
                    sumofphotonmomentum = sumFourMomentum(photonmomarray)
                    invmasshiggs = sumofphotonmomentum.M()
                    photon_pt = event["photon_pt"]
                    if (photon_pt[0]/invmasshiggs) > 0.35 and (photon_pt[1]/invmasshiggs) > 0.25:
                        if invmasshiggs< 161 and invmasshiggs > 104:
                            hist2.fill(invmasshiggs)
        else:
            break 
                                 
    hist2.plot()
    plt.plot()
    plt.show()