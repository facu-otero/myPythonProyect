# 2) Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

numero = int(input("ingrese un numero impar: "))
# print((numero%2))
while (numero%2) == 0:
    print("ingresaste un numero Par")
    numero = int(input("Por favor, ingrese un numero impar: "))

print("el numero ingresado {} es impar" .format(numero))
