import subprocess
import os
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math

P_0 = 101325.
a = -0.0065
R = 287.
p_0 = 1.225
T_0 = 288.
g_0 = 9.80665
gamma = 1.4
W_OEW = 60500.
W_p = (82+96+98.5+82+79+77.5+83.5+92.5+83.5+77)
S = 30.
CmTc = -0.0064
b = 15.911
A = b*b/S
c = 2.0569

font = {'weight' : 'bold',
        'size'   : 28}

matplotlib.rc('font', **font)


datas = open('FTISxprt-20150305_144557_2.txt')
data = datas.readlines()

outs = []
for line in data:
    line = line.strip('\n').split('\t')
    
    #Find h_p
    h_p = float(line[17])

    #Find V
    V = float(line[19])
    
    #Find T_m
    T_m = float(line[18])+273.15

    #Find weights
    W_f = 2423*0.45359237 - (float(line[5]) + float(line[6]))
    #Need h_p, V, T_m, W_OEW, W_f, W_p
    
    #find P
    P = P_0*(1+a*h_p/T_0)**(-g_0/(a*R))
    
    #Find M
    M = sqrt(2./(gamma-1)*((1+P_0/P*((1+(gamma-1)/(2*gamma)*p_0/P_0*V*V)**(gamma/(gamma-1))-1))**((gamma-1)/gamma)-1))

    #Find T
    T = T_m/(1+(gamma-1)/2*M*M)

    #Find p (rho)
    p = P/(R*T)

    #Find V_t
    V_t = V*sqrt(p_0/p)

    #Reduce Weight
    W_s = W_OEW/g_0
    W = W_OEW/g_0 + W_f + W_p

    #Reduce Airspeed
    V_e = V*sqrt(W_s/W)

    #Standard fuel flows
    FFL = round(float(line[3]),4)
    FFR = round(float(line[4]),4)


    #catches
    h_p = round(h_p,0)
    M = round(M,2)
    if M == 0:
        M = 0.01
    T = round(T,0)
    if h_p == 0:
        h_p = 1.0
    
    #save to list
    outs.append([int(h_p),M,T,FFL,FFR,V_e,V_t,p])

#----------------------------------------------------Thrustdata is got------------------------------------------------------------------

#Get reduced thrust
thrust = open('thrusst.txt','w')
for i in [10000,11000,12100,13100,14200,15800,18500,21650,22200,23400,24200,24850,25600,26600,28100]:
    thrust.write(str(outs[i][0])+'\t'+str(outs[i][1])+'\t'+str(abs(outs[i][2]-T_0))+'\t'+str(outs[i][3])+'\t'+str(outs[i][4])+'\n')
    thrust.write(str(outs[i][0])+'\t'+str(outs[i][1])+'\t'+str(abs(outs[i][2]-T_0))+'\t'+str(0.048)+'\t'+str(0.048)+'\n')
thrust.close()

process = subprocess.Popen(['thrust.exe','thrusst.txt'], bufsize = -1 ,stderr = subprocess.PIPE, stdin=subprocess.PIPE, stdout = subprocess.PIPE)
process.wait()
thrust = open('thrust.dat','r')

Tlist = []
Tlists = []
thrustd = thrust.readlines()
i = 0
for line in thrustd:
    line = line.strip('\n').split('\t')
    if i%2 == 0:
        Tlist.append(float(line[0])+float(line[1]))
    else:
        Tlists.append(float(line[0])+float(line[1]))
    i+=1
thrust.close()
os.remove('thrusst.txt')
#os.remove('thrust.dat')

#------------------------------------------------------Thrust is got--------------------------------------------------------------------
#ninth = range(27953,28287)
#Calculate xcg for measurement 9
plane = [82,96,82,79,77.5,83.5,92.5,83.5,98.5,77]
M_a = [131,131,214,214,251,251,288,288,170,170]
for i in range(len(M_a)):
    M_a[i] = 0.0254*M_a[i]
mom = 0
mom_af = 4572*.01152
M_p = (262+81*.25)*0.0254

i = 0
for fag in plane:
    mom += fag*M_a[i]
    i+=1

mom += M_p*W_OEW/g_0 + mom_af
xcg_9 = mom/(W_OEW/g_0+1700*0.453592+sum(plane))

plane = [82,96,82,79,77.5,83.5,92.5,83.5,98.5,77]
M_a = [131,131,214,214,251,251,288,288,135,170]
for i in range(len(M_a)):
    M_a[i] = 0.0254*M_a[i]
mom = 0
mom_af = 4856*.01152
M_p = (262+81*.25)*0.0254

i = 0
for fag in plane:
    mom += fag*M_a[i]
    i+=1

mom += M_p*W_OEW/g_0 + mom_af
xcg_8 = mom/(W_OEW/g_0+1600*0.453592+sum(plane))

dxcg = abs(xcg_8-xcg_9)

de_8 = -0.02 #rad
de_9 = -0.03 #rad

dde = abs(de_8-de_9)

Cmde = -(1./dde)*(W_OEW+W_p*g_0+(2423-780)*0.4536)/(0.5*S*0.94325*158*158*0.51444*0.514444)*dxcg/2.0569
#------------------------------------------------------Cmde is got----------------------------------------------------------------------

#Reduced elevator deflection
i = 0
j = 6
velist = []
ddeslist = []
alphalist = []
elevlist = []
feslist = []
Wflist = []
Mlist = []
Relist = []
for line in data:
    if i in [18500,21650,22200,23400,24200,24850,25600]:  #2nd measurement
