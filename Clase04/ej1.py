# 1) Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
# En caso de no introducir una opción válida, el programa informará de que no es correcta.

numero_1 = int(input("inserta el numero 1: "))
numero_2 = int(input("inserta el numero 2: "))
opcion = int(input("Elige la opcion deseada: (1) para suma (2) para resta (3) para multiplicacion (4)para finalizar: "))

if (opcion ==1):
    print(numero_1+numero_2)
elif(opcion ==2):
    print(numero_1-numero_2)
elif(opcion ==3):
    print(numero_1*numero_2)
elif(opcion ==4):
    print("el progama finalizó")
elif(opcion>4):
    print("opcion incorrecta")
