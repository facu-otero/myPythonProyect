# 4) Escribí un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:

cantidad=int(input("cuantos numeros queres ingresar para calcular la media aritmetica: "))

numero_media=[]
for i in range(0,cantidad,1):
    numero=int(input("ingrese un valor: "))
    numero_media.append(numero) 

media=sum(numero_media)/cantidad
print("la media aritmetica es: ",media)