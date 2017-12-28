
'''
this file is simulation of martingale convergence.
'''


import sys
sys.path.append("../src")
sys.path.append("../data")


import random_walk as rd
import importlib #funciton for doing reload
import numpy as np
from matplotlib import pyplot as plt
import math
from scipy.stats import norm
import argparse
import pdb
import os

class martingale_convergence(rd.random_walk):
    def __init__(self,**keyargs):
        super(martingale_convergence, self).__init__(**keyargs)#becase of using for function,don't use self

        self.nu=self.key['nu']


    def martingale_convergence(self):
        now_place=self.init
        repeat_time=100
        for k in range(repeat_time)
            new_place=self.one_step(now_place)
            variance=(new_place-now_place)**2
            sum_variance=sum_variance+variance
        sigma=sum_variance/repeat_time
        sigma_t=sigma_t+sigma
        
