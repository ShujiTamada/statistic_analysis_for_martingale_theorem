# simulation thm 5.1.1

#make a random walk
import numpy as np
import sys
sys.path.append("../src")#road a file

import random_walk as rd
#from random_walk import random_walk as rdw
import importlib #function to reroad a file

from matplotlib import pyplot as plt

import math
from scipy.stats import norm
import argparse
import pdb
import os

def main():
    term=10#terminal_time
    init=np.array([0.])#init_value
    jump_size=2
    prob=0.5
    repeat_time=20

    sdekey={}
    sdekey['init'] = init
    sdekey['term'] = term
    sdekey['jump_size'] = jump_size
    sdekey['prob'] = prob
    sdekey['repeat_time'] = repeat_time
    sdekey['model']='integral_discrete'

    figplace = '../fig/thm5.1.1'#move to fig file
    figname= str('random_walk_%s.png'%sdekey['model'])
    figpath= os.path.join(figplace,figname)



    rd_walk = rd.random_walk(**sdekey)
    path=rd_walk.plot_glaph(figpath)

    #trajectory=rd_walk.integral_discrete()
    #print(trajectory)



if __name__ == '__main__':
    main()
