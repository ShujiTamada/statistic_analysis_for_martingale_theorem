
'''
simulation thorem 5.1.1
'''

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

def main(args):
    init=np.array([0.])#init_value


    sdekey={}
    sdekey['init'] = init #init place
    sdekey['term'] = args.terminal #terminal times
    sdekey['jump_size'] = args.jump #jump size value
    sdekey['prob'] = args.prob #translate probability
    sdekey['repeat_time'] = args.repeat_time #number of path
    sdekey['model']=args.model#selection path model
    sdekey['value']=args.value #section path value

    figplace = '../../fig/thm5.1.1' #move to fig file
    pathname= str('%s_rw_path.png'%sdekey['model']) #picture name of path of thorem 5.1.1
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
    parser.add_argument('--terminal', '-t', type=int, default =100,  help='terminal time')
    parser.add_argument('--jump', '-j', type=int, default =1,  help='jump size')
    parser.add_argument('--prob', '-p', type=int, default =0.5,  help='jump size')
    parser.add_argument('--repeat_time', '-r', type=int, default =5000,  help='number of trajectories')
    parser.add_argument('--model', '-m', type=str, default ='square_minus_qv',  help='mode of the random walk')
    parser.add_argument('--value', '-v', type=str, default ='path',  help='value of the random walk')
    args= parser.parse_args()
#pdb.set_trace()
    start = timeit.default_timer()
    main(args)
    stop = timeit.default_timer()
    print("elapsed %ssecs"%(stop - start))
