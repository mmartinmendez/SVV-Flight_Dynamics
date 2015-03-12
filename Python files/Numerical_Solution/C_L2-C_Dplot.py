import matplotlib.pyplot as plt

def C_L2vsC_Dplot(C_L,C_D):
    plt.plot(C_L**2,CD)
    plt.axis([-5, 20, -0.2, 2])
    plt.xlabel(r'${C_L}^2')
    plt.ylabel(r'$C_D$')
    plt.title(r"${C_L}^2 \  -\ C_D$")
    plt.show()

    pos=0
    for i in range(C_L):
        if C_L[i]==0:
            pos=i
            break

        elif C_L>0:
            pos=i
            C_D0=interpolate(C_L,C_D,pos)

    e=(C_L[2]-C_L[1])/(C_D[2]-C_D[1])
    return C_D0,e