import matplotlib.pyplot as plt
from Cit_par import *

def plot_shortPeriod(t,y1,u1,y2,u2,y3,u3,y4,u4):
    plt.figure(1)
    plt.subplot(411)
    plt.plot(t,y1+V0,t,u1)
    plt.xlabel('t')
    plt.ylabel('u')

    plt.subplot(412)
    plt.plot(t,y2+alpha0,t,u2)
    plt.xlabel('t')
    plt.ylabel(r'$\alpha$')

    plt.subplot(413)
    plt.plot(t,y3+th0,t,u3)
    plt.xlabel('t')
    plt.ylabel(r'$\theta$')

    plt.subplot(414)
    plt.plot(t,y4+q0,t,u4)
    plt.xlabel('t')
    plt.ylabel('q')

    plt.show()

def plot_phugoid(t,y1,u1,y2,u2,y3,u3,y4,u4):
    plt.figure(1)
    plt.subplot(411)
    plt.plot(t,y1+V0,t,u1)
    plt.xlabel('t')
    plt.ylabel('u')

    plt.subplot(412)
    plt.plot(t,y2+alpha0,t,u2)
    plt.xlabel('t')
    plt.ylabel(r'$\alpha$')

    plt.subplot(413)
    plt.plot(t,y3+th0,t,u3)
    plt.xlabel('t')
    plt.ylabel(r'$\theta$')

    plt.subplot(414)
    plt.plot(t,y4+q0,t,u4)
    plt.xlabel('t')
    plt.ylabel('q')

    plt.show()

def plot_aperiodicRoll(t,y1,u1,y2,u2,y3,u3,y4,u4):
    plt.figure(1)
    plt.subplot(411)
    plt.plot(t,y1+V0,t,u1)
    plt.xlabel('t')
    plt.ylabel(r'$\beta$')

    plt.subplot(412)
    plt.plot(t,y2+alpha0,t,u2)
    plt.xlabel('t')
    plt.ylabel(r'$\varphi')

    plt.subplot(413)
    plt.plot(t,y3+th0,t,u3)
    plt.xlabel('t')
    plt.ylabel('p')

    plt.subplot(414)
    plt.plot(t,y4+q0,t,u4)
    plt.xlabel('t')
    plt.ylabel('r')

    plt.show()

def plot_dutchRoll(t,y1,u1,y2,u2,y3,u3,y4,u4):
    plt.figure(1)
    plt.subplot(411)
    plt.plot(t,y1+V0,t,u1)
    plt.xlabel('t')
    plt.ylabel(r'$\beta$')

    plt.subplot(412)
    plt.plot(t,y2+alpha0,t,u2)
    plt.xlabel('t')
    plt.ylabel(r'$\varphi')

    plt.subplot(413)
    plt.plot(t,y3+th0,t,u3)
    plt.xlabel('t')
    plt.ylabel('p')

    plt.subplot(414)
    plt.plot(t,y4+q0,t,u4)
    plt.xlabel('t')
    plt.ylabel('r')

    plt.show()

def plot_aperiodicSpiral(t,y1,u1,y2,u2,y3,u3,y4,u4):
    plt.figure(1)
    plt.subplot(411)
    plt.plot(t,y1+V0,t,u1)
    plt.xlabel('t')
    plt.ylabel(r'$\beta$')

    plt.subplot(412)
    plt.plot(t,y2+alpha0,t,u2)
    plt.xlabel('t')
    plt.ylabel(r'$\varphi')

    plt.subplot(413)
    plt.plot(t,y3+th0,t,u3)
    plt.xlabel('t')
    plt.ylabel('p')

    plt.subplot(414)
    plt.plot(t,y4+q0,t,u4)
    plt.xlabel('t')
    plt.ylabel('r')

    plt.show()





