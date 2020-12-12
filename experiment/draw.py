import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

names = ['blackscholes','bodytrack', 'facesim', 'fluidanimate', 'freqmine', 'swaptions', 'x264']
fig = plt.figure()
fig.subplots_adjust(left=0.05,right=0.95,bottom=0.07,top=0.93,wspace=0.1,hspace=0.15)
plt.axis('off')

data = pd.read_csv('speedup.csv',header=None)
data.drop([7],axis=1,inplace=True)
# print(data)
i = 1
width = 0.21
threads = ['1', '2', '4', '8', '16', '32']
index = np.arange(len(threads))
count = 0
for name in names:
    num = 240 + i
    i += 1
    fig.add_subplot(num)
    plt.title(name, fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    # empty = [0,0,0,0,0,[0
    for j in range(1, 8):
        line = data.loc[[count * 8 + j]].values
        name = line[0][0]
        var = line[0][1:]
        plt.plot(index, var, label=name)
    if i > 5:
        plt.xlabel('threads', fontsize=18)
    if i == 2 or i == 6:
        plt.ylabel('speed up', fontsize=18)
    if i == 7:
        plt.legend(fontsize=14)
    count += 1

plt.show()

