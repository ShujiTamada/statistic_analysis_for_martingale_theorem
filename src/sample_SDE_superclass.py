#sample superclass
#確率微分方程式の実装のためのクラス

import numpy as np#パッケージはクラスの外におかないといけない
import pdb
from matplotlib import pyplot as plt
import pdb
koyamaSAN = None

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
    def __init__(self, **keyargs):


        self.key = keyargs
        #mymat = self.key['mat']
        #mymat_noise = mykey['mat_noise']
        #myvar = mykey['var']
        #myterm = mykey['term']
        #mymean = mykey['mean']
        #mymat = mykey['mat']
        #myscale = mykey['scale']
        #myinit = mykey['init']
        #step_size = mykey['stepsize']

        #classの与えたい変数一覧 辞書式にする事によって順番を無視できる
        self.default_initialize()


        #self.transform_matrix_step= mymat#遷移行列
        #self.transform_matrix_noise=mymat_noise
        #self.noise_var_matrix= myvar#ノイズ行列
        self.terminal= self.key['term'] #終点時間
        self.deltaT = self.key['stepsize']
        self.division= int(np.ceil(self.terminal/self.deltaT))#分割数
        #self.normal_mean= mymean#ノイズ正規分布の平均
        #self.normal_scale= myscale#ノイズ正規分布の分散
        self.dimen = len(self.key['init'])#次元
        self.init= self.key['init'].reshape(self.dimen, 1)#初期値(ベクトル)

        self.sanity_check()

    def default_initialize(self):#デフォルト値入力
        if self.key['default'] :
            pass
        else:
            pass


    def one_step(self,now_position=np.array([1,1])):
        #random_variable_T=np.random.normal(self.normal_mean,self.normal_scale,self.dimen).reshape(self.dimen,1)
        #now_position_T=now_position.reshape(self.dimen,1)
        #new_position=now_position_T+np.dot(self.transform_matrix_step, now_position_T)*self.deltaT\
        #+np.dot(self.noise_var_matrix, random_variable_T)*np.sqrt(self.deltaT)
        now_position = new_position
        return(new_position)


    #def many_step(self,now_position=np.array([1,1])):
        #division=int(self.division)
        #trajectory_box=np.zeros((self.dimen,division+1))
        #trajectory_box[:,0]=now_position
        #for k in range(division):
            #new_position = self.one_step(now_position)
            #trajectory_box[:,k+1]=new_position
            #now_position = new_position
        #return(trajectory_box)

    def many_step(self, **keyargs):
        trajectory_box=np.zeros((self.dimen,self.division+1))
        trajectory_box[:,0]=now_position
        for k in range(division):
            new_position = self.one_step(now_position)
            trajectory_box[:,k+1]=new_position
            now_position = new_position
        return(trajectory_box)
    '''
    def many_step(self):
        now_position = self.init
        division=int(self.division)
        trajectory_box=np.zeros((self.dimen,division+1))
        trajectory_box[:,0]=now_position
        for k in range(division):
            new_position = self.one_step(now_position)
            trajectory_box[:,k+1]=new_position
            now_position = new_position
        #times=np.zeros((self.dimen,self.terminal*self.deltaT+1))
        times = np.arange(0,self.terminal+self.deltaT,self.deltaT)
        #times = np.asarray(times).reshape(1,len(times))
        return(times, trajectory_box)

    def simulation(self, numsamples = 10):
        sampledat = []
        for k in range(numsamples):
            times, trajectory_box = self.many_step()
            trajectory = trajectory_box[0]
            sampledat.append(trajectory)
        return(times, sampledat)
    '''



    def saveFig(self,figpath, numsamples= 10):
        times, trajectory_box = self.simulation(numsamples)
        #pdb.set_trace()

        for k in range(len(trajectory_box)):
            k_th_trajectory = trajectory_box[k]
            myfig = plt.plot(times, k_th_trajectory, color='r')
        plt.savefig(figpath)


    def sanity_check(self):#警報機みたいなもの
        pass
        '''
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
        '''
#pdb.set_trace()　エラーの場所を探すコード
#行列の設定方法
#np.array([[],[],[]])
#行列の掛け算 np.dot(,)
