def getrho(h):
    #h must be lower than 11km and in meters
    T0 = 293.
    a = -0.0065
    rho0 = 1.225
    g0 = 9.80665
    R = 287.
    
    T = T0 + a*h
    rho = rho0*(T/T0)**(-g0/(a*R)-1)
    return rho  #kg/m3
