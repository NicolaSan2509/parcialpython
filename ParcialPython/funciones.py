""" 
Contexto: Se desea analizar los datos de una población organizada en

una matriz de n filas por m columnas, donde cada celda representa la

edad de una persona. """

#Importo las validaciones 
import validaciones


def cargar_matriz_edades(n,m):
    """ 
     Vamos a dos entero n que van a ser las filas y m van a ser columnas y va a permitir cargar edades
     mayores a 0 en la matriz
    """

    matriz_edades = []  

    print("Advertencia, ingrese edades validas (numeros mayores de 0) Por favor")

    #Primer bucle que va a recorrer cada fila de la matriz 
    for i in range(n):  #aca se recorre cada fila

        fila = [] # matriz vacia

        #Segundo bucle interior que va a recorrer cada columna 
        for j in range(m):  #aca se recorre cada columna

            while True:
                
                entrada_usuario = input(f"Ingrese la edad para la posicion [{i + 1}][{j + j}] ")

                #Aca Uso la validaciones
                if validaciones.es_numero_entero(entrada_usuario):
                    numero_valido = int(entrada_usuario)    #Parceamos el numero 

                    if numero_valido > 0:   #Verificamos si el numero es mayor a 0 
                        fila.append(numero_valido)  #Agregamos el numero a fila que esta vacio
                        break
                    else:
                        print("Error: La edad debe ser un numero entero y mayor a 0.")
                else:
                    print("Error: Ingrese solo numeros enteros, No se permiten letras o cosas raras por favor")
        
        matriz_edades.append(fila) # Aca agregamos la fila a la matriz vacia para que se vayan acumulando ahi
    print("Matriz de edades cargada correctamente!!")
    return matriz_edades


#=======================================================================
#=======================================================================


def porcentaje_mayores(matriz_generada):
    """ 
    Ahora vamos a calcular del total de las personas de la matriz de edades que 
    superan los 60 anios
    """

    contador_total_de_personas = 0
    contador_personas_mayores_de_60 = 0

    # Vamos a recorer cada fila de la matriz 
    for fila in matriz_generada:

        #Ahora necesito recorrer cada una de las edades adentro de las filas 
        for edad in fila:
            contador_total_de_personas += 1     #Cada celda es una persona asi que vamos a ir tomando en 1 en 1 

            #Verificamos si la edad es mayor a 60 
            if edad > 60:
                contador_personas_mayores_de_60 += 1    #Si es mayor de 60 la contamos
    

    if contador_total_de_personas == 0: #La idea es que no se pueda dividir por 0 y devuelva false o error 
        return False
    else: 
        #Calculamos el porcentaje
        porcentaje = (contador_personas_mayores_de_60 / contador_total_de_personas) * 100
        return porcentaje


#=======================================================================
#=======================================================================

def menor_edad(matriz_edades):
    """
    Determina la edad mínima de toda la matriz sin usar la función min()
    y retorna ese valor junto con todas las posiciones (fila, columna) donde aparece.
    """
    if not matriz_edades or not matriz_edades[0]:   # Verifica si la matriz está vacía o si la primera fila está vacía
        return [] # Retorna una lista vacía si la matriz está vacía o si la primera fila está vacía

    edad_minima_encontrada = 0      # Un valor que sabemos que será superado por cualquier edad válida
    posiciones_menor_edad = []      # Lista para almacenar las posiciones de la menor edad encontrada

    # Bandera para saber si ya hicimos la inicializacion de la edad mínima
    encontrado_primer_valor = False


    # Bucle exterior para recorrer las filas de la matriz.
    # 'i' representa el índice de la fila actual empezando en 0
    for i in range(len(matriz_edades)):             # Recorre las filas
        # Bucle interior para recorrer las columnas de la fila actual.
        # 'j' representa el índice de la columna actual empezando en 0
        # Recorremos cada fila y columna de la matriz
        for j in range(len(matriz_edades[i])):      # Recorre las columnas de la fila actual
            edad_actual = matriz_edades[i][j]       # Obtenemos la edad actual en la posición [i][j]

            if not encontrado_primer_valor:                         # Si es el primer valor que encontramos
                edad_minima_encontrada = edad_actual                # inicializamos la edad mínima con el primer valor encontrado
                posiciones_menor_edad.append([i + 1, j + 1])        # guardamos la posición como lista [fila, columna]
                encontrado_primer_valor = True                      # marcamos que encontramos el primer valor

            elif edad_actual < edad_minima_encontrada:          # Si encontramos una edad menor
                edad_minima_encontrada = edad_actual            # Actualizamos la edad mínima encontrada
                # aca reiniciamos la lista de posiciones porque encontramos una nueva edad mínima
                posiciones_menor_edad = [[i + 1, j + 1]]        # Reiniciamos la lista con la nueva posición
                
            elif edad_actual == edad_minima_encontrada:         # Si encontramos una edad igual a la mínima actual
                posiciones_menor_edad.append([i + 1, j + 1])    # Agregamos la posición a la lista

            else:
                continue # Si la edad actual es mayor, no hacemos nada

    return edad_minima_encontrada, posiciones_menor_edad
    

def buscar_edad(matriz_edades, edad_buscada):
    """
    Recibe una matriz y una edad determinada, y retorna todas las posiciones
    (fila, columna) donde aparece esa edad exacta.
    """
    posiciones_encontradas = []     # Lista para almacenar las posiciones donde se encuentra la edad buscada

    # Recorremos la matriz completa
    for i in range(len(matriz_edades)): # Iteramos sobre las filas
        for j in range(len(matriz_edades[i])): # Iteramos sobre las columnas de cada fila

            # Verificamos si la edad en la posición actual es igual a la edad buscada
            if matriz_edades[i][j] == edad_buscada:     # Comparación directa de la edad en la matriz con la edad buscada
                # Si la edad en la posición actual coincide con la edad buscada
                # Agregamos la posición (fila, columna) a la lista
                # Sumamos 1 a i y j para que las posiciones para el usuario no vea desde 0 y empiecen en 1
                posiciones_encontradas.append([i + 1, j + 1])
    
    return posiciones_encontradas