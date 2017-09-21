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
    def __init__(self):
        super(brown_motion,self).__init__(self, mymat = np.eye(2),mymat_noise = np.eye(2),myvar = np.eye(2),myterm= 10,\
        mymean = 0 , myscale =1,myinit = np.array([1,1]),step_size=0.1)

        self.transform_matrix_step= mymat#遷移行列
        self.transform_matrix_noise=mymat_noise
        self.noise_var_matrix= myvar#ノイズ行列
        self.terminal= myterm#終点時間
        self.deltaT = step_size
        self.division= self.terminal/self.deltaT#分割数
        self.normal_mean= mymean#ノイズ正規分布の平均
        self.normal_scale= myscale#ノイズ正規分布の分散
        self.dimen = len(myinit)#次元
        self.init= myinit.reshape(self.dimen, 1)#初期値(ベクトル)
     #新しい変数は self.を作る？？
#deltaT division dimen

    def brown_motion_nomal(self):
        sampledat = []
        division=int(self.division)
        trajectory_box=np.zeros((self.dimen,division+1))
        qv_box=np.zeros((self.dimen,division))
        trajectory_box[:,0]=np.log(now_position)
        for k in range(division):
            new_position = np.log(self.one_step(now_position))
            qv_box[k]=qv_box[k-1]+(now_position-new_position)**2
            trajectory_box[:,k+1]=new_position
            now_position = new_position
        trajectory = trajectory_box[0]
        sampledat.append(trajectory)
        return(trajectory,qv_box,sampledat)


    def brown_motion_square(self):
        sampledat = []
        division=int(self.division)
        trajectory_box=np.zeros((self.dimen,division+1))
        qv_box=np.zeros((self.dimen,division))
        #qv=np.zeros((self.dimen,1))
        trajectory_box[:,0]=now_position**2
        for k in range(division):
            new_position = self.one_step(now_position)**2
            #qv=qv+(now_position-new_position)**2
            qv_box[k]=qv_box_[k-1]+(now_position-new_position)**2
            trajectory_box[:,k+1]=new_position
            now_position = new_position
        trajectory = trajectory_box[0]
        sampledat.append(trajectory)
        return(trajectory,qv_box,sampledat)


    def brown_motion_log(self):
        sampledat = []
        division=int(self.division)
        trajectory_box=np.zeros((self.dimen,division+1))
        qv_box=np.zeros((self.dimen,division))
        #qv=np.zeros((self.dimen,1))
        trajectory_box[:,0]=now_position**2
        for k in range(division):
            new_position = self.one_step(now_position)**2
            #qv=qv+(now_position-new_position)**2
            qv_box[k]=qv_box[k-1]+(now_position-new_position)**2
            trajectory_box[:,k+1]=new_position
            now_position = new_position
        trajectory = trajectory_box[0]
        sampledat.append(trajectory)
        return(trajectory,qv_box,sampledat)
