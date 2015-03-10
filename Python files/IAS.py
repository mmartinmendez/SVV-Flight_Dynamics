#International Standard Atmopshere calculations
#==============================================

#import math
from math import*

def IAS():

    #constants
    g = 9.81
    R = 287.0

    #sea level conditions
    T0 = 288.15
    p0 = 101325.0
    rho0 = 1.225
    h0 = 0.
    #11000m conditions
    T11000 = 216.65
    p11000 = 22614.2066867
    rho11000 = 0.363630885894
    h11000 = 11000.

    #gradient
    a = -0.0065

    h1=1000

#-------calculations for altitude = 0 - 11000m---------
    if h1>0. and h1<=11000.:
    
        #TEMPERATURE
        T1 = T0 + a*(h1-h0)
        print "Temperature =",T1, "K"
        #PRESSURE
        p1 = p0*((T1/T0)**(-g/(a*R)))
        print "Pressure =", p1, "Pa"
        #DENSITY
        rho1 = rho0*((T1/T0)**((-g/(a*R))-1))
        print "Density =", rho1, "kg/m^3"

#-------calculations foraltitude = 11000 - 20000m------
    elseif h1>11000. and h1<=20000.:

        #TEMPERATURE
        T1 = T11000
        print "Temperature =",T1, "K"
        #PRESSURE
        p1 = p11000*exp((-g/(R*T11000))*(h1-h11000))
        print "Pressure =", p1, "Pa"
        #DENSITY
        rho1 = rho11000*exp((-g/(R*T11000))*(h1-h11000))
        print "Density =", rho1, "kg/m^3"

    else:
        print "Invalid altitude"


    return T1,p1,rho1

