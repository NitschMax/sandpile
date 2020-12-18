from sandpile import grid
import numpy as np
import time

def main():
    N       = 200
    n       = 1000
    mu      = 0.7
    geom    = "hex"

    lattice = grid(mu, N, N, geom)
    #lattice.test_run()
    lattice.fill_random()
    lattice.run(n)
    lattice.save()
    lattice.load()
    lattice.plot()

    #lattice.fill_random()
    #lattice.animation(n)

    for mu in np.arange(0.01, 2.001, .01):
        print(mu)
        lattice = grid(mu, N, N, 'hex')
        lattice.fill_random()
        lattice.run(n)
        lattice.save()
 
if __name__ == "__main__":
    main()
