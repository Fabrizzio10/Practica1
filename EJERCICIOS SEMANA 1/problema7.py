menu= """
     Menú
     1. Suma de números
     2. Resta de números
     3. Producto de números
     4. Salir
"""
print(menu)
opción=int(input("Introduzca su opción: "))
if opción==1:
   primernumer=int(input("Digitar el primer número: "))
   segundnumer=int(input("Digitar el segundo número: "))
   print(f"La suma de los números que escogió es: {primernumer+segundnumer}")
elif opción==2:
     primernumer=int(input("Digitar el primer número: "))
     segundnumer=int(input("Digitar el segundo número: "))
     print(f"La resta de los números que escogió es: {primernumer-segundnumer}")
elif opción==3:
     primernumer=int(input("Digitar el primer número: "))
     segundnumer=int(input("Digitar el segundo número: "))
     print(f"El producto de los números que escogió es: {primernumer*segundnumer}")
elif opción==4:
     print("Espero haberte ayudado")
else :
    print("Opción invalida,no es correcta.")