import matplotlib.pyplot as plt


alpha = [0,1,2,3,4,5,6,7,8]
C_L = alpha/10
CL_alpha(C_L,alpha)

def CL_alpha(C_L,alpha):
    plt.plot(C_L,alpha)
    plt.axis([-5, 20, -0.2, 2])
    plt.title(r'$\alpha$')
    plt.show