#    if i in [10000,11000,12100,13100,14200,15800]:     #1st measurement
        line = line.strip('\n').split('\t')
        h_p = outs[i][0]
        M = outs[i][1]
        T = outs[i][2]
        V_e = outs[i][5]
        Thr = Tlist[j]/(0.5*1.225*V_e*V_e*S)  
        Thrs = Tlists[j]/(0.5*1.225*V_e*V_e*S)
        de = float(line[9])
        W_f = 2423*0.45359237 - (float(line[5]) + float(line[6]))
        Fe = float(line[2])
        Fes = Fe*W_OEW/(W_OEW+W_p*g_0+W_f*g_0)
        M = outs[i][1]
        V_t = outs[i][6]
        mu = (1.458*10e-6 * np.sqrt(T))/(1+ 110.4/T)
        rho = outs[i][7]
        Re = rho*V_t*c/mu
        #print h_p
        
        ddes = de-CmTc*(Thrs-Thr)/Cmde
        
        velist.append(V_e)
        ddeslist.append(ddes)
        alphalist.append(float(line[0]))
        elevlist.append(de)
        feslist.append(Fes)
        Wflist.append(W_f)
        Mlist.append(M)
        Relist.append(Re)

        j+=1
    i+=1
elevalpha = np.polyfit(alphalist,elevlist,1)
relevrve = np.polyfit(velist,ddeslist,2)
velev = np.poly1d(relevrve)

rfeve = np.polyfit(velist,feslist,2)
rfeve = np.poly1d(rfeve)

x = np.linspace(55,90,100)

Cma = -elevalpha[0]*Cmde


print 'Cma=',Cma
print 'Cmde=', Cmde
plt.figure()
plt.scatter(velist,ddeslist)
plt.plot(x,velev(x),label='2nd order ploynomial fit')
plt.legend()
plt.xlabel('$\~V_e$ (m/s)')
plt.ylabel('$\delta_e^*$ (rad)')
plt.gca().invert_yaxis()
plt.title('Reduced Elevator Trim Curve')
plt.show()


plt.figure()
plt.scatter(velist,feslist)
plt.plot(x,rfeve(x),label='2nd order ploynomial fit')
plt.legend(loc=4)
plt.xlabel('$\~V_e$ (m/s)')
plt.ylabel('$F_e^*$ (N)')
plt.title('Reduced Stick Force Curve')
plt.show()

#Outputs here are:
#Cma
#Cmde
#reduced control force-V curve
#reduced de-V curve

'''
plt.scatter(alphalist,elevlist, label='1st order ploynomial fit')
plt.legend()
plt.xlabel('$\alpha$ (rad)')
plt.ylabel('$\delta_e^*$ (rad)')
plt.title('Reduced Elevator Deflection Polar - Alpha Curve')
plt.show()
'''

#--------------------------------------------outputs done------------------------------
CDlist = []
CLlist = []
CL2list = []

Velist = []
for i in range(len(velist)):
    #Velist.append(velist[i]*(Wflist[i]*g_0+W_p*g_0+W_OEW)/W_OEW)
    Velist.append(velist[i])

for i in range(7):
    T = Tlist[i]
    CDlist.append(T/(0.5*1.225*Velist[i]*Velist[i]*S))
    CL = (W_OEW/(0.5*1.225*Velist[i]*Velist[i]*S))
    CLlist.append(CL)
    CL2list.append(CL*CL)  
cl2cd = np.polyfit(CDlist,CL2list,1)
cl2cd = np.poly1d(cl2cd)

cdcl2 = np.polyfit(CL2list,CDlist,1)
cdcl2 = np.poly1d(cdcl2)

cla = np.polyfit(alphalist,CLlist,1)
cla = np.poly1d(cla)
acl = np.polyfit(CLlist,alphalist,1)
acl = np.poly1d(acl)

clcd = np.polyfit(CDlist,CLlist,2)
clcd = np.poly1d(clcd)

cda = np.polyfit(alphalist,CDlist,2)
cda = np.poly1d(cda)

x = np.linspace(0.025,0.075,100)
x1 = np.linspace(0.02,0.19,100)

CD0 = cdcl2(0)
grad = cdcl2[1]
e = 1./(grad*A*np.pi)
CLa = cla[1]
CL0 = acl(0)

print 'CD0 =', CD0
print 'e=', e
print 'CLa=', CLa
print 'CL0=', CL0
plt.figure()
plt.scatter(alphalist,CDlist)
plt.xlabel(r'$\alpha$ (rad)')
plt.ylabel('$C_D$')
plt.title('Drag polar')
plt.plot(x1,cda(x1),label='2nd order polynomial fit')
plt.legend(loc=4)
plt.show()

plt.figure()
plt.scatter(CDlist,CLlist)
plt.xlabel('$C_D$')
plt.ylabel('$C_L$')
plt.title('Lift-drag polar')
plt.plot(x,clcd(x),label='2nd order polynomial fit')
plt.legend(loc=4)
plt.show()

plt.figure()
plt.scatter(alphalist,CLlist)
plt.xlabel(r"$\alpha$ (rad)")
plt.ylabel('$C_L$')
plt.title('Lift slope')
plt.plot(x1,cla(x1),label='1st order polynomial fit')
plt.legend(loc=4)
plt.show()

plt.figure()
plt.scatter(CDlist,CL2list)
plt.xlabel('$C_D$')
plt.ylabel('$C_L^2$')
plt.title('$C_L^2$ vs $C_D$')
plt.plot(x,cl2cd(x),label='1st order ploynomial fit')
plt.legend(loc=4)
plt.show()
