import matplotlib.pyplot as plt
import time
from scipy.stats import norm

#Loi normale loc : moyenne, scale : écart type
#probabilité d'obtenirune valeur > 110
probability = 1 - norm.cdf(x=110,loc=100,scale=15)
print(probability) #

samples=norm.rvs(loc=100,scale=15,size=1000000) 
plt.hist(samples,bins=1000 ,color='blue',density=True)
plt.show()
time.sleep(1) # pause d'une seconde - En pas à pas laisser le temps de voir le graphique
