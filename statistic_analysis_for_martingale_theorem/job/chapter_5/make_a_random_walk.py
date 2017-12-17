
#This file simulates making other files

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
    term=50 #terminal_time
    init=np.array([0.]) #init_value
    jump_size=1
    #step size(jump_size=1 if simulate model is discreate model.)
    prob=0.5 #trancelate probability
    repeat_time=500 #number of path

    sdekey={}
    sdekey['init'] = init
    sdekey['term'] = term
    sdekey['jump_size'] = jump_size
    sdekey['prob'] = prob
    sdekey['repeat_time'] = repeat_time
    sdekey['model']='standard'
    sdekey['value']='qv'

    figplace = '../fig/verfication'#move to fig file
    pathname= str('rw_%s_path.png'%sdekey['model'])
    histname= str('rw_%s_hist.png'%sdekey['model'])
    fighist= os.path.join(figplace,histname)
    figpath= os.path.join(figplace,pathname)


    rd_walk = rd.random_walk(**sdekey)
    rd_walk.plot_glaph(figpath,fighist)

    #os.system('say "うんこぉぉぉぉぉぉぉぉぉぉぉ"')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='runnning parameters')
    parser.add_argument('--repeat_time', '-n', type=int, default =1,  help='number of trajectories')
    args= parser.parse_args()
    #pdb.set_trace()
    main()
    #main(args)
