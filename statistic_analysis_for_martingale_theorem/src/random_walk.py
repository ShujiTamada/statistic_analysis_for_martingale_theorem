#random_walk


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import pdb

class random_walk:
      def __init__(self, **keyargs):
          self.key = keyargs
          self.terminal= self.key['term'] #terminal
          self.dimen = len(self.key['init'])#dimension
          self.jump_size=self.key['jump_size']
          self.init= self.key['init'].reshape(self.dimen, 1)#初期値(ベクトル)
          self.prob=self.key['prob']
          self.repeat_time=self.key['repeat_time']
          self.model=self.key['model']


      def one_step(self,placenow,**keyargs):
          random_variable=np.random.binomial(1,self.prob,1)*2*self.jump_size -self.jump_size
          placenow = placenow + random_variable
          return(placenow)

      def model_selection(self,**keyargs):
          if self.model=='standard':
             trajectory_box,qv_box=self.random_walk_standard()
          elif self.model=='sq_qv':
             trajectory_box,qv_box=self.rdw_sq_qv()
          else:
             print('manuke')
          return(trajectory_box,qv_box)


      def random_walk_standard(self,**keyargs):
          trajectory_box = np.zeros(self.terminal+1)
          qv_box = np.zeros(self.terminal+1)
          trajectory_box[0] = self.init
          qv_box[0] = self.init**2
          placenow=self.init
          for k in range(self.terminal):
              placenow=self.one_step(placenow)
              trajectory_box[k+1] = placenow
              qv_box[k+1]=qv_box[k]+placenow**2
          return(trajectory_box,qv_box)

      def rdw_sq_qv(self,**keyargs):
          trajectory_box = np.zeros(self.terminal+1)
          qv_box = np.zeros(self.terminal+1)
          path = np.zeros(self.terminal+1)
          trajectory_box[0] = self.init**2
          qv_box[0] = self.init**2
          placenow=self.init
          path[0]=trajectory_box[0]- qv_box[0]
          for k in range(self.terminal):
              random_variable=np.random.binomial(1,self.prob,1)*2*self.jump_size -self.jump_size
              placenow=placenow+random_variable
              trajectory_box[k+1] = placenow**2
              qv_box[k+1]=qv_box[k]+random_variable**2 #this value is standard random_walk qv
              path[k+1]=trajectory_box[k+1]-qv_box[k+1]
          return(path,qv_box)



      def rw_multi_dim(self,**keyargs):
          trajectory_box = np.zeros([self.dimen,self.terminal+1])
          placenow=self.init
          sb=placenow.shape
          trajectory_box[0:0+sb[0],0:0+sb[1]]=placenow
          for k in range(self.terminal):
              rv=np.random.randn(self.dimen,1)
              print(rv)
              placenow=placenow+rv
              trajectory_box[0:0+sb[0],k+1:k+1+sb[1]]=placenow
              path=1
          return(trajectory_box,path)

      def simulation(self,**keyargs):
          times=np.arange(0,self.terminal+1,1)
          times = np.asarray(times).reshape(1,len(times))
          sample_box=np.zeros([self.repeat_time,self.terminal+1])
          summation=0
          terminal_box=np.zeros(self.repeat_time)
          for k in range(self.repeat_time):
              if np.mod(k, 100) == 0:
                  print('%s paths complete'%k)
              trajectory,qv=self.model_selection()
              sample_box[k]=trajectory
              terminal_box[k]=trajectory[self.terminal]
          average=np.average(terminal_box)
          print(average)
          return(times, sample_box,terminal_box)

      def simulation_multi_dim(self,**keyargs):
          times=np.arange(0,self.terminal+1,1)
          times = np.asarray(times).reshape(1,len(times))
          sample_box=np.zeros([self.repeat_time*2,self.terminal+1])
          summation=0
          for k in range(self.repeat_time):
              if np.mod(k, 1) == 0:
                  print('%s paths complete'%k)
              trajectory,qv=self.rw_multi_dim()
              sb=trajectory.shape
              sample_box[k:k+sb[0],0:0+sb[1]]=trajectory
          return(times, sample_box)

      def plot_glaph(self,figpath,**keyargs):
          times, sample_box,terminal=self.simulation()
          times=times[0]
          for k in range(self.repeat_time):
              k_th_trajectory=sample_box[k]
              plt.plot(times, k_th_trajectory)
          plt.savefig(figpath)


      def plot_hist(self,fighist,**keyargs):
          times, sample_box,terminal=self.simulation()
          plt.hist(terminal,20)
          plt.savefig(fighist)


#pdb.set_trace()
