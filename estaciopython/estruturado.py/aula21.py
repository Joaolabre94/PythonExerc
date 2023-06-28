
import random
import matplotlib.pyplot as plt
notas_aluno = []
random.seed(200)
random.randrange(0,11)
for notas in range(8):
    notas_aluno.append((random.randrange(0,11)))
print(notas_aluno)
print(notas_aluno[2])

x = list(range(1,9))
y = notas_aluno

plt.plot(x,y, marker='o')
plt.title('Notas')
plt.xlabel('provas')
plt.ylabel('notas')
plt.show()