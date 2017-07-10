#確率微分方程式の実装のためのクラス

import numpy as np#パッケージはクラスの外におかないといけない
import pdb
from matplotlib import pyplot as plt

'''
mymat:
myterm:
mynoise:
mydiv:
mynoise:
mymean:
myinit:
'''




class SDE_Markov:
    def __init__(self, mymat = np.eye(2),myvar = np.eye(2),myterm= 10,\
    mynoise = 1, mydiv = 1, mymean = 0 , myscale =1,myinit = np.array([1,1])):
        self.transform_matrix= mymat#遷移行列
        self.terminal= myterm#終点時間
        self.noize_var_matrix= myvar#ノイズ行列
        self.division= mydiv#分割数
        self.normal_mean= mymean#ノイズ正規分布の平均
        self.normal_scale= myscale#ノイズ正規分布の分散
        self.dimen = len(myinit)#次元
        self.init_value=myinit#初期値
        self.init= myinit.reshape(self.dimen, 1)#初期値(ベクトル)
        self.sanity_check()
        self.deltaT = 0.1

    def one_step(self,now_position=np.array([1,1]),parameter=1):
        random_variable_T=np.random.normal(self.normal_mean,self.normal_scale,self.dimen).reshape(self.dimen,1)
        #reshape ベクトルの形を指定する
        now_position_T=now_position.reshape(self.dimen,1)
        new_position=parameter*now_position_T+np.dot(self.transform_matrix, now_position_T)+np.dot(self.noize_var_matrix, random_variable_T)
        return(new_position)


    def one_step_small(self,now_position=np.array([1,1]),parameter=1):
        sqrt_time=np.sqrt(self.terminal/self.division)
        random_variable_T=np.random.normal(self.normal_mean,self.normal_scale,self.dimen).reshape(self.dimen,1)
        now_position_T=parameter*now_position.reshape(self.dimen,1)
        new_position=now_position_T+np.dot(self.transform_matrix, now_position_T)+np.dot(self.noize_var_matrix, random_variable_T)*sqrt_time


    def many_step(self, myTerm = 100. , default = False ):

        if default:
            myTerm = self.terminal

        times= myTerm/self.division
        times_number=int(times)

        now_position = self.init
        for k in range(times_number):
            new_position = self.one_step(now_position)
            now_position = new_position
        return(now_position)

    def many_step_martingale(self, myTerm = 100. , default = False ):

        if default:
            myTerm = self.terminal

        times= myTerm/self.division
        times_number=int(times)

        now_position = self.init
        for k in range(times_number):
            new_position = self.one_step_martingale(now_position)
            now_position = new_position
        return(now_position)


    def tragectory(self,myTerm = 100.,now_position=np.array([1,1])):
        times= myTerm/self.division
        times_number=int(times)
        tragectory_box=np.zeros((self.dimen,times_number))
        for k in range(times_number):
            new_position = self.one_step(now_position)
            tragectory_box[:,k]=new_position
            now_position=new_position
        return(tragectory_box)

    def tragectory_martingale(self,myTerm = 100.,now_position=np.array([1,1])):
        times= myTerm/self.division
        times_number=int(times)
        tragectory_box=np.zeros((self.dimen,times_number))
        for k in range(times_number):
            new_position = self.one_step_martingale(now_position)
            tragectory_box[:,k]=new_position
            now_position=new_position
        return(tragectory_box)


    def sanity_check(self):#警報機みたいなもの
        #pdb.set_trace()
        if len(self.transform_matrix.shape)<2 or\
         len(self.noize_var_matrix.shape)<2:
            print("you must input a matrix for the transformation and noise!!")
        else:
            mymatD, _ = self.transform_matrix.shape
            mymatD2, _ =  self.noize_var_matrix.shape
            if mymatD !=  self.dimen:
                print("Transformation dimension mismatch!! ")
            if mymatD2 !=  mymatD:
                print("noise and transformation dimension mismatch!! ")
#pdb.set_trace()　エラーの場所を探すコード
#行列の設定方法
#np.array([[],[],[]])
#行列の掛け算
