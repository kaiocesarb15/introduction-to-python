#This program transforms Real(R$) into:
#Dollar($), considering $1 = R$5.29
#Euro(€), considering €1 = R$5.14
#Pound(£), considering £1 = R$5.87
print('\nEsse programa transforma Real(R$) em:')
print('\tDolar($), considerando 1$ = R$5.29')
print('\tEuro(€), considerando 1€ = R$5.14')
print('\tLibra(£), considerando 1£ = R$5.87')
valor = float(input('Quantos Reais você tem? R$'))
print('\nVocê pode comprar {:.2f} dolares'.format(valor/5.29))
print('Você pode comprar {:.2f} Euros'.format(valor/5.14))
print('Você pode comprar {:.2f} Libras'.format(valor/5.87))
