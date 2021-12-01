cadena = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"

# print(cadena)
# nueva_cadena = cadena.replace("&","\n- ",4)

# nueva_cadena_2=nueva_cadena.capitalize()
# print(nueva_cadena_2)
nueva_cadena = cadena.split("&")
for i,linea in enumerate(nueva_cadena):
    nueva_cadena[i]= linea.capitalize()
    if(i==0):
        nueva_cadena[i] = nueva_cadena[i] + "..."
    else:
        nueva_cadena[i] = "- " + nueva_cadena[i] + "."
    
    print(nueva_cadena[i])