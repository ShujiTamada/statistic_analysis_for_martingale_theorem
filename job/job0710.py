import sys
sys.path.append("../src")
import SDE_class as sde
import importlib
importlib.reload(sde)
import numpy as np
from matplotlib import pyplot as plt
import util as util
importlib.reload(util)



util.simulate("unko")
