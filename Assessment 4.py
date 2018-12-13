import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
import statistics
import scipy
from scipy.stats import ks_2samp

idnum = 201386288

seed=(idnum+9123)

Z=95+rand(995)*300
X=rand(200)*rand()*9
Y=(randn(130)+2)*rand()*8
Xu='m'
if rand()<0.5 : Xu='cm'
Yu='m'
if rand()<0.3:Yu='cg'

print('Units\n X: ',Xu,'\n Y: ',Yu,'\n W: kg \n Z: hours')

print(idnum) # Q3
print(sum(X)) # Q4
print(len(X)) # Q5
print(Xu) # Q6
print(len(Y)) # Q7
print(Yu) # Q8

plt.figure()
plt.boxplot(X, 0, 'gD') # Q9, Plots a box and whisker graph with green dots as outliers

X.sort()
print(statistics.median(X)) # Q10
print(Xu) # Q11
print(scipy.stats.variation(X)) # Q12

#print(np.polyfit(X,Y,1)) # Q14, 15
print(ks_2samp(X, Y)) # Q16, 17
print(scipy.stats.mannwhitneyu(X, Y)) # Q18, 19

# SECTION 2 #

print(len(Z)) # Q21
defect_rate = sum(i < 100 for i in Z)
print(defect_rate) # Q22
prob_bad = defect_rate / len(Z)
print(prob_bad) # Q23
prob_good = 1 - prob_bad
print(prob_good) # Q24
print(prob_good * prob_good) # Q25