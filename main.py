from sandpile import grid
import numpy as np
import time

def main():
    N       = 100
    n       = 100
    mu      = 0.7

    lattice = grid(mu, N, N)
    #lattice.test_run()
    lattice.fill_random()
    lattice.run(n)
    lattice.plot()
    lattice.fill_random()
    lattice.animation(n)

#    for mu in np.arange(4., 5.0001, .01):
#        print(mu)
#        lattice = grid(mu, N, N)
#        lattice.fill_random()
#        lattice.run(n)
#        lattice.save()
 
if __name__ == "__main__":
    main()
