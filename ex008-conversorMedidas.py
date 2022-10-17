#This program receives a measure in meters and converts to Kilometers, Hemometers, Decâmeters, Decimeters, Centimeters and Millimeters
print('\nEsse programa recebe uma medida em metros e converte para:')
print('Quilômetros, Hectômetros, Decâmetros, Decímetros, Centímetros e milímetros')
m = float(input('Digite uma medida em metros: '))
print('\n{}km = {}hm = {}dam = {}m = {}dm = {}cm = {}mm'.format(m/10**3, m/10**2, m/10, m, m*10, m*10**2, m*10**3))
