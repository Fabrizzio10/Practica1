print('BIENVENIDO A "KINGPLAY"')
print("¿Cúal es su edad?")
edad=int(input())
if edad>= 4 and edad<= 18:
    print("El precio de su entrada es: $5")
elif edad>18:
    print("El precio de su entrada es: $10")
else :
    print("Puedes entrar gratis :)")