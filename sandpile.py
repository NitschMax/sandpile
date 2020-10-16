import numpy as np
import matplotlib.pyplot as plt

from scipy.sparse import identity

class grid:
    def greet(self):
        print("Hello World, I am a grid of heigth " + str(self.h) + " and length " + str(self.l) + "!" )
        print(self.o)

    def fill_random(self):
        self.o      = np.random.rand(self.h, self.l)

    def fill_checkerboard(self):
        self.o      = np.indices((self.h, self.l) ).sum(axis=0) % 2 

    def fill_random_checker(self):
        self.o      = (np.indices((self.h, self.l) ).sum(axis=0) % 2)*(1-.1*np.random.rand(self.h, self.l) )

    def modify(self, i, j, value):
        if (i >= self.h) or (i < 0) or (j >= self.l) or (j < 0):
            print("This modification is not possible.")
        if not (isinstance(i, int) and isinstance(j, int) ):
            print("This modification is not possible.")
        else:
            self.o[i, j]    = value

    def plot(self):
        fig, ax     = plt.subplots(1,1)
        c           = ax.pcolor(self.o, cmap='RdBu', vmin=0)
        fig.colorbar(c, ax=ax)
        fig.tight_layout()
        plt.show()

    def time_step(self):
        overspill   = np.transpose(np.where(self.o > self.x) )
        update      = np.identity(self.h*self.l)
        vector      = self.o.flatten()

        for example in overspill:
            j           = example[0]
            l           = example[1]
            neighbors   = [j*self.l+np.mod(l-1, self.l), j*self.l+np.mod(l+1, self.l), np.mod(j-1, self.h)*self.l+l, np.mod(j+1, self.h)*self.l+l ]
            index                           = j*self.l+l
            spill                           = np.zeros((self.h*self.l, self.h*self.l) )
            spill[index, index]             = -1
            spill[neighbors[0], index]      = 1/4
            spill[neighbors[1], index]      = 1/4
            spill[neighbors[2], index]      = 1/4
            spill[neighbors[3], index]      = 1/4
            update                          += spill

        vector                          = np.matmul(update, vector)
        self.o                          = vector.reshape(self.h, self.l)

    def time_step_mat(self):
        candidates  = np.transpose(np.where(self.o > self.x) )
        vector      = self.o.flatten()

        steps       = np.array([[-1, 0], [1, 0], [0, -1], [0, 1] ] )
        vec_index   = np.transpose(np.array([self.l, 1]) )

        indices     = np.matmul(candidates, vec_index)
        neighbors   = np.array([np.matmul(np.mod(el + steps, self.l), vec_index) for el in  candidates] ) #.reshape((-1, 2) 
        indices     = indices.reshape((indices.size, 1))

        spill                       = np.identity(self.a )
        spill[neighbors, indices]   = 1/4
        spill[indices, indices]     = 0

        vector                      = np.matmul(spill, vector)
        self.o                      = vector.reshape(self.h, self.l)


    def __init__(self, crittical_value, heigth, length):
        self.x      = crittical_value               #critcal value
        self.h      = heigth                        #heigth of the grid
        self.l      = length                        #length of the grid
        self.a      = self.h*self.l                 #area of the grid
        self.o      = np.zeros((self.h, self.l) )   #occupations, to get non-zero ocupations use the fill_* fuctions

    
