import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import DBSCAN
import h5py
import time
from IPython import get_ipython
import mplcursors
from math import cos, sin, pi
from scipy.optimize import least_squares
import warnings
warnings.filterwarnings("ignore")

W = 346
H = 260

h5f = h5py.File('/home/ahmed/Downloads/davis_slow.h5', 'r')
events = h5f['events_data'][:]
h5f.close()

events[:,3] = (events[:,3] - events[0,3])

with open("davis_fast.txt", "w") as f:
    for event in events:
        f.write(str(int(event[3]*1e9))+" "+str(event[0])+" "+str(event[1])+" "+str(int(event[2]))+" ")