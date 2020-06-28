import matplotlib.pyplot as plt
import numpy as np

score = np.loadtxt(open("/home/xulong/snowstorm/pysot_pytorch/results/score_fig/elephant.csv","rb"),delimiter=",",skiprows=0)
# data = np.loadtxt(open("C:\\Users\\DZF\\Desktop\\girl.csv","rb"),delimiter=",",skiprows=0)

x = np.linspace(1, len(score), len(score))
y = score

plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y, color='red', linewidth=1, linestyle='--')
plt.show()

