#This program asks for an integer and shows its double, triple and its square root
print('\nEsse programa pede um número inteiro e mostra seu dobro, triplo e sua raiz quadrada')
numero = int(input('Digite um número: '))
print('\nO dobro de {} é {}\nO triplo de {} é {}'.format(numero, numero*2, numero, numero*3))
print('A raiz quadrada de {} é {}'.format(numero, numero**(1/2)))
