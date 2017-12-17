#random_walk
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import pdb

class random_walk:
      def __init__(self, **keyargs):
          self.key = keyargs
          self.terminal= self.key['term'] #terminal
          self.dimen = len(self.key['init'])#dimension
          self.jump_size=self.key['jump_size']#jump_size
          self.init= self.key['init'].reshape(self.dimen, 1)#初期値(ベクトル)
          self.prob=self.key['prob']#translate probability
          self.repeat_time=self.key['repeat_time']#number of path
          self.model=self.key['model']#selection path model
          self.value=self.key['value']#selection path value(for example quadratic valuation, path and so on.)
      '''
      this function runs noize term.
      Noize distribution is binomial
      '''

      def generateDelta_binom(self,jumpsize):
          random_variable=(np.random.binomial(1,self.prob,1)*2 -1) *self.jump_size
          return(random_variable)

      '''
      This function is one step.
      All function uses this function.
      '''
      def one_step(self,placenow,**keyargs):
          random_variable=self.generateDelta_binom(self.jump_size)
          #make noize
          placenow = placenow + random_variable
          return(placenow)

      '''
      this function use for model selection.
      Model is standard, if simulate model is standrd.
      Model is square, if simulate model is standrd.

      '''
      def model_selection(self,**keyargs):
          if self.model=='standard' and self.value =='path':
              #select path of standard random walk
             path,qv=self.random_walk_standard()
             model_value=path
          elif self.model=='standard' and self.value =='qv':
              #select qv of standard random walk
             path,qv=self.random_walk_standard()
             model_value=qv
          elif self.model=='square_minus_qv' and self.value =='path':
              #select path of square_minus_qv
             path,qv=self.random_walk_square_minus_qv()
             model_value=path
          elif self.model=='square_minus_qv' and self.value =='square_random_walk':
              #select path of square_random_walk
             path,square_random_walk=self.random_walk_square_minus_qv()
             model_value=square_random_walk
          else:
             print('manuke')
             raise NotImplementedError
          return(model_value)

      '''
      This function runs standrd random walk.
      '''
      def random_walk_standard(self,**keyargs):
          placenow=self.init
          standrd_random_walk = np.zeros(self.terminal+1)#box for recording path value
          qv = np.zeros(self.terminal+1)#box for recording quadratic valuation
          standrd_random_walk[0] = placenow#record init value
          qv[0] = placenow**2#record init quadratic valuation
          oldplace=placenow
          for k in range(self.terminal):
              placenow=self.one_step(placenow)
              standrd_random_walk[k+1] = placenow #record path value
              qv[k+1]=qv[k]+(placenow-oldplace)**2#record quadratic valuation
              oldplace=placenow
          return(standrd_random_walk,qv)
      '''
      This function runs square random walk minus standard random walk quadratic valuation
      For using this functiion, it is to find that
           square random walk minus standard random walk quadratic valuation is martingale.
      '''
      def random_walk_square_minus_qv(self,**keyargs):
          placenow=self.init
          square_random_walk = np.zeros(self.terminal+1)#box for recording square random walk path value
          qv_box_standard = np.zeros(self.terminal+1)#box for recording quadratic valuation of standard random valuation
          square_minus_qv = np.zeros(self.terminal+1)#box for recording square minus quadratic valuation path value
          square_random_walk[0] = placenow**2
          qv_box_standard[0] = placenow**2
          square_minus_qv[0]=square_random_walk[0]- qv_box_standard[0]
          for k in range(self.terminal):
              random_variable = self.generateDelta_binom(self.jump_size)
              placenow=placenow+random_variable
              square_random_walk[k+1] = placenow**2 #record square random walk path value
              qv_box_standard[k+1]=qv_box_standard[k]+random_variable**2 #record quadratic valuation of standard random valuation
              square_minus_qv[k+1]=square_random_walk[k+1]-qv_box_standard[k+1]#record square minus quadratic valuation path value
          return(square_minus_qv,square_random_walk)


      '''
      this function runs multi dimension random walk
      remark glaph is left of
      '''

      def random_walk_multi_dim(self,**keyargs):
          multi_dim_random_walk = np.zeros([self.dimen,self.terminal+1])
          placenow=self.init
          sb=placenow.shape
          multi_dim_random_walk[0:0+sb[0],0:0+sb[1]]=placenow
          for k in range(self.terminal):
              random_variable=np.random.randn(self.dimen,1)
              placenow=placenow+random_variable
              multi_dim_random_walk[0:0+sb[0],k+1:k+1+sb[1]]=placenow
              path=1
          return(multi_dim_random_walk,path)

      '''
      This method runs the simulation of the designated mode.
      Inputs:
      Output:
      '''
      def simulation(self,**keyargs):
          times=np.arange(0,self.terminal+1,1)#box for time
          times = np.asarray(times).reshape(1,len(times))#making time array
          model_path=np.zeros([self.repeat_time,self.terminal+1])#box for recording all path value
          terminal_value=np.zeros(self.repeat_time)#box for recording all path terminal value
          for k in range(self.repeat_time):#record all path value in model_path
              if np.mod(k, 100) == 0:
                  print('%s paths complete'%k)
              model_value=self.model_selection()
              model_path[k]=model_value
              terminal_value[k]=model_value[self.terminal]
          average=np.average(terminal_value) #average terminal value
          variance = np.var(terminal_value) #variance terminal value
          print('average terminal value is%s'%average)
          print('variance of the terminal value is%s'%variance)
          return(times, model_path,terminal_value)

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

      def plot_glaph(self,figpath,fighist,**keyargs):
          times, sample_box,terminal=self.simulation()
          times=times[0]
          for k in range(self.repeat_time):
              k_th_trajectory=sample_box[k]
              plt.plot(times, k_th_trajectory)#making a glaph
          plt.savefig(figpath)
          plt.close()#this command separate glaph and histglam
          plt.hist(terminal,40)#making a histglam
          plt.savefig(fighist)



#pdb.set_trace()
