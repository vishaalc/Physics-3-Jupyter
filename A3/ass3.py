from __future__ import division
import math

# r vector
# r magnitude
# r unit vector
# E(n)


def rod(n):

    piece = 1 / n

    Q = piece * (10**-6)
    K = 9.0 * (10**9)

    E_calc = [0, 0, 0]

    for i in range(1, n + 1):

        ry = 0.5 - ((2*i) - 1) * (piece/2)
        r = [0.1, ry, 0.0]
        #r = [0,0.6,0]
        #r = [0.1, 0.5, 0]

        x = r[0]
        y = r[1]
        z = r[2]

        r_mag = math.sqrt(x**2 + y**2 + z**2)
        r_unit = [x/r_mag, y/r_mag, z/r_mag]

        E = (K*Q)/r_mag**2
        E_net = [E*r_unit[0], E*r_unit[1], E*r_unit[2]]

        E_calc[0] += E_net[0]
        E_calc[1] += E_net[1]
        E_calc[2] += E_net[2]

    return E_calc;


def main():
    print rod(6)


main()




