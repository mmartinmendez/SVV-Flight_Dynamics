__author__ = 'myth'


from Cit_par import*

def points(value,m):
    start = 29987
    r = 413
    Time = zeros(r)
    Input1 = zeros(r)
    Input2 = zeros(r)
    for i in range(r):
        Time[i] = value[start+i][23]
    start = 29987
    for j in range(r):
        Input1[j] = value[start+j][9]
    if m==19:
        start = 29987
        for j in range(r):
            rho = rho0*((1+(lam*value[start][17]/Temp0)))**(-((g/(lam*R))+1))
            Input2[j] = value[start+j][m]*sqrt(rho0/rho)
    else:
        start = 29987
        for j in range(r):
            Input2[j] = value[start+j][m]
    return Time,Input1,Input2