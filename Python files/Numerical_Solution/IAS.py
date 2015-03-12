#International Standard Atmopshere calculations
#==============================================

from math import*

def aparameters(h1):

    """

    :rtype : integer
    """
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



    if h1>0. and h1<=11000.:

        T1 = T0 + a*(h1-h0)
        p1 = p0*((T1/T0)**(-g/(a*R)))
        rho1 = rho0*((T1/T0)**((-g/(a*R))-1))


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

