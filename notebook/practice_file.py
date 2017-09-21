#練習
import sys
#sys.path.append("../notebook")
sys.path.append("../src")#ファイル読み込み
sys.path.append("../data")#ファイル読み込み
sys.path.append("../fig")#ファイル読み込み
#sys.path.append("../SDE_class.py")
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

    term=1#最終時刻
    step=0.1#刻み幅
    div=term/step#飛ぶ回数
    init=np.array([0.])#初期値
    #repeat_time=20000#pass本数
    #S=0
    sdekey={}
    sdekey['default'] = True
    sdekey['init'] = init
    sdekey['stepsize'] = step
    sdekey['term'] = term
    sdekey['variance'] = 1.0
    sdekey['mean'] = 1.0


    mymodel = sde.SDE_Markov(**sdekey)
    simulate=bmt.brown_motion(**sdekey)

    #transform_matrix_step=np.array([[0.]]),transform_matrix_noise=np.array([[1.]]),noise_var_matrix,terminal,\
    #deltaT,division,normal_mean,normal_scale,dimen,init

    #brown_motion_nomal=simulate.brown_motion_nomal()

if __name__ == '__main__':
    main()
