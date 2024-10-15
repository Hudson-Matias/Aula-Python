import Aula107_m
import importlib

print(Aula107_m.variavel)

for i in range(10):
    importlib.reload(Aula107_m)
    print(i)

print('Fim')
