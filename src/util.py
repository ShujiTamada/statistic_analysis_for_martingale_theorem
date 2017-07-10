import numpy as np
import SDE_class as sde
from matplotlib import pyplot as plt
import sys
import os
import pdb

figpath = "../figs"
datpath = "../data"

def simulate(filename):
    mymodel = sde.SDE_Markov(mymat=np.array([[0.5]]), \
    myvar =np.array([[1.]]),myinit=np.array([1.]),myscale=1.)

    #Trajectory must also return time for the real implementation
    trajectory = mymodel.trajectory(now_position=np.array([0]))

    #YOU MUST CHANGE THIS!!!
    times = np.array(range(len(trajectory[0])))
    #pdb.set_trace()

    plt.plot(times, trajectory[0])
    filepath= os.path.join(figpath, filename)
    datFilepath= os.path.join(datpath, filename)
    plt.savefig(filepath)
    np.save(datFilepath,trajectory)
