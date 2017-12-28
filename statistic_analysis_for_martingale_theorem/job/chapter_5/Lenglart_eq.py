
# this file is simulation of Lenglant_eq

import numpy as np
import sys
sys.path.append("../../src")#road a file

import random_walk as rd
import Lenglart as lg #load a file
import importlib #function to reroad a file

from matplotlib import pyplot as plt

import math
from scipy.stats import norm
import argparse
import pdb
import os

def main():

    init=np.array([0.])#init_value
    delta=args.delta #left term parameter
    nu=args.nu #right term parameter

    sdekey={}
    sdekey['init'] = init
    sdekey['term'] = args.terminal
    sdekey['jump_size'] = args.jump_size
    sdekey['prob'] = args.prob
    sdekey['repeat_time'] = args.repeat_time
    sdekey['model']=args.model
    sdekey['value']=args.value

    sdekey['delta']=delta
    sdekey['nu']=nu
    sdekey['normal_mean']=args.mean
    sdekey['normal_var']=args.var


    lgeq_eq= lg.Lenglart(**sdekey)#load a class
    for k in range (args.simulation):
        left_term,right_term=lgeq_eq.Lenglart_eq()#load a function
        print(left_term,right_term)




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
    parser.add_argument('--jump_size', '-j', type=int, default =1,  help='jump size')
    parser.add_argument('--prob', '-p', type=int, default =0.5,  help='jump size')
    parser.add_argument('--repeat_time', '-r', type=int, default =500,  help='number of trajectories')
    parser.add_argument('--model', '-m', type=str, default ='standard',  help='mode of the random walk')
    parser.add_argument('--value', '-v', type=str, default ='path',  help='value of the random walk')

    parser.add_argument('--delta', '-d', type=float, default =0.7,  help='left term parameter')
    parser.add_argument('--nu', '-nu', type=float, default =0.6,  help='right term parameter')
    parser.add_argument('--mean', '-n', type=int, default =0,  help='nomal mean')
    parser.add_argument('--var', '-var', type=int, default =1,  help='nomal var')
    parser.add_argument('--simulation', '-s', type=int, default =100,  help='simulation time')

    args= parser.parse_args()
#pdb.set_trace()
    main()
