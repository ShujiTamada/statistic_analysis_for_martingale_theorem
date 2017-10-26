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
    term=100#terminal_time
    init=np.array([0.])#init_value
    jump_size=1
    prob=0.5
    repeat_time=10000

    sdekey={}
    sdekey['init'] = init
    sdekey['term'] = term
    sdekey['jump_size'] = jump_size
    sdekey['prob'] = prob
    sdekey['repeat_time'] = repeat_time
    sdekey['model']='sq_qv'

    figplace = '../fig/thm5.1.1'#move to fig file
    pathname= str('random_walk_path_%s.png'%sdekey['model'])
    histname= str('random_walk_hist_%s.png'%sdekey['model'])
    fighist= os.path.join(figplace,histname)
    figpath= os.path.join(figplace,pathname)


    rd_walk = rd.random_walk(**sdekey)
    #rd_walk.plot_glaph(figpath)
    rd_walk.plot_hist(fighist)

    #trajectory=rd_walk.integral_discrete()
    #print(trajectory)



if __name__ == '__main__':
    main()
