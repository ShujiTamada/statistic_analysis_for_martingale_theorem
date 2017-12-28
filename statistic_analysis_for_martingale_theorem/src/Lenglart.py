
'''
this file is simulation of Lenglart equation.
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

class Lenglart(rd.random_walk):
    def __init__(self,**keyargs):
        super(Lenglart, self).__init__(**keyargs)#becase of using for function,don't use self
        self.delta= self.key['delta']
        self.nu = self.key['nu']

        self.normal_mean = self.key['normal_mean']
        self.normal_var = self.key['normal_var']


    def Lenglart_eq(self):
        left_term_event_true=0 # this is a number which left term event is true.
        right_term_event_true=0 # this is a number which right term event is true.
        for k in range(self.repeat_time):
            now_place=self.init
            increase_process0=self.init
            path_value_box = np.zeros(self.terminal+1) #box for recording path value
            path_value_box[0]=now_place
            switch=True #this is swich to stop path.
            for i in range(self.terminal):
                #random_variable=np.random.binomial(1,self.prob,1)*2*self.jump_size -self.jump_size
                if switch==True:
                    random_variable=np.random.normal(self.normal_mean,self.normal_var)
                    now_place=now_place+random_variable
                    path_value_box[i+1]=now_place
                    increase_process0=increase_process0+np.abs(random_variable)
                    increase_process = self.sigmoid(increase_process0)
                if now_place>self.nu:#stopping time condition
                    switch=False
            X_max=np.max(path_value_box)
            if X_max>self.nu: #this is decision that left term event is true or not
                left_term_event_true=left_term_event_true+1
            if increase_process>self.delta: #this is decision that right term event is true or not
                right_term_event_true=right_term_event_true+1
        prob_left=left_term_event_true/self.repeat_time #make left term probability
        prob_right=self.delta/self.nu+right_term_event_true/self.repeat_time #make right term probability
        return(prob_left,prob_right) #prob_left is left term of equation. prob_right is right term of equation.

    def sigmoid(self,x):
        val =  np.exp(x)/(1 + np.exp(x))
        return(val)
