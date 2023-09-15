import numpy as np
from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt

# Importiamo i dati da GitHub
url = "https://raw.githubusercontent.com/LucaA0111/BigData/main/Docs/Statistics/ProduttoriBatterie.csv"
df = pd.read_csv(url)

# Calcoliamo Media, Deviazione Standard e Distribuzione Normalizzata del produttore A e mandiamo in output le informazioni ottenute
Media_prodA = df['PRODUTTORE A'].mean()
Stan_devA = df['PRODUTTORE A'].std()
Distr_norA = np.zeros(len(df['PRODUTTORE A']))
for i in range(len(df['PRODUTTORE A'])):
  Distr_norA[i] =norm.pdf(df.iloc[i,0], loc = Media_prodA, scale = Stan_devA)

# Calcoliamo Media, Deviazione Standard e Distribuzione Normalizzata del produttore B e mandiamo in output le informazioni ottenute
Media_prodB = df['PRODUTTORE B'].mean()
Stan_devB = df['PRODUTTORE B'].std()
Distr_norB = np.zeros(len(df['PRODUTTORE B']))
for i in range(len(df['PRODUTTORE B'])):
  Distr_norB[i] = norm.pdf(df.iloc[i,1], loc = Media_prodB, scale = Stan_devB)

# Stampiamo i risultati ottenuti
print("Produttore A\n")
print("Media batterie produttore A: " + str(Media_prodA) + "\n")
print("Deviazione standard A: " + str(Stan_devA) + "\n")
print("Distribuzione normalizzata di A: " + str(Distr_norA) + "\n")
print("----------------------------------------\nProduttore B\n")
print("Media batterie produttore B: " + str(Media_prodB) + "\n")
print("Deviazione standard B: " + str(Stan_devB) + "\n")
print("Distribuzione normalizzata di B: " + str(Distr_norB) + "\n")


# Creiamo i grafici
fig, ax = plt.subplots(1, 1, figsize = (10,5))
plt.plot(df['PRODUTTORE A'], Distr_norA)
plt.title('PRODUTTORE A')
plt.xlabel('Durata Batterie')
plt.ylabel('Normalizzazione')

fig, ax = plt.subplots(1, 1, figsize = (10,5))
plt.plot(df['PRODUTTORE B'], Distr_norB)
plt.title('PRODUTTORE B')
plt.xlabel('Durata Batterie')
plt.ylabel('Normalizzazione')

plt.show()