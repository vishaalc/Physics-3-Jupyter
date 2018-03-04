import numpy as np


'''
	Unless your instructor provides you with other values, assume each voltage source and each resistor has a value 10× its identifying number. 
	(i.e. V2=20 V, R3=30Ω.)
'''

''' 
EXERCISE 1

1. On paper
2.

'''

R1, R2, R3 = 10, 20, 30
V1, V2 = 10, 20

M = np.array([[R1, 0, R3], [0, -R2, R3], [1, -1, -1]])
b = np.array([V1, V2, 0])

x = np.linalg.solve(M, b)

print x

'''
3. Substituting currents back into the system of equations in 1, we can verify that they are the solutions

'''


'''

EXERCISE 2

1. On paper
2. On paper
3.

'''

R1, R2, R3, R4, R5, R6 = 10, 20, 30, 40, 50, 60
V1, V2, V3, V4 = 10, 20, 30, 40

M = np.array([
				[R1, 0, R3, 0, 0, 0],
				[0, 0, 0, -R4, 0, 0],
				[0, -R2, R3, R4, 0, -R6],
				[0, -R2, R3, 0, 0, 0],
				[1, -1, -1, 0, 0, 0],
				[0, 0, 0, 0, -R5, 0]
			])

b = np.array([
				V1,
				V4,
				V3,
				V2,
				0,
				V4
			])

I = np.linalg.solve(M, b)
print I

'''
4. Yes, the values of currents found solve the system of equations with which we started (2)
5. Both solutions for the exercises have the same values for I1, I2, I3. This is because the circuit shown in Exercise 2
   actually contains the sub-loop of the same circuit for Exercise 1 from the upper left. As per the assumption stated,
   the same values of R and V were also used in both exercises.

'''

