
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
    term=100#terminal_time
    init=np.array([0.])#init_value
    jump_size=1
    prob=0.5
    repeat_time=100 #time of trial

    delta=0.7
    nu=0.6
    simulation_time=100

    normal_mean=0
    normal_var=1

    sdekey={}
    sdekey['init'] = init
    sdekey['term'] = term
    sdekey['jump_size'] = jump_size
    sdekey['prob'] = prob
    sdekey['repeat_time'] = repeat_time
    sdekey['model']='standard'
    sdekey['value']='path'

    sdekey['delta']=delta
    sdekey['nu']=nu
    sdekey['normal_mean']=normal_mean
    sdekey['normal_var']=normal_var


    lgeq_eq= lg.Lenglart(**sdekey)#load a class
    for k in range (simulation_time):
        left_term,right_term=lgeq_eq.Lenglart_eq()#load a function
        print(left_term,right_term)




if __name__ == '__main__':

#pdb.set_trace()
    main()
