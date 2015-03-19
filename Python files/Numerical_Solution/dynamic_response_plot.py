import matplotlib.pyplot as plt

def plot_shortPeriod(t,y1,u1,y2,u2,y3,u3,y4,u4):
    plt.figure(1)
    plt.subplot(411)
    plt.plot(t,y1,t,u1)
    plt.xlabel('t')
    plt.ylabel('V')

    plt.subplot(412)
    plt.plot(t,y2,t,u2)
    plt.xlabel('t')
    plt.ylabel(r'$\alpha$')

    plt.subplot(413)
    plt.plot(t,y3,t,u3)
    plt.xlabel('t')
    plt.ylabel(r'$\theta$')

    plt.subplot(414)
    plt.plot(t,y4,t,u4)
    plt.xlabel('t')
    plt.ylabel('q')

    plt.show()




def plot_phugoid():
    plt.figure(1)
    plt.subplot(411)
    plt.plot(t[0],y[0])
    plt.xlabel('t')
    plt.ylabel('u')

    plt.subplot(412)
    plt.plot(t[1],y[1])
    plt.xlabel('t')
    plt.ylabel(r'$\alpha$')

    plt.subplot(413)
    plt.plot(t[2],y[2])
    plt.xlabel('t')
    plt.ylabel(r'$\theta$')

    plt.subplot(414)
    plt.plot(t[3],y[3])
    plt.xlabel('t')
    plt.ylabel('q')
    plt.show()

def plot_aperiodicRoll():
    plt.figure(1)
    plt.subplot(411)
    plt.plot(t[0],y[0])
    plt.xlabel('t')
    plt.ylabel(r'$\beta$')

    plt.subplot(412)
    plt.plot(t[1],y[1])
    plt.xlabel('t')
    plt.ylabel(r'$\varphi$')

    plt.subplot(413)
    plt.plot(t[2],y[2])
    plt.xlabel('t')
    plt.ylabel('p')

    plt.subplot(414)
    plt.plot(t[3],y[3])
    plt.xlabel('t')
    plt.ylabel('r')
    plt.show()

def plot_dutchRoll():
    plt.figure(1)
    plt.subplot(411)
    plt.plot(t[0],y[0])
    plt.xlabel('t')
    plt.ylabel(r'$\beta$')

    plt.subplot(412)
    plt.plot(t[1],y[1])
    plt.xlabel('t')
    plt.ylabel(r'$\varphi$')

    plt.subplot(413)
    plt.plot(t[2],y[2])
    plt.xlabel('t')
    plt.ylabel('p')

    plt.subplot(414)
    plt.plot(t[3],y[3])
    plt.xlabel('t')
    plt.ylabel('r')
    plt.show()

def plot_aperiodicSpiral():
    plt.figure(1)
    plt.subplot(411)
    plt.plot(t[0],y[0])
    plt.xlabel('t')
    plt.ylabel(r'$\beta$')

    plt.subplot(412)
    plt.plot(t[1],y[1])
    plt.xlabel('t')
    plt.ylabel(r'$\varphi$')

    plt.subplot(413)
    plt.plot(t[2],y[2])
    plt.xlabel('t')
    plt.ylabel('p')

    plt.subplot(414)
    plt.plot(t[3],y[3])
    plt.xlabel('t')
    plt.ylabel('r')
    plt.show()