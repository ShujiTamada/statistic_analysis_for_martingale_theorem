#練習
import sys
sys.path.append("../src")#ファイル読み込み
sys.path.append("../data")#ファイル読み込み
sys.path.append("../fig")#ファイル読み込み
import SDE_class as sde
import brown_motion_tranceform as bmt
import importlib #リロード呼ぶ関数
import numpy as np
from matplotlib import pyplot as plt
import util as util
import math
from scipy.stats import norm
import argparse
import pdb
import os

def main():
    #SDE_Markov variation_number
    term=1#terminal_time
    step=0.1#step_size
    div=term/step#jump_number
    init=np.array([1000.])#init_value

    #brown_motion_tranceform variation_number
    #matrix=
    #mat_noise=
    #var_matrix=
    mean=0
    variance=1




    sdekey={}
    sdekey['default'] = True
    sdekey['init'] = init
    sdekey['stepsize'] = step
    sdekey['term'] = term

    sdekey['mat'] = np.array([[1.]])
    #sdekey['mat_noise'] = 1.0
    sdekey['var_matrix'] = np.array([[1.]])
    sdekey['n_mean'] = mean
    sdekey['n_scale'] = variance


    mymodel = sde.SDE_Markov(**sdekey)
    simulate=bmt.brown_motion(**sdekey)

    #transform_matrix_step=np.array([[0.]]),transform_matrix_noise=np.array([[1.]]),noise_var_matrix,terminal,\
    #deltaT,division,normal_mean,normal_scale,dimen,init

    times,trajectory,qv=simulate.brown_motion_nomal()
    print(times.shape)
    print(trajectory.shape)
    print(qv.shape)

if __name__ == '__main__':
    main()
