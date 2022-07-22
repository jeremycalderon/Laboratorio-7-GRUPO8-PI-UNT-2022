#Escriba una función que permita la multiplicación de una matriz de MxN por una de NxP (no usar numpy).

                        #FUNCIONES
#Función que pide al usuario el número de filas o columnas de una matriz y devuelve dicho número
def pedir_numero_f_o_c(filas_o_columnas, primera_o_segunda):
    if filas_o_columnas=="columnas" and primera_o_segunda=="primera": print("Ingrese el número de columnas de la primera matriz (este también será el número de filas de la segunda matriz para que la multiplicación entre ellas sea posible):")
    else: print("Ingrese el número de", filas_o_columnas, "de la", primera_o_segunda, "matriz:")
    numero_f_o_c = input()
    numero_f_o_c=int(numero_f_o_c)
    while numero_f_o_c<=0:
        print("El número que ingresaste no es válido, prueba otra vez.")
        numero_f_o_c = input()
        numero_f_o_c=int(numero_f_o_c)
    return numero_f_o_c

#Función que pide al usuario los elementos de una matriz y devuelve la matriz ya creada
def crear_matriz(numero_filas, numero_columnas, primera_o_segunda):
    print("A continuación vas a ingresar los elementos de la", primera_o_segunda, "matriz:")
    i=0
    j=0
    elemento=0
    matriz = []
    while i<numero_filas:
        matriz.append([])
        while j<numero_columnas:
            print(f"Ingrese el elemento (", i+1, ",", j+1, ") de la", primera_o_segunda, "matriz:")
            elemento = input()
            elemento = float(elemento)
            matriz[i].append(elemento)
            j+=1
        i+=1
        j=0
    return matriz

#Función que multiplica una matriz de MxN por otra matriz de NxP y devuelve el resultado
def multiplicar_matrices(M, N, P, matriz1, matriz2):
    i=0
    j=0
    k=0
    elemento=0
    matriz_producto = []
    while i<M:
        matriz_producto.append([])
        while k<P:
            while j<N:
                elemento = elemento + (matriz1[i][j]*matriz2[j][k])
                j+=1
                if j==N:
                    matriz_producto[i].append(elemento)
                    k+=1
                    elemento=0
            j=0
        i+=1
        k=0
    return matriz_producto

                        #PROGRAMA
print("Este programa multiplica dos matrices.")

#Determinar las dimensiones de las matrices MxN y NxP
M = pedir_numero_f_o_c("filas", "primera")
N = pedir_numero_f_o_c("columnas", "primera")
P = pedir_numero_f_o_c("columnas", "segunda")

#Pedir al usuario los elementos de la primera matriz y crearla
matriz1 = crear_matriz(M, N, "primera")

#Pedir al usuario los elementos de la segunda matriz y crearla
matriz2 = crear_matriz(N, P, "segunda")

#Presentar las matrices a multiplicar
print("La primera matriz es:", matriz1)
print("La segunda matriz es:", matriz2)

#Presentar el resultado de la multiplicación de las matrices dadas por el usuario
print("El producto de las dos matrices indicadas es:", multiplicar_matrices(M, N, P, matriz1, matriz2))