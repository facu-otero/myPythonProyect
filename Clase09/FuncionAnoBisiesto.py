def ano_bisiesto(numero):
    if (numero % 400==0 and numero % 100==0):
        return f'el año {numero} es bisiesto'
    elif (numero % 4==0 and numero% 100!=0):     
        return f'el año {numero} es bisiesto'
    elif(type(numero)!=int):
        return f'ingresar un numero por favor'
    else:
        return f'el año {numero} no es bisiesto'        


print(ano_bisiesto(4))

