print('Introducir un número entero postivo')
numero= int(input())
n=numero
if n>0:
   sumatoria=int(n*(n+1)/2)
   print('La sumatoria hasta el número introducido es: '+ str(sumatoria))
else :
   print("El numero introducido no es un entero positivo")