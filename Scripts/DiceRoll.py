import matplotlib.pyplot as plt

Somma_dadi = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Probabilita = [ 1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

# Visualizziamo il grafico
fig, ax = plt.subplots(1, 1, figsize = (10,5))
plt.bar(Somma_dadi, Probabilita)
plt.xlabel('Somma dei lanci')
plt.ylabel('Probabilità ')
plt.title('Lancio dei Dadi')

plt.show()