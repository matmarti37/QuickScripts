import numpy as np
import sys

def getDensities(element):
	eleFile = open("elements.txt","r+")
	eleData = eleFile.readlines()
	for line in eleData:
		if(line[0]=="\n" or line[0]=="#" or line[0]==" "):
			continue
		line=line.replace("\n","").replace("\t"," ")
		line=line.split(" ")
		for spot in line:
			if(spot==""):
				line.remove("")
		if(line[0]==element):
			return(line[0],line[1])
	print("Failed to properly read the densities file")
	exit(-1)

rho = 0
if(len(sys.argv)==2):
	param_file = open(sys.argv[1],"r")
	param_data = param_file.readlines()
	for line in param_data:
		if(line[0]=="#" or line[0]=="\n" or line[0]==" "):
			continue
		line = line.replace("\n","")
		line = line.replace("\t"," ")
		line = line.split(" ")
		for element in line:
			if(element == ""):
				line.remove("")
		if(line[0] == "A"):
			A = float(line[1])
		elif(line[0] == "B"):
			B = float(line[1])
		elif(line[0] == "C"):
			C = float(line[1])
		elif(line[0] == "D"):
			D = float(line[1])
		elif(line[0] == "E"):
			E = float(line[1])
		elif(line[0] == "M"):
			M = float(line[1])
		elif(line[0] == "ELE"):
			element = getDensities(line[1])
			ELE = element[0]
			rho = float(element[1])
	print("A = " + str(A) + " mm")
	print("B = " + str(B) + " mm")
	print("C = " + str(C) + " mm")
	print("D = " + str(D) + " mm")
	print("E = " + str(E) + " mm")
	print("M = " + str(M) + "  g")

else:
	# Takes input values in mm
	A = float(input("Enter A Parameter in mm: "))
	B = float(input("Enter B Parameter in mm: "))
	C = float(input("Enter C Parameter in mm: "))
	D = float(input("Enter D Parameter in mm: "))
	E = float(input("Enter E Parameter in mm: "))
	M = float(input("Enter M Parameter in g:  "))


# Converts all lengths to cm
A = A/10
B = B/10
C = C/10
D = D/10
E = E/10
# Converts mass to mg
M = M*1000

# Calculates the area of the quadrilateral
term1 = np.sqrt(A**2 * B**2 - 0.25*(A**2 + B**2 - E**2)**2)
term2 = np.sqrt(C**2 * D**2 - 0.25*(C**2 + D**2 - E**2)**2)
area = 0.5*(term1+term2)

# Prints the area for reference
print("The area of the quadrilateral is " + str(round(area,2)) + " cm^2")

# Calculates the foil thickness in mg/cm^2
thick = M / area

# Prints the thickness in ug/cm^2
print("The thickness of the foil is: " + str(round(thick,2)) + " mg/cm^2")

# If element given, thickness in microns
if(rho!=0):
	thickness = 10 * thick / rho
	print("The thickness of the " + str(ELE) + " foil is: " + str(round(thickness,2)) + " um")




