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

term=1#最終時刻
step=0.1#刻み幅
div=term/step#飛ぶ回数
init=np.array([0.])#初期値
#repeat_time=20000#pass本数
#S=0
mymodel = sde.SDE_Markov(mymat=np.array([[0.]]), myvar =np.array([[1.]]),myinit=init,myscale=1.,myterm=term,step_size=step)

simulate=bmt.brown_motion(mymat=np.array([[0.]]), myvar =np.array([[1.]]),myinit=init,myscale=1.,myterm=term,step_size=step)
#transform_matrix_step=np.array([[0.]]),transform_matrix_noise=np.array([[1.]]),noise_var_matrix,terminal,\
#deltaT,division,normal_mean,normal_scale,dimen,init

brown_motion_nomal=simulate.brown_motion_nomal()
