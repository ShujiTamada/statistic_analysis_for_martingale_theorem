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
    step=0.0005#step_size
    div=term/step#jump_number
    init=np.array([0.])#init_value

    mean=0
    variance=1

    repeat_time=1000


    sdekey={}
    sdekey['default'] = False
    sdekey['init'] = init
    sdekey['stepsize'] = step
    sdekey['term'] = term

    sdekey['matrix'] = np.array([[0.]])
    sdekey['var_matrix'] = np.array([[1.]])
    sdekey['n_mean'] = mean
    sdekey['n_scale'] = variance

    sdekey['observation'] = "qv"
    sdekey['function_select'] = "brown_motion_Doob_mayer"

    figplace = '../figs'#move to fig file
    figname= str('brownian_motion_doob_mayar_%s.png'%sdekey['observation'])
    arrayname= str('brownian_motion_doob_mayar_%s.npy'%sdekey['observation'])
    arraypath = os.path.join(figplace,arrayname)
    figpath = os.path.join(figplace,figname)


    mymodel = sde.SDE_Markov(**sdekey)
    mybmt=bmt(**sdekey)

    #times,trajectory_box,qv=mybmt.brown_motion_square()
    #print(trajectory_box)
    #times,trajectory_box,qv_box=mybmt.brown_motion_square()
    #print(trajectory_box)


    times,trajectory_box=mybmt.simulation(repeat_time)

    #mybmt.saveFigure(figpath,repeat_time)
    np.save(arraypath,trajectory_box)
    mybmt.saveResult(figpath, times, trajectory_box)


    numpath,numstep = trajectory_box.shape
    lastval= trajectory_box[:,numstep-1]#terminal value
    meanval =  np.mean(lastval)#mean of terminal value
    varval  = np.var(lastval)#var of terminal value

    print('over %spaths, mean at time%s is %s. var is %s'%(numpath,term, meanval, varval))

    #simulate.saveFig(brownian_motion_sq,repeat_time)
    #np.save(brownian_motion_sq,trajectory)








if __name__ == '__main__':
    main()
