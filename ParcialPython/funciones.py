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



        





