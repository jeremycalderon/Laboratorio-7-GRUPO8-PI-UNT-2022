#Escribir una función que dada una matriz de números enteros y un número objetivo,
#retorne los indices de los 2 números que sumen ese numero objetivo. Asuma que
#habrá una solución valida en el array y no se puede usar el elemento del array 2
#veces.

print('PROGRAMA DE SUMAS CON OBJETIVO')
v=input('Desea iniciar [y]/[n]: ')
numbers_list=[]

if v == 'y' :
  try:
    num=int(input('¿Cuantos números ingresará? '))
  except ValueError:
    print('No es entero')
  for x in range(num):
    numbers_list.append([0]*1) #CREANDO LA MATRIZ
  for numero in range(num):
    numbers_list[numero] = int(input(f'Escriba el {numero+1}° número entero: ')) #VALORES A LA MATRIZ 
  try:
    n=int(input('Escribe el numero entero objetivo: '))
    object=n
  except ValueError:
    print('No es entero')
   
  for first in range(len(numbers_list)):
    for second in range(len(numbers_list)):
      if numbers_list[first] != numbers_list[second] :  #CONDICION 1
        if object == numbers_list[first] + numbers_list[second] : #SUMA CONDICIONADA
          print(f'[{first} , {second}]')
          exit()                    #Para dar todas las combinaciones, solo basta quitar esta línea de código               
else:
  print('Programa finalizado')