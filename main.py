from sandpile import grid

def main():
    N       = 100
    crit    = .70
    lattice = grid(crit, N, N)
    lattice.fill_random_checker()
    lattice.fill_random()
    lattice.plot()
    for k in range(500):
        lattice.time_step_mat()
    lattice.plot()


if __name__ == "__main__":
    main()
