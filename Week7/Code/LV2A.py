#! usr/bin/python2
""" Author - Oliver Tarrant
 The typical Lotka-Volterra Model simulated using scipy """

import scipy as sc 
import scipy.integrate as integrate
import pylab as p #Contains matplotlib for plotting
import sys

# import matplotlip.pylab as p #Some people might need to do this

def dR_dt(pops, t=0):
    """ Returns the growth rate of predator and prey populations at any 
    given time step """
    
    R = pops[0]
    C = pops[1]
    dRdt = r*R*(1 - (R/K)) - a*C*R
    dydt = -z*C + e*a*R*C
    
    return sc.array([dRdt, dydt])

# Define parameters:
r = 1. # Resource growth rate
a = 0.1 # Consumer search rate (determines consumption rate) 
z = 1.5 # Consumer mortality rate
e = 0.75 # Consumer production efficiency

# Now define time -- integrate from 0 to 15, using 1000 points:
t = sc.linspace(0, 100,  50000)
K = 100
x0 = 10
y0 = 5 
z0 = sc.array([x0, y0]) # initials conditions: 10 prey and 5 predators per unit area

pops, infodict = integrate.odeint(dR_dt, z0, t, full_output=True) #runs dR_dt as an integration with i.c z0 and over time interval t
									# infodict just checks integration was successful
infodict['message']     # >>> 'Integration successful.'

prey, predators = pops.T # Transposes to form correct format 
final_prey = prey[-1]
final_predator = predators[-1]
f1 = p.figure() #Open empty figure object
p.plot(t, prey, 'g-', label='Resource density') # Plot
p.plot(t, predators  , 'b-', label='Consumer density')
p.annotate( 'Constants: r = %r , a = %r , z = %r , e = %r , K = %r' %(r,a,z,e,K), xy=(20,5), color = "red") 
p.annotate('Final prey = %.5s , Final predators = %.5s' %(final_prey,final_predator), xy=(25,2), color = "purple")
p.grid()
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population')
p.title('Consumer-Resource population dynamics')
p.show()
f1.savefig('../Results/prey_and_predators_2A.pdf') #Save figure
