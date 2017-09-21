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
        pdb.set_trace()
        super().__init__(self, **keyargs)
        mean = keyargs['mean']
        var  = keyargs['variance']
     #新しい変数は self.を作る？？
#deltaT division dimen

    def brown_motion_nomal(self):
        #sampledat = []
        trajectory_box=np.zeros((self.dimen,self.division+1))
        qv_box=np.zeros((self.dimen,self.division))
        now_position = self.init
        trajectory_box[:,0]=now_position
        for k in range(self.division):
            new_position = self.one_step(now_position)
            qv_box[k]=qv_box[k-1]+(now_position-new_position)**2
            trajectory_box[:,k+1]=new_position
            now_position = new_position
        trajectory = trajectory_box[0]
        #sampledat.append(trajectory)
        return(trajectory,qv_box)


    def unko():
        print("koyamasan is Joujaku!!")

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
