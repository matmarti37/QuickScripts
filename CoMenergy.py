import numpy as np
import sys

beams = ["18O"]

if(len(sys.argv)==4):
        beam = sys.argv[1]
        Elab = float(sys.argv[2])
        target = sys.argv[3]
elif(len(sys.argv)==1):
        Elab = 48.0
        Abeam = 18
        Zbeam = 8
        target = input("Target material (e.g. H or Au): ")
else:
        print("Failed. Use\n")
        print("python3 CoMenergy.py BEAM(18O) ENERGY(MeV) TARGET(Au)\n")
        exit(-1)

if beam == "18O":
        Zbeam = 8
        Abeam = 18
'''
Elab = 48.0

Abeam   = 18
Zbeam   = 8
'''
targets = ["H","C","Cu","Sn","Ag","Au","Ta"]
#target = input("Please enter the chemical symbol of the target: ")

if target == "H":
	Ztarget = 1
	Atarget = 1

if target == "C":
	Ztarget = 6
	Atarget = 12

if target == "Cu":
	Ztarget = 29
	Atarget = 64
	
if target == "Sn":
	Ztarget = 50
	Atarget = 119

if target == "Ag":
	Ztarget = 47
	Atarget = 108

if target == "Au":
	Ztarget = 97
	Atarget = 197

if target == "Ta":
        Ztarget = 73
        Atarget = 118


# Converts Elab [MeV] to Elab [GeV]
Elab = Elab/1000

# Entire equation in GeV
ECM = np.sqrt(Abeam**2 + Atarget**2 + 2*(Elab+Abeam)*Atarget) - (Abeam + Atarget)
ECM = ECM * 1000 # Converts back to MeV

# ECoul manual
r0 = 1.2
#ECoul = 1.44 * (Zbeam * Ztarget) / (r0*Abeam**(1/3) + r0*Atarget**(1/3) + 5)
ECoul = 1.44 * (Zbeam * Ztarget) / 6.3


#ECM = ECM/1000
#Etest = (1/(2*Atarget)) * ((ECoul+Abeam+Atarget)**2 - (Abeam+Atarget)**2)
#print(Etest*1000)

# Output
print("For beam of \n A = "+ str(Abeam) + "; Z = "+ str(Zbeam) + "\n with energy \n E = " + str(1000*Elab) + " MeV")
print("For target of \n A = "+ str(Atarget) + "; Z = "+ str(Ztarget) + "\n")
print("Centre of Mass \n Ecm = " + str(ECM) + " MeV \n")
print("Coulomb Barrier \n ECoul = " + str(ECoul) + " MeV \n")
