import matplotlib.pyplot as plt
import numpy as np
import time

rolls=np.random.randint(1,21,1000000) #Génère de 1 à 20, la borne supérieure est exclue
print(type(rolls))
print(np.count_nonzero(rolls == 18)) #Compte le nombre de 20
print(np.count_nonzero(rolls == 19)) #Compte le nombre de 20
print(np.count_nonzero(rolls == 20)) #Compte le nombre de 20
plt.figure(figsize=(10,6))
#plt.hist(rolls, bins=np.arange(1, 22) - 0.5, color='blue', alpha=0.7)
#bins bins=np.arange(1, 21) - Le borne supérieure est exclue. Il arrange
#les 20 valeurs entre les limites 1 et 20, ce qui ne fait que 19 colonnes et les 
#valeurs 19 et 20 sont cumulées dans la dernière, qui est deux fois plus haute
#que les autres.
#plt.hist(rolls, bins=np.arange(1, 21), color='blue', alpha=0.7)
#avec (1,22) on a bien 20 colonne, la dernière va de 20 à 21
#plt.hist(rolls, bins=np.arange(1, 22), color='blue', alpha=0.7)
#avec (1,22)-0.5 on a bien 20 colonne, elles cont centrées sur les valeurs entières
plt.hist(rolls, bins=np.arange(1, 22) - 0.5, color='blue', alpha=0.7)
#avec (1,21)-0.5 on a 19 colonnes, la valeur 20 n'apparait pas
#arange(1.21) créé des valeurs de 1 à 20 (borne sup exclue), on les ramene à 0.5-19.5
#la valeur 20 n'est plus dans la plage affiché
#plt.hist(rolls, bins=np.arange(1, 21) - 0.5, color='blue', alpha=0.7)

plt.title('Histogramme des lancers de dés d20')
plt.xlabel('Valeur du dé')
plt.ylabel('Fréquence')
plt.grid(True, alpha=0.3)
plt.xticks(np.arange(1, 21))
plt.show()
time.sleep(1) # pause d'une seconde - En pas à pas laisser le temps de voir le graphique

