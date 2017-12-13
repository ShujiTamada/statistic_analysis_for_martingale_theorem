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


    def Lenglart_eq(self):
        count_1=0
        count_2=0
        for k in range(self.repeat_time):
            count=0
            now_place=self.init
            increase_process=self.init
            trajectory_box = np.zeros(self.terminal+1)
            trajectory_box[0]=now_place
            switch=True
            for i in range(self.terminal):
                #random_variable=np.random.binomial(1,self.prob,1)*2*self.jump_size -self.jump_size
                if switch==True:
                    random_variable=np.random.normal(0,10)
                    now_place=now_place+random_variable
                    trajectory_box[i+1]=now_place
                    increase_process=increase_process+np.abs(random_variable)
                    count=count+1
                if now_place>self.nu:#stopping time condition
                    switch=False
            X_max=np.max(trajectory_box)
            if X_max>self.nu:
                count_1=count_1+1
            if increase_process>self.delta:
                count_2=count_2+1
        prob_left=count_1/self.repeat_time
        prob_right=self.delta/self.nu+count_2/self.repeat_time
        return(prob_left,prob_right) #prob_left is left term of equation. prob_right is right term of equation.
