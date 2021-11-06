""" print(type(' '))

a = 10
b = -5
c = "Hola"
d = [1,2,3]
e = (4,5,6)

print(a * 5)
print(a - b)
print(c + "Mundo")
print(c * 2)
print(c[-1])
print(c[1:])
print(d + d)
print(e[1])
print(e+(7,8,9)) """


""" numero_1 = 9
numero_2 = 3
numero_3 = 6

media = (numero_1 + numero_2 + numero_3)/3
print("La nota media es", media) """

""" nota_1 = 10
nota_2 = 7
nota_3 = 4
nota_final=((nota_1*0.15)+(nota_2*0.35)+(nota_3*0.5))
print(nota_final) """

matriz = [ 
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
]
sum_sub_matriz_1 = [matriz[0].append(sum(matriz[0]))]
sum_sub_matriz_2 = [matriz[1].append(sum(matriz[1]))]
sum_sub_matriz_3 = [matriz[2].append(sum(matriz[2]))]
sum_sub_matriz_4 = [matriz[3].append(sum(matriz[3]))]
print(matriz)