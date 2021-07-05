import math as m
import sys
from decimal import Decimal

ln2 = m.log(2)
Na = 6.022e23

class Element:
    def __init__(self,name,T,dT,f,df,M,dM,p,dp):
        self.name = name #Name of element, i.e. Pt190
        self.T = T #Halflife in s
        self.dT = dT
        self.f = f #Natural abundance as a decimal (10% = 0.1)
        self.df = df
        self.M = M #Molar mass in g/mol
        self.dM = dM
        self.p = p #Density in g/cm3
        self.dp = dp

Pt190 = Element("Pt190",2.05e19,1e18,0.00012,0.00002,195.08,0,21.45,0)


ele = {"Pt190": Pt190}


arguments = sys.argv[1:]
if len(arguments) != 2 and len(arguments) != 5:
    print("Run program with:")
    print("python ActivityCalculator.py element thickness")
    print("or")
    print("python ActivityCalculator.py element thickness area dt da")
    quit()

case = arguments[0]
t = float(arguments[1])
dt = float(0)
a = float(1)
da = float(0)
if len(arguments) == 5:
    a = arguments[2]
    dt = arguments[3]
    da = arguments[4]
t = t * 1e-4



activity = a*t* (ln2/ele[case].T)*ele[case].f*(Na/ele[case].M)*ele[case].p
uncertainty = activity * m.sqrt((ele[case].dT/ele[case].T)**2 + (ele[case].dM/ele[case].M)**2 + (ele[case].df/ele[case].f)**2 + (da/a)**2 + (dt/t)**2 + (ele[case].dp/ele[case].p)**2)

act = '%.3E' % Decimal(activity)
unc = '%.3E' % Decimal(uncertainty)

print("Activity is "+str(act)+" +/- "+str(unc)+" decays per second")
