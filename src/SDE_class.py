#確率微分方程式の実装のためのクラス

import numpy as np#パッケージはクラスの外におかないといけない
import pdb
from matplotlib import pyplot as plt

'''
mymat:遷移行列 デフォルト2×2
mymat_noise:ノイズ項の遷移行列 デフォルト2×2
myvar:ノイズ行列 デフォルト2×2
myterm:終点時間
mydiv:
mymean:ノイズ正規分布平均
myscale:ノイズ正規分布分散
myinit:初期値 二次元ベクトル
step_size:一歩の大きさ
'''

'''
X(t)=X(t-1)+mymat*X(t-1)+myvar*normal
ノイズ項の形が合わない
'''

class SDE_Markov:
    def __init__(self, mymat = np.eye(2),mymat_noise = np.eye(2),myvar = np.eye(2),myterm= 10,\
    mymean = 0 , myscale =1,myinit = np.array([1,1]),step_size=0.1):
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

        self.sanity_check()


    def one_step(self,now_position=np.array([1,1])):
        random_variable_T=np.random.normal(self.normal_mean,self.normal_scale,self.dimen).reshape(self.dimen,1)
        now_position_T=now_position.reshape(self.dimen,1)
        new_position=now_position_T+np.dot(self.transform_matrix_step, now_position_T)*self.deltaT\
        +np.dot(self.noise_var_matrix, random_variable_T)*np.sqrt(self.deltaT)
        return(new_position)

    def many_step(self,now_position=np.array([1,1])):
        division=int(self.division)
        trajectory_box=np.zeros((self.dimen,division+1))
        trajectory_box[:,0]=now_position
        for k in range(division):
            new_position = self.one_step(now_position)
            trajectory_box[:,k+1]=new_position
            now_position = new_position
        return(trajectory_box)


    def sanity_check(self):#警報機みたいなもの
        #pdb.set_trace()
        if len(self.transform_matrix_step.shape)<2 or\
         len(self.noise_var_matrix.shape)<2:
            print("you must input a matrix for the transformation and noise!!")
        else:
            mymatD, _ = self.transform_matrix_step.shape
            mymatD2, _ =  self.noise_var_matrix.shape
            if mymatD !=  self.dimen:
                print("Transformation dimension mismatch!! ")
            if mymatD2 !=  mymatD:
                print("noise and transformation dimension mismatch!! ")
#pdb.set_trace()　エラーの場所を探すコード
#行列の設定方法
#np.array([[],[],[]])
#行列の掛け算 np.dot(,)
