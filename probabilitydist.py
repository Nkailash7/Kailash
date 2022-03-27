import numpy as np
import matplotlib.pyplot as plt
#creating a series of data 
x = np.linspace(1,50,5)
def normal_dist(x , mean , sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density


mean = np.mean(x)
sd = np.std(x)
pdf = normal_dist(x,mean,sd)
plt.plot(x,pdf , color = 'blue')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
