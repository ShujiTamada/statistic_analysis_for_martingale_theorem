#make a random walk
import numpy as np
import sys
sys.path.append("../src")#road a file

import random_walk as rd
from random_walk import random_walk as rdw
import importlib #function to reroad a file

from matplotlib import pyplot as plt

import math
from scipy.stats import norm
import argparse
import pdb
import os

def main():
    term=10#terminal_time
    init=np.array([0.,0.])#init_value
    jump_size=1
    prob=0.5
    repeat_time=5

    sdekey={}
    sdekey['init'] = init
    sdekey['term'] = term
    sdekey['jump_size'] = jump_size
    sdekey['prob'] = prob
    sdekey['repeat_time'] = repeat_time
    sdekey['model']='rw_malti_dim'

    figplace = '../fig/thm5.1.1'#move to fig file
    figname= str('random_walk_%s.png'%sdekey['model'])
    figpath= os.path.join(figplace,figname)



    rd_walk = rd.random_walk(**sdekey)
    rd_walk.simulation_multi_dim()


    #path=rd_walk.random_walk_dim()
    #print(path)



if __name__ == '__main__':

#pdb.set_trace()
    main()
