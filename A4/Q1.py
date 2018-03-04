'''
Calculating components of the electric field at each point on the grid,
depends on axis orientation as well as position of the particle.
Where E is according to the formula given and letting t = theta for example...
Q1: Ex = Ecost (+), Ey = Esint (+)
Q2: Ex = Ecost (-), Ey = Esint (+)
Q3: Ex = Esint (-), Ey = Ecost (-)
Q4: Ex = Esint (+), Ey = Ecostt(-)
'''

import math
q = 1.0 * 10**-9
k = 9.0 * 10**9

x = 1
y = 1

r2 = [x,y] #x, y position
r1 = [0,0]
r =  [r2[0]-r1[0], r2[1]-r1[1]]
mag = math.fabs(r[0]**2 + r[1]**2)
E = k(q(r2-r1))/mag**3

