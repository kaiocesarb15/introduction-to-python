#This program should sort anything typed
print('\nEsse programa deve classificar qualquer coisa digitada')
x = input('Digite qualquer coisa: ')
print('\nÉ um numero?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('Só tem espaços?', x.isspace())
print('É alfanumérico?', x.isalnum())
print('Esta em maiúsculo?', x.isupper())
print('Esta em minúsculo?', x.islower())
print('Esta em maiúsculo e minúsculo?', x.istitle())

