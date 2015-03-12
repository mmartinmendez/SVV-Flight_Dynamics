#International Standard Atmopshere calculations
#==============================================

from math import*
from Cit_par import*

def aparameters(h1):

    """

    :rtype : integer
    """

    #sea level conditions
    p0 = 101325.0

    #11000m conditions
    T11000 = 216.65
    p11000 = 22614.2066867
    rho11000 = 0.363630885894
    h11000 = 11000.



    if h1>0. and h1<=11000.:

        T1 = Temp0 + lam*(h1-hp0)
        p1 = p0*((T1/Temp0)**(-g/(lam*R)))
        rho1 = rho0*((T1/Temp0)**((-g/(lam*R))-1))


    elif h1>11000. and h1<=20000.:

        T1 = T11000
        p1 = p11000*exp((-g/(R*T11000))*(h1-h11000))
        rho1 = rho11000*exp((-g/(R*T11000))*(h1-h11000))

    else:
        print "Invalid altitude"
        T1=0
        p1=0
        rho1=0

    return T1,p1,rho1

def

