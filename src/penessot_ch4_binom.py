import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom,norm
import time

#Loi binomiale probabilité de exactement k succes en faisant n essais d'un 
#test de probabilité p. Ici d'avoir exactement 3 six secs en lançant 5 dés
probability = binom.pmf(k=3,n=5,p=1/6) #On lance 5 dés on veut exactement 3 six
print(probability) #0.03215 3,21% de chance


p1 = binom.pmf(k=4,n=4,p=1/6)
print('probabilité à chaque coup de faire un yam sec : ',p1*100,'%') #0.077% de chances
p2 = binom.pmf(k=1,n=2*2*4*12,p=p1) #2 équipes * 2 joueurs/equipe * 4 colonne * 12 lignes
print('probabilité d"un yam sec et un seul au cours d"une partie de yam à 4 : ',p2*100,'%')
#12,78% de chance
#On fait 1000 parties combien de partie avec un et un seul yam sec
samples=binom.rvs(n=2*2*4*12,p=p1,size=1000) 
plt.hist(samples,bins=np.arange(min(samples),max(samples)+2) - 0.5,color='blue',density=True)
plt.show()
time.sleep(1) # pause d'une seconde - En pas à pas laisser le temps de voir le graphique
