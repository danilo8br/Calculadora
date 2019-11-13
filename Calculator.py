#Calculadora Python

import random
from time import sleep 

#  +  Adição
#  -  Subtração
#  *  Multiplicação
#  /  Divisão
#  // Divisão Inteira
# **  Exponenciação
#  %  Resto da Divisão

print('-=-' * 20)

print('Seja Bem Vindo!')
sleep(1)
print('Vamos começar!')
sleep(1)
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
operação = input('Digite a operação: ')
print('Calculando...')
sleep(3)


if operação == '+':
    print('O resultado dessa operação é {}'.format(n1 + n2))
elif operação == '-':
    print('O resultado dessa operação é {}'.format(n1 - n2))
elif operação == '*':
    print('O resultado dessa operação é {}'.format(n1 * n2))
elif operação == '/':
    print('O resultado dessa operação é {}'.format(n1 / n2))
elif operação == '**':
    print('O resultado dessa operação é {}'.format(n1 ** n2))
elif operação == '//':
    print('O resultado dessa operação é {}'.format(n1 // n2))
elif operação == '%':
    print('O resultado dessa operação é {}'.format(n1 % n2))    
else:
    print('Digite uma operação valida! ')
    

calc = input('Deseja calcular mais alguma coisa, SIM ou NÃO ? ')

if calc == 'sim':
    print('Por favor clicar na opção Run ou algum comando que execute')
else:
    print('Foi um prazer ajuda-lo ;)')

 

print('-=-' * 20)  
