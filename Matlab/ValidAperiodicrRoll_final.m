clc
clear all
syms data
data = load('FTISxprt-20150305_144557');
begin = 29124;
ending = 29500;
UTC = data.flightdata.Gps_utcSec.data;

TAS = 0.514444444 * data.flightdata.Dadc1_tas.data;
beta = data.flightdata.Ahrs1_Pitch.data;
phi = data.flightdata.Ahrs1_Roll.data;
p = data.flightdata.Ahrs1_bRollRate.data;
r = data.flightdata.Ahrs1_bYawRate.data;


%-------------------------------------------------------------------------%
%%%%%%%%%%%%%%%%%%%%%%%% Change these parameters! %%%%%%%%%%%%%%%%%%%%%%%%%
%-------------------------------------------------------------------------%
FusedL = 183.1762766;  % Parameter F in Excel - Midsection of motion!
FusedR = 202.4232494;  % Parameter G in Excel - Midsection of motion!

alpha0 = 0.076822267;  % Parameter A in Excel - Startsection of motion!
th0    = 0.055971485;  % Parameter M in Excel - Startsection of motion!
hp0    = 2178.103142;  % Parameter R in Excel - Startsection of motion!
V0     = 84.80083235;  % Parameter T in Excel - Startsection of motion!
%-------------------------------------------------------------------------%
%%%%%%%%%%%%%%%%%%%%%%%% End of changing variables %%%%%%%%%%%%%%%%%%%%%%%%
%-------------------------------------------------------------------------%
m0     = 9170/0.224808943/9.81;
mf     = 2423*0.45359237;
mp     = 851.5;
Fused  = FusedL + FusedR;
m      = m0 + mf + mp - Fused;

e      =  0.598607792739;%0.963751922274;        %----------------------------------------%
CD0    =  0.0268891723086;%0.0242883628867;       % These parameters may still change due  %
CLa    =  4.40100457224;%5.37484226789;         % to incomplete work by Twan and Juan.   %
Cma    = -0.561377830286;%-0.732594717104;        % Final values are therefore temporary   %
Cmde   = -0.825489971065;%-0.934024280588;        %----------------------------------------%

S      = 30.00;
Sh     = 0.2*S;
Sh_S   = Sh/S;
lh     = 0.71*5.968;
c      = 2.0569;
lh_c   = lh/c;
b      = 15.911;
bh     = 5.791;
A      = b^2/S;
Ah     = bh^2/Sh;
Vh_V   = 1;
ih     = -2*pi/180;

rho0   = 1.2250;
lam    = -0.0065;
Temp0  = 288.15;
R      = 287.05;
g      = 9.81;

rho    = rho0*((1+(lam*hp0/Temp0)))^(-((g/(lam*R))+1));
W      = m*g;

muc    = m/(rho*S*c);
mub    = m/(rho*S*b);
KX2    = 0.019;
KZ2    = 0.042;
KXZ    = 0.002;
KY2    = 1.25*1.114;

Cmac   = 0;
CNwa   = CLa;
CNha   = 2*pi*Ah/(Ah+2);
depsda = 4/(A+2);

CL     = 2*W/(rho*V0^2*S);
CD     = CD0 + (CLa*alpha0)^2/(pi*A*e);

CX0    = W*sin(th0)/(0.5*rho*V0^2*S);
CXu    = -0.02792;
CXa    = -0.47966;
CXadot = +0.08330;
CXq    = -0.28170;
CXde   = -0.03728;

CZ0    = -W*cos(th0)/(0.5*rho*V0^2*S);
CZu    = -0.37616;
CZa    = -5.74340;
CZadot = -0.00350;
CZq    = -5.66290;
CZde   = -0.69612;

Cmu    = +0.06990;
Cmadot = +0.17800;
Cmq    = -8.79415;

CYb    = -0.7500;
CYbdot =  0     ;
CYp    = -0.0304;
CYr    = +0.8495;
CYda   = -0.0400;
CYdr   = +0.2300;

Clb    = -0.10260;
Clp    = -0.71085;
Clr    = +0.23760;
Clda   = -0.23088;
Cldr   = +0.03440;

Cnb    = +0.1348;
Cnbdot =  0     ;
Cnp    = -0.0602;
Cnr    = -0.2061;
Cnda   = -0.0120;
Cndr   = -0.0939;

C1 = b/TAS(begin)*[-2*mub, 0 , 0 , 0; 
      0, -0.5, 0, 0;
      0, 0, -4*mub*KX2*b/2/TAS(begin), 4*mub*KXZ*b/2/TAS(begin);
      0, 0, 4*mub*KXZ*b/2/TAS(begin), -4*mub*KZ2*b/2/TAS(begin)];
  
C2 = [-CYb, -CL, -CYp*b/2/TAS(begin), -(CYr-4*mub)*b/2/TAS(begin);
      0, 0, -b/2/TAS(begin), 0; 
      -Clb, 0, -Clp*b/2/TAS(begin), -Clr*b/2/TAS(begin);
      -Cnb, 0, -Cnp*b/2/TAS(begin), -Cnr*b/2/TAS(begin)];
  
C3 = [-CYda, -CYdr;
      0,0 ;
      -Clda, -Cldr;
      -Cnda, -Cndr];

A = inv(C1)*C2;
B = inv(C1)*C3;
C      =  eye(4);
D = zeros(4,2);
u1           = data.flightdata.delta_a.data(begin:ending);
u2           = data.flightdata.delta_r.data(begin:ending);
u = horzcat(u1,u2);
t           = data.flightdata.Gps_utcSec.data(begin:ending)-ones(size(ending-begin))*data.flightdata.Gps_utcSec.data(begin);
figure(3)
plot(t,u)
sys         = ss(A, B, C, D);
SP          = lsim(sys, u, t);

figure(2)
subplot(4,1,1)
plot(UTC(begin:ending)-UTC(begin), beta(begin:ending))
hold on
plot(t,SP(:,1)+beta(begin),'r')
xlabel('Time [s]')
ylabel('beta [deg]')
title('Aperiodic Roll')
subplot(4,1,2)
plot(UTC(begin:ending)-UTC(begin), phi(begin:ending))
hold on
plot(t,SP(:,2)+phi(begin),'r')
xlabel('Time [s]')
ylabel('phi [deg]')
subplot(4,1,3)
plot(UTC(begin:ending)-UTC(begin), p(begin:ending))
hold on
plot(t,SP(:,3)+p(begin),'r')
xlabel('Time [s]')
ylabel('p [deg/s]')
subplot(4,1,4)
plot(UTC(begin:ending)-UTC(begin), r(begin:ending))
hold on
plot(t,SP(:,4)+r(begin),'r')
xlabel('Time [s]')
ylabel('r [deg/s]')