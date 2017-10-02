#練習
import sys
sys.path.append("../src")#road a file
sys.path.append("../data")#road a file
sys.path.append("../fig")#road a file
import SDE_class as sde
from brown_motion import brown_motion as bmt
import importlib #function to reroad a file
import numpy as np
from matplotlib import pyplot as plt
import util as util
import math
from scipy.stats import norm
import argparse
import pdb
import os

def main():

    #SDE_Markov variation_number
    term=1#terminal_time
    step=0.001#step_size
    div=term/step#jump_number
    init=np.array([0.])#init_value

    mean=0
    variance=1

    repeat_time=3


    sdekey={}
    sdekey['default'] = True
    sdekey['init'] = init
    sdekey['stepsize'] = step
    sdekey['term'] = term

    sdekey['mat'] = np.array([[1.]])
    sdekey['var_matrix'] = np.array([[1.]])
    sdekey['n_mean'] = mean
    sdekey['n_scale'] = variance

    figplace = '../figs'#move to fig file
    figname= str('brownian_motion_nomnal.png')
    arrayname= str('brownian_motion_nomnal.npy')
    arraypath = os.path.join(figplace,arrayname)
    figpath = os.path.join(figplace,figname)


    mymodel = sde.SDE_Markov(**sdekey)
    simulate=bmt(**sdekey)

    times,trajectory,qv=simulate.brown_motion_nomal()
    '''
    all_trajectory=np.zeros([repeat_time,div+1])
    for k in range(repeat_time):
        simulate.brown_motion_nomal()
        times,trajectry_box,qv_box=simulate.brown_motion_nomal()
        all_trajectory[k,:]=trajectry_box
    print(all_trajectory)
    '''
    times,trajectry_box,qv_box=simulate.brown_motion_nomal()


    simulate.saveFigure(figpath,repeat_time)

    np.save(arraypath,trajectory)


    #plt.plot(times, trajectory[0])
    #filepath= os.path.join(figpath, filename)
    #datFilepath= os.path.join(datpath, filename)
    #plt.savefig(filepath)





if __name__ == '__main__':
    main()
