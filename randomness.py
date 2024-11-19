import random as rand
from matplotlib import pyplot as pp
import numpy as np

num = 500
mean = 0
avg = np.zeros(101)
final = []
for i in range(num):
    n = 100
    x = [0]
    step = [0]
    for j in range(n):
        x.append(x[-1]+rand.randint(-1,1))
        step.append(j)
        avg[j+1] += x[j+1]**2
    pp.plot(step,x)
    final.append(x[-1])

for i in range(len(final)):
    mean += final[i]
    

mean = mean/num
print(mean)
avg = avg/num

#pp.plot(step,avg)
pp.xlabel('step count')
pp.ylabel('position')
pp.show()