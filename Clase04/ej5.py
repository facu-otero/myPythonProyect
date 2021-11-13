# 5) Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
# 🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)

numero=int(input("ingresar un numero entero de 0 a 9: "))
numeros = [1, 3, 6, 9]


while (numero<0) or (numero>9):
    
    print("ingresaste un numero incorrecto, por favor reingresar")
    numero=int(input("ingresar un numero entero de 0 a 9: "))

print("el numero {} es correcto" .format(numero))

if numero in numeros:
    print("el numero esta en la lista: ",numeros)