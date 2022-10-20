#make a program that reads the width and height of a wall, in meters, and calculates its area and the amount of paint
#needed to paint it, knowing that each liter of paint paints an area of 2 m^2.
print('\nEsse programa pede a altura e largura de uma parede e informa a sua área e quantas litros de tinta', end='')
print(' são necessários para pintar essa parede,\n(considerando que 1l de tinta rende 2m^2)')
altura = float(input('Qual a altura da parede, em metros? '))
largura = float(input('Qual a largura da parede, em metros? '))
print('\nA área da parede é {}m^2, potanto é necessário {}l de tinta'.format(altura*largura, altura*largura/2))