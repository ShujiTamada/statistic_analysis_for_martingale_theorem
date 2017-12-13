# simulation thm 5.1.1

#make a random walk
import numpy as np
import sys
sys.path.append("../src")#road a file

import random_walk as rd
#from random_walk import random_walk as rdw
import importlib #function to reroad a file

from matplotlib import pyplot as plt

import math
from scipy.stats import norm
import argparse
import pdb
import os
import timeit

def main(args):
    term=100#terminal_time
    init=np.array([0.])#init_value
    jump_size=1
    prob=0.5
    repeat_time=args.repeat_time

    sdekey={}
    sdekey['init'] = init
    sdekey['term'] = args.terminal
    sdekey['jump_size'] = jump_size
    sdekey['prob'] = prob
    sdekey['repeat_time'] = repeat_time
    sdekey['model']=args.mode

    figplace = '../fig/thm5.1.1'#move to fig file
    pathname= str('random_walk_path_%s.png'%sdekey['model'])
    pathfilename= str('random_walk_path_%s.npy'%sdekey['model'])

    histname= str('random_walk_hist_%s.png'%sdekey['model'])
    fighist= os.path.join(figplace,histname)
    figpath= os.path.join(figplace,pathname)
    filepath = os.path.join(figplace,pathfilename)

    rd_walk = rd.random_walk(**sdekey)
    rd_walk.plot_graph(figpath,filepath,fighist) #why does the glaph get together
    #rd_walk.plot_hist(fighist)

    #trajectory=rd_walk.integral_discrete()
    #print(trajectory)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='runnning parameters')
    parser.add_argument('--repeat_time', '-n', type=int, default =10,  help='number of trajectories')
    parser.add_argument('--terminal', '-t', type=float, default =100,  help='terminal time')
    parser.add_argument('--mode', '-m', type=str, default ='standard',  help='mode of the random walk')

    args= parser.parse_args()
#pdb.set_trace()

    start = timeit.default_timer()

    main(args)

    stop = timeit.default_timer()

    print("elapsed %ssecs"%(stop - start))
