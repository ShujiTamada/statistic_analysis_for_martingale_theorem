import sys
sys.path.append("../src")
sys.path.append("../data")
sys.path.append("../fig")
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


def main():
    figplace = '../figs'#fig ファイルに移動

    parser = argparse.ArgumentParser(description='SDE simulation')
    parser.add_argument('--term', '-t', type=float, default =1, help='terminal time of the simulation' )
    parser.add_argument('--step', '-s', type=float, default =0.1, help='size of the jump step' )
    parser.add_argument('--init', '-init', type=float, default =0., help='initial value of the sde ' )
    parser.add_argument('--repeat', '-r', type=int, default =20, help='number of paths' )
    parser.add_argument('--filename', '-f', type=str, default ='mypath.png', help='filename' )#変数をいじれる。一つ目は関数を作る時のショートカット二つ目がterminalで使えるショートカット
    args= parser.parse_args()#呼び出すショートカット


    term= args.term
    step= args.step
    init= args.init
    filename= args.filename
    num_samples= args.repeat
    filepath = os.path.join(figplace,filename)

    div=term/step#飛ぶ回数
    init=np.array([init])#初期値


    mymodel = sde.SDE_Markov(mymat=np.array([[0.]]), \
        myvar =np.array([[1.]]),myinit=np.array([1.]),myscale=1.,myterm=term,step_size=step)


    mymodel.saveFig(filepath, num_samples)









if __name__ == '__main__':
    main()
