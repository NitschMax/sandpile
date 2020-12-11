import numpy as np
import matplotlib.pyplot as plt
import data_dir
import os

def main():
    N           = 100
    directory   = data_dir.get_dir()
    directory   += str('Nk1-{}_Nk2-{}/').format(N, N)
    os.chdir(directory)
    files       = os.listdir(directory)
    print(files)

    var         = np.array([[float(mu[2:]), np.mean(np.load(mu + "/variance.npy" )[-4:])] for mu in files] )
    var         = var[var[:,0].argsort() ]
    print(var)
    plt.plot(var[:, 0], var[:, 1])
    plt.grid(True)
    plt.xlabel("mu")
    plt.ylabel("variance")
    plt.show()
    

if __name__ == "__main__":
    main()
