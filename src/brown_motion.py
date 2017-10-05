#brown_motion trancefform

import sys
sys.path.append("../src")
sys.path.append("../data")


import SDE_class as sde
import importlib #funciton for doing reload
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
        super(brown_motion, self).__init__(**keyargs)#becase of using for function,don't use self

        self.key=keyargs
        self.normal_mean= self.key['n_mean']#noize nomal mean
        self.normal_scale= self.key['n_scale']#noize nomal variance
        self.transform_matrix_step= self.key['matrix']#transition matrix
        self.noise_var_matrix= self.key['var_matrix']#noize matrix

        self.observation= self.key['observation']#noize matrix


    def outcome_output(self,**keyargs):
        trajectory_box=np.zeros((self.dimen,self.division+1))
        qv_box=np.zeros((self.dimen,self.division+1))
        times=np.arange(0,self.terminal+self.deltaT,self.deltaT)
        times = np.asarray(times).reshape(1,len(times))
        return(trajectory_box,qv_box,times)

    def function_select(self):
        if self.function_select==brown_motion_normal:
            function=self.brown_motion_normal()
        if self.function_select==brown_motion_sq:
            function=self.brown_motion_sq()
        if self.function_select==brown_motion_Doob_mayer:
            function=self.brown_motion_Doob_mayer()
        else:
           function=self.brown_motion_normal()




    def one_step(self,now_position):
        random_variable_T=np.random.normal(self.normal_mean,self.normal_scale,self.dimen).reshape(self.dimen,1)
        now_position_T=now_position.reshape(self.dimen,1)
        updatevalue =  np.dot(self.transform_matrix_step, now_position_T)*self.deltaT\
        +np.dot(self.noise_var_matrix, random_variable_T)*np.sqrt(self.deltaT)
        new_position=now_position_T+ updatevalue
        now_position = new_position
        return(new_position)

    def many_step(self,**keyargs):
        trajectory_box,qv_box,times=self.outcome_output()
        now_position=self.init
        trajectory_box[:,0]=now_position
        for k in range(self.division):
            new_position = self.one_step(now_position)
            trajectory_box[:,k+1]=new_position
            now_position = new_position
        return(times,trajectory_box,times)


    def simulation(self, numsamples = 10):
        print("Initiating the simulation sequence...")
        sampledat = []
        for k in range(numsamples):
            if np.mod(k, 100) == 0:
                print('%s paths complete'%k)
            times, trajectory_box,qv_box = self.brown_motion_normal()
            if self.observation=='qv':
                observation=qv_box[0]
            else:
                observation=trajectory_box[0]
            sampledat.append(observation)
        sampledat = np.array(sampledat)
        print("Simulations successfully completed!")
        return(times, sampledat)




    def saveFigure(self,figpath,numsamples= 10):
        times, trajectory_box = self.simulation(numsamples)
        times=times[0]
        plt.figure(figsize = (20,20))
        for k in range(len(trajectory_box)):
            k_th_trajectory = trajectory_box[k]
            myfig = plt.plot(times, k_th_trajectory, color='r')
        plt.savefig(figpath)

    def brown_motion_normal(self,**keyargs):
        trajectory_box,qv_box,times=self.outcome_output()
        now_position = self.init
        trajectory_box[:,0]=now_position
        qv_box[:,0]=0
        for k in range(self.division):
            new_position = self.one_step(now_position)
            qv_box[:,k+1]=qv_box[:,k]+(now_position-new_position)**2
            trajectory_box[:,k+1]=new_position
            now_position = new_position
        return(times,trajectory_box,qv_box)




    def brown_motion_square(self,**keyargs):
        trajectory_box,qv_box,times=self.outcome_output()
        now_position = self.init
        now_position_sq = self.init**2
        trajectory_box[:,0]=now_position_sq
        qv_box[:,0]=0
        for k in range(self.division):
            new_position = self.one_step(now_position)
            new_position_sq = new_position**2
            qv_box[:,k+1]=qv_box[:,k]+(new_position_sq-new_position_sq)**2
            trajectory_box[:,k+1]=new_position**2
            now_position = new_position
            now_position_sq = new_position_sq
        return(times,trajectory_box,qv_box)


    def brown_motion_Doob_mayer(self,**keyargs):
        trajectory_box,qv_box,times=self.outcome_output()
        now_position = self.init
        now_position_doob = self.init**2
        trajectory_box[:,0]=now_position_doob
        qv_box[:,0]=0
        for k in range(self.division):
            new_position = self.one_step(now_position)
            new_position_doob=new_position**2-k*self.deltaT
            qv_box[:,k+1]=qv_box[:,k]+(new_position_doob**2-now_position_doob**2)**2
            trajectory_box[:,k+1]=new_position_doob
            now_position = new_position
            now_position_doob = new_position_doob
        return(times,trajectory_box,qv_box)
