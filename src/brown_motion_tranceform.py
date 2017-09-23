#brown_motion 変換

import sys
sys.path.append("../src")
sys.path.append("../data")


import SDE_class as sde
import importlib #リロード呼ぶ関数
import numpy as np
from matplotlib import pyplot as plt
import util as util
import math
from scipy.stats import norm
import argparse
import pdb
import os


class brown_motion(sde.SDE_Markov):
    def __init__(self,**keyargs):
        super(brown_motion, self).__init__(**keyargs)#関数で使う時はselfはいらない

        self.key=keyargs

        self.normal_mean= self.key['n_mean']#noize nomal mean
        self.normal_scale= self.key['n_scale']#noize nomal variance
        self.transform_matrix_step= self.key['mat']#transition matrix
        self.noise_var_matrix= self.key['var_matrix']#noize matrix

    def one_step(self,now_position):
        random_variable_T=np.random.normal(self.normal_mean,self.normal_scale,self.dimen).reshape(self.dimen,1)
        now_position_T=now_position.reshape(self.dimen,1)
        new_position=now_position_T+np.dot(self.transform_matrix_step, now_position_T)*self.deltaT\
        +np.dot(self.noise_var_matrix, random_variable_T)*np.sqrt(self.deltaT)
        now_position = new_position
        return(new_position)

    def many_step(self,**keyargs):
        now_position=self.init
        trajectory_box=np.zeros((self.dimen,self.division+1))
        trajectory_box[:,0]=now_position
        for k in range(self.division):
            new_position = self.one_step(now_position)
            trajectory_box[:,k+1]=new_position
            now_position = new_position
        times = np.arange(0,self.terminal+self.deltaT,self.deltaT)
        times = np.asarray(times).reshape(1,len(times))
        return(times,trajectory_box)


    def simulation(self, numsamples = 10):
        sampledat = []
        for k in range(numsamples):
            times, trajectory_box = self.many_step()
            trajectory = trajectory_box[0]
            sampledat.append(trajectory)
        return(times, sampledat)



    def brown_motion_nomal(self,**keyargs):
        trajectory_box=np.zeros((self.dimen,self.division+1))
        qv_box=np.zeros((self.dimen,self.division))
        now_position = self.init
        trajectory_box[:,0]=now_position
        qv_box[:,0]=0
        for k in range(self.division):
            new_position = self.one_step(now_position)
            qv_box[:,k]=qv_box[:,k]+(now_position-new_position)**2
            trajectory_box[:,k+1]=new_position
            now_position = new_position
        trajectory = trajectory_box[0]
        return(trajectory,qv_box)

    def brown_motion_square(self,**keyargs):
        trajectory_box=np.zeros((self.dimen,self.division+1))
        qv_box=np.zeros((self.dimen,self.division))
        now_position = self.init
        trajectory_box[:,0]=now_position**2
        qv_box[:,0]=0
        for k in range(self.division):
            new_position = self.one_step(now_position)**2
            qv_box[:,k]=qv_box[:,k]+(now_position-new_position)**2
            trajectory_box[:,k+1]=new_position
            now_position = new_position
        trajectory = trajectory_box[0]
        return(trajectory,qv_box)


    def brown_motion_log(self,**keyargs):
        trajectory_box=np.zeros((self.dimen,self.division+1))
        qv_box=np.zeros((self.dimen,self.division))
        now_position = self.init
        trajectory_box[:,0]=np.log(now_position)
        qv_box[:,0]=0
        for k in range(self.division):
            new_position = np.log(self.one_step(now_position))
            qv_box[:,k]=qv_box[:,k]+(now_position-new_position)**2
            trajectory_box[:,k+1]=new_position
            now_position = new_position
        trajectory = trajectory_box[0]
        return(trajectory,qv_box)
