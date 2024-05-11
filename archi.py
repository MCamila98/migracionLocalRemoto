numero = int(input('Ingrese el número del cual quiere obtener la tabla de multiplicar => '))
for factor in range(10):
  print(f'{numero} X {factor} = {factor*numero}')