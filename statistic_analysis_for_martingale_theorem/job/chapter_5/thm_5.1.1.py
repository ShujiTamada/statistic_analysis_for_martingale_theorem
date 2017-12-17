
'''
simulation thorem 5.1.1
'''

import numpy as np
import sys
sys.path.append("../../src")#road a file

import random_walk as rd
#from random_walk import random_walk as rdw
import importlib #function to reroad a file

from matplotlib import pyplot as plt

import math
from scipy.stats import norm
import argparse
import pdb
import os
import timeit

def main(args):
    term=100#terminal_time
    init=np.array([0.])#init_value
    jump_size=1
    prob=0.5
    repeat_time=args.repeat_time

    sdekey={}
    sdekey['init'] = init #init place
    sdekey['term'] = args.terminal #terminal times
    sdekey['jump_size'] = jump_size #jump size value
    sdekey['prob'] = prob #translate probability
    sdekey['repeat_time'] = repeat_time #number of path
    #sdekey['model']=args.mode #selection path model
    sdekey['model']='square_minus_qv'
    sdekey['value']='path' #section path value

    figplace = '../../fig/thm5.1.1' #move to fig file
    pathname= str('%s_rw_path_.png'%sdekey['model']) #picture name of path of thorem 5.1.1
    pathfilename= str('%s_rw_path.npy'%sdekey['model'])

    histname= str('%s_rw_hist.png'%sdekey['model'])
    fighist= os.path.join(figplace,histname)
    figpath= os.path.join(figplace,pathname)
    filepath = os.path.join(figplace,pathfilename)

    rd_walk = rd.random_walk(**sdekey)
    rd_walk.plot_glaph(figpath,fighist)


if __name__ == '__main__':
    '''
    how to use argparse
    1. write "argparse.ArgumentParser(description='runnning parameters')"
    2. add parameter
       for example  "parser.add_argument('--repeat_time', '-n', type=int, default =10,  help='number of trajectories')"
         parser.add_argument('parameter name, command(dicide myself),defalt value, meaning of parameter')
    3. write args= parser.parse_args()
    4. write
    '''
    parser = argparse.ArgumentParser(description='runnning parameters')
    parser.add_argument('--repeat_time', '-n', type=int, default =10,  help='number of trajectories')
    parser.add_argument('--terminal', '-t', type=int, default =100,  help='terminal time')
    parser.add_argument('--mode', '-m', type=str, default ='standard',  help='mode of the random walk')
    args= parser.parse_args()
#pdb.set_trace()

    start = timeit.default_timer()
    main(args)
    stop = timeit.default_timer()
    print("elapsed %ssecs"%(stop - start))
