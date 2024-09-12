"""
Entendo os seus próprios módulo Python
O primeiro módulo executado chama-se __main__
Você pode importar outro módulo inteiro ou parte do módulo
O python conhece a pasta onde o __main__ está e as pastas
abaixo dele.
Ele não reconhece pastas e módulos acima do __main__ por padrão
O Python conhece todos os módulos e pacotes presentes nos caminhos
de sys.path
"""
import sys

import Aula106_m

print(*sys.path, sep='\n')
print('Este módulo se chama ', __name__)
