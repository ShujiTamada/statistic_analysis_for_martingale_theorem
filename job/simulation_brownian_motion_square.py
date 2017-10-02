#練習
import sys
sys.path.append("../src")#road a file
sys.path.append("../data")#road a file
sys.path.append("../fig")#road a file
import SDE_class as sde
import brown_motion_tranceform as bmt
import importlib #function to reroad a file
importlib.reload(sde)
importlib.reload(bmt)
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
    init=np.array([2.])#init_value

    mean=0
    variance=1

    repeat_time=3

    print('UNKO')

    sdekey={}
    sdekey['default'] = False
    sdekey['init'] = init
    sdekey['stepsize'] = step
    sdekey['term'] = term

    sdekey['mat'] = np.array([[0.]])
    sdekey['var_matrix'] = np.array([[1.]])
    sdekey['n_mean'] = mean
    sdekey['n_scale'] = variance

    figplace = '../figs'#move to fig file
    filename= str('brownian_motion_sq')
    brownian_motion_sq = os.path.join(figplace,filename)


    mymodel = sde.SDE_Markov(**sdekey)
    simulate=bmt.brown_motion(**sdekey)


    times,trajectry_box,qv_box=simulate.brown_motion_square()
    times=times[0]
    trajectry_box=trajectry_box[0]
    qv_box=qv_box[0]

    print(trajectry_box)
    print(times)
    print(qv_box)

    plt.plot(times,qv_box)


    #simulate.saveFig(brownian_motion_sq,repeat_time)
    #np.save(brownian_motion_sq,trajectory)








if __name__ == '__main__':
    main()
