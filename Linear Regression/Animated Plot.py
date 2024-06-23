from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

X = pd.read_csv("./Training Data/Linear_X_Train.csv").values
Y = pd.read_csv("./Training Data/Linear_Y_Train.csv").values

theta = np.load("ThetaList.npy")
T0 = theta[:, 0]
T1 = theta[:, 1]

plt.ion() ## intractive mode of matplotlib
for i in range(0, 50, 3):
    Y_ = T1[i]*X + T0

    plt.scatter(X, Y, color = 'blue')
    plt.plot(X, Y_, 'orange')
    plt.draw()
    plt.clf ## clear last object (plot)s
    plt.pause(1)
    
