import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Importiamo i dati da GitHub
url = "https://raw.githubusercontent.com/LucaA0111/BigData/main/Docs/Correlation/ValoreAssoluto.csv"
df = pd.read_csv(url)

# Calcoliamo e mandiamo in output la correlazione di Pearson
corr, _ = pearsonr (df['X'], df['|X|'])
print('Correlazione di Pearson: %.3f' % corr)
print(df)

# Creiamo il grafico
plt.scatter(df['X'], df['|X|'])
plt.xlabel('X')
plt.ylabel('|X|')
plt.title('Valore Assoluto')

# Mandiamo in output in grafico
plt.show()