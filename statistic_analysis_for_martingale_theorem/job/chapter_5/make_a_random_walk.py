
#This file simulates making other files
"""
import numpy as np
import sys
sys.path.append("../../src")#road a file

import random_walk as rd
from random_walk import random_walk as rdw
import importlib #function to reroad a file

from matplotlib import pyplot as plt

import math
from scipy.stats import norm
import argparse
import pdb
import os
"""
import numpy as np
import sys
sys.path.append("../../src")#road a file

import random_walk as rd
import importlib #function to reroad a file
from matplotlib import pyplot as plt

import math
from scipy.stats import norm
import argparse
import pdb
import os
import timeit


def main():

    init=np.array([0.]) #init_value

    sdekey={}
    sdekey['init'] = init
    sdekey['term'] = args.terminal
    sdekey['jump_size'] = args.jump
    sdekey['prob'] = args.prob
    sdekey['repeat_time'] = args.repeat_time
    sdekey['model']=args.model
    sdekey['value']=args.value

    figplace = '../../fig/verfication'#move to fig file
    pathname= str('%s_rw_path.png'%sdekey['model'])
    histname= str('%s_rw_hist.png'%sdekey['model'])
    fighist= os.path.join(figplace,histname)
    figpath= os.path.join(figplace,pathname)


    rd_walk = rd.random_walk(**sdekey)
    rd_walk.plot_glaph(figpath,fighist)

    #os.system('say "うんこぉぉぉぉぉぉぉぉぉぉぉ"')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='runnning parameters')
    parser.add_argument('--terminal', '-t', type=int, default =100,  help='terminal time')
    parser.add_argument('--jump', '-j', type=int, default =1,  help='jump size')
    parser.add_argument('--prob', '-p', type=int, default =0.5,  help='jump size')
    parser.add_argument('--repeat_time', '-r', type=int, default =5000,  help='number of trajectories')
    parser.add_argument('--model', '-m', type=str, default ='standard',  help='mode of the random walk')
    parser.add_argument('--value', '-v', type=str, default ='path',  help='value of the random walk')
    args= parser.parse_args()
    main()
