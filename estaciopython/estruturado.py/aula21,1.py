#Exercicio2 - implementar uma solução em python para visualizar dados de vendas de produtos em um gráfico de barras.
#Por exemplo, utilize os seguintes dados:
# x=['A', 'B', 'C', 'D']
# y=[3,8,1,10]
import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()