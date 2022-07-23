#Escriba una función para transformar números arábigos a números romanos. El número ingresado debe ser menor a 4000.
                        #FUNCIÓN
#Función que convierte un número arábigo menor que 4000 a números romanos
def convertir_a_romanos(numero):
    numero_string = list(str(numero))
    cantidad_cifras_numero = len(numero_string)
    romanos = []
    #Conversión de los millares si los hubiera
    if cantidad_cifras_numero==4:
        millares = int(numero_string[0])
        while millares>0:
            romanos.append("M")
            millares-=1
    #Conversión de las centenas si las hubiera
    if cantidad_cifras_numero==3 or cantidad_cifras_numero==4:
        if cantidad_cifras_numero==3: centenas = int(numero_string[0])
        if cantidad_cifras_numero==4: centenas = int(numero_string[1])
        if centenas<4:
            while centenas>0:
                romanos.append("C")
                centenas-=1
        elif centenas==4:
            romanos.append("C")
            romanos.append("D")
        elif centenas<9:
            romanos.append("D")
            while centenas>5:
                romanos.append("C")
                centenas-=1
        elif centenas==9:
            romanos.append("C")
            romanos.append("M")
    #Conversión de las decenas si las hubiera
    if cantidad_cifras_numero==2 or cantidad_cifras_numero==3 or cantidad_cifras_numero==4:
        if cantidad_cifras_numero==2: decenas = int(numero_string[0])
        if cantidad_cifras_numero==3: decenas = int(numero_string[1])
        if cantidad_cifras_numero==4: decenas = int(numero_string[2])
        if decenas<4:
            while decenas>0:
                romanos.append("X")
                decenas-=1
        elif decenas==4:
            romanos.append("X")
            romanos.append("L")
        elif decenas<9:
            romanos.append("L")
            while decenas>5:
                romanos.append("X")
                decenas-=1
        elif decenas==9:
            romanos.append("X")
            romanos.append("C")
    #Conversión de las unidades
    if cantidad_cifras_numero==1: unidades = int(numero_string[0])
    if cantidad_cifras_numero==2: unidades = int(numero_string[1])
    if cantidad_cifras_numero==3: unidades = int(numero_string[2])
    if cantidad_cifras_numero==4: unidades = int(numero_string[3])
    if unidades<4:
        while unidades>0:
            romanos.append("I")
            unidades-=1
    elif unidades==4:
        romanos.append("I")
        romanos.append("V")
    elif unidades<9:
        romanos.append("V")
        while unidades>5:
            romanos.append("I")
            unidades-=1
    elif unidades==9:
        romanos.append("I")
        romanos.append("X")
    
    return romanos

                        #PROGRAMA
#Obtener el número en arábigo a convertir a números romanos
print("Ingrese un número entero mayor que 0 y menor que 4000: ")
numero = input()
numero = int(numero)
while numero<1 or numero>3999:
    print("El número que ingresaste no es un entero mayor que 0 y menor que 4000, vuelve a intentarlo.")
    numero = input()
    numero = int(numero)

#Convertir el número arábigo dado a números romanos
romanos = convertir_a_romanos(numero)

#Presentar del resultado al usuario
print("El número que ingresaste es", numero, "y ese número expresado en números romanos es:", "".join(romanos))