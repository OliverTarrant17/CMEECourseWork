#! usr/bin/python2
"""Author - Oliver Tarrant  
A discrete time version Lotka-Volterra Model simulated using scipy """

import scipy as sc 
import scipy.integrate as integrate
import pylab as p #Contains matplotlib for plotting
import sys


# import matplotlip.pylab as p #Some people might need to do this

def dR_dt(x,y, t=0):
    """ Returns the growth rate of predator and prey populations at any 
    given time step """
    # the model
    R = x
    C = y
    dR = (r*R*(1-(R/K))-a*C*R)
    dC = (-z*C + e*a*R*C)
    
    return sc.array([[dR, dC ]])

if len(sys.argv) >= 5: # Allows uses to input arguments else uses defaults
	r = float(sys.argv[1])
	a = float(sys.argv[2])
	z = float(sys.argv[3])
	e = float(sys.argv[4])
elif len(sys.argv) == 4:
	r = float(sys.argv[1])
	a = float(sys.argv[2])
	z = float(sys.argv[3])
	e = 0.75
elif len(sys.argv) == 3:	
	r = float(sys.argv[1])
	a = float(sys.argv[2])
	z = 1.5
	e = 0.75
elif len(sys.argv) == 2:	
	r = float(sys.argv[1])
	a = 0.1
	z = 1.5
	e = 0.75
else:
# Define parameters:
	r = 1. # Resource growth rate
	a = 0.1 # Consumer search rate (determines consumption rate) 
	z = 1.5 # Consumer mortality rate
	e = 0.75 # Consumer production efficiency

# Now define time -- integrate from 0 to 15, using 1000 points:
t = sc.linspace(0, 10,  10)
K = 250
x0 = 100
y0 = 5
z0 = sc.array([x0, y0]) # initials conditions: 10 prey and 5 predators per unit area
pops = sc.array([[x0,y0]])
x = z0[0]
y = z0[1]
n= len(t) # get length of t
### Get time step size
t_step = t[1]-t[0]

for i in t[1:n]: # initial conditions already included in pops
	
	new = dR_dt(x,y,i) # 2*1 array
	if new[0,0] < 0: # doesn't allow density to drop below 0
		new[0,0] = 0
	if new[0,1] < 0:
		new[0,1] = 0
	pops = sc.concatenate((pops,new),axis=0) 
	x = round(new[0,0],10)  # rounds values so doesn't exceed memory
	y = round(new[0,1],10)



prey, predators = pops.T # Transposes to form correct format 
print(pops.T)

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
f1.savefig('../prey_and_predators_3.pdf') #Save figure
