# Lenglant_eq

import numpy as np
import sys
sys.path.append("../src")#road a file

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
    repeat_time=1
    delta=2
    nu=2

    sdekey={}
    sdekey['init'] = init
    sdekey['term'] = term
    sdekey['jump_size'] = jump_size
    sdekey['prob'] = prob
    sdekey['repeat_time'] = repeat_time
    sdekey['model']='sq_qv'
    sdekey['delta']=delta
    sdekey['nu']=nu


    lgeq_eq= lg.Lenglart(**sdekey)#load a class
    for k in range (1):
        left_term,right_term=lgeq_eq.Lenglart_eq()#load a function
        print(left_term,right_term)




if __name__ == '__main__':

#pdb.set_trace()
    main()
