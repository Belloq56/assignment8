import numpy as np
from matplotlib import pyplot as pp

def f(P,m,v,C,rho,A,):
    return (P/v - (0.5*C*rho*A*v**2))/m

def f1(P,m,v,C,rho,A,eta,h):
    return (P/v - (0.5*C*rho*A*v**2)-eta*A*(v/h))/m

def f2(P,m,v,C,rho,A,eta,h,g,theta):
    return (P/v - (0.5*C*rho*A*v**2)-eta*A*(v/h)-(m*g*np.sin(theta)))/m

def euler(P,m,v,h,C,rho,A):
    return v + f(P,m,v,C,rho,A)*h

def euler1(P,m,v,h,C,rho,A,eta,height):
    return v + f1(P,m,v,C,rho,A,eta,height)*h

def euler2(P,m,v,h,C,rho,A,eta,height,g,theta):
    return v + f2(P,m,v,C,rho,A,eta,height,g,theta)*h

C=0.9
rho=1.1889
A=0.33
eta=2e-5
h=2
g=9.81
grade=10
theta=np.arctan(grade/100)
P=400
m=70
start=0
step=0.1
final=200
v=[4]
v1=[4]
v2=[4]
x=np.arange(start,final+step,step)


for i in range(len(x)-1):
    v.append(euler(P,m,v[-1],step,C,rho,A))
    v1.append(euler1(P,m,v1[-1],step,C,rho,A,eta,h))
    v2.append(euler2(P,m,v2[-1],step,C,rho,A,eta,h,g,theta))


pp.plot(x,v)
pp.plot(x,v1,"--")
pp.plot(x,v2)
pp.xlabel('time (s)')
pp.ylabel('velocity (m/s)')
pp.show()
#pp.savefig('bicycle.png')

