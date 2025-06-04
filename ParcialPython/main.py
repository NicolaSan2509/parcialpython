import funciones
import validaciones


def mostrar_menu():
    """ Aca mostramos el menu al usuario """
    print("### Menu Principal ###")
    print("Opcion 1. Vas a Cargar las edades")
    print("Opcion 2. Vas a Calcular el porcentaje de personas mayores a 60")
    print("Opcion 3. Vas a Encontrar la menor edad y sus posiciones")
    print("Opcion 4. Vas a Buscar una edad especifica") 
    print("Opcion 0. Salir del Programa")


matriz_poblacion = []   #Aca cargamos o vamos metiendo los resultados de la matriz cargada

while True:
    """ Vamos armar un bucle con varios bucles para que pueda mostrarse el menu y valla cargando los datos de manera progresiva """
    mostrar_menu()

    opcion = input("Ingrese una opcion ")

    match opcion:
        case "1":
            print("Has elegido 1: Cargar Matriz")

                #Primero le pedimos al usuario el numero de filas que quiere y verificamos 

            while True:
                n_filas = input("Ingrese el numero de filas que desea: ")

                if validaciones.es_numero_entero(n_filas):
                    filas = int(n_filas)
                    if filas > 0:
                        break #Salimos del bucle si es valido 
                    else:
                        print("Error: el numero de filas debe ser mayor a 0.")
                else:
                    print("Error: Ingrese un numero entero para las filas")


                #Le pedimos al usuario el numero de columnas y verificamos 
            while True:
                n_columnas = input("Ingrese el numero de columnas que desea: ")

                if validaciones.es_numero_entero(n_columnas):
                    columnas = int(n_columnas)
                    if columnas > 0:
                        break #Salimos del bucle si es valido 
                    else:
                        print("Error: el numero de columna debe ser mayor a 0.")
                else:
                    print("Error: Ingrese un numero entero para las columnas")
            
            matriz_poblacion = funciones.cargar_matriz_edades(filas , columnas)


            for fila in matriz_poblacion:
                print(fila)


        case "2":
            print("Has elegido 2: Calcular el porcentaje mayores de 60")

            if matriz_poblacion is not [] and len(matriz_poblacion) > 0:

                porcentaje_mayores_60 = funciones.porcentaje_mayores(matriz_poblacion)

                print(f"El porcentaje de personas mayores de 60 es de {porcentaje_mayores_60} % ")
            else:
                print("!!!!! Error Primero tenes que cargas las edades en la opcion 1 !!!!!")
        
        case "3":
            print("Has elegido 3: Encontrar la menor edad y sus posiciones")
            if matriz_poblacion and len(matriz_poblacion) > 0 and len(matriz_poblacion[0]) > 0:

                # modificamos la llamada a la función menor_edad
                resultado_menor_edad = funciones.menor_edad(matriz_poblacion)
                
                # Accedemos a los elementos individualmente desde la variable resultado_menor_edad
                # El primer elemento es la edad mínima, el segundo es la lista de posiciones
                edad_minima_encontrada = resultado_menor_edad[0] 
                lista_posiciones = resultado_menor_edad[1]

                if edad_minima_encontrada is not None: # Verificamos si se encontró una edad mínima y no es none 
                    print(f"La edad mínima encontrada es: {edad_minima_encontrada}")
                    print("Aparece en las siguientes posiciones (fila, columna):")
                    for pos in lista_posiciones:    # Recorremos la lista de posiciones
                        print(f"  - Fila: {pos[0]}, Columna: {pos[1]}")     # Mostramos cada posición encontrada
                else:
                    print("No se pudo determinar la edad mínima. La matriz está vacía.")
            else:
                print("!!!!! Error: Primero tenes que cargar las edades en la opcion 1 !!!!!")

        case "4": # Nuevo case para la función buscar_edad()
            print("Has elegido 4: Buscar una edad especifica")

            if matriz_poblacion and len(matriz_poblacion) > 0 and len(matriz_poblacion[0]) > 0:  # Verificamos que la matriz no esté vacía

                while True: # Bucle para validar la edad a buscar

                    # Pedimos al usuario que ingrese la edad a buscar
                    edad_busqueda = input("Ingrese la edad que desea buscar: ")
                    
                    if validaciones.es_numero_entero(edad_busqueda):    # Verificamos si la entrada es un número entero
                        # convetimos la entrada a entero y verificamos que sea mayor a 0
                        edad_a_buscar = int(edad_busqueda)
                        if edad_a_buscar > 0:
                            break # Salimos del bucle si la edad es válida
                        else:
                            print("Error: La edad a buscar debe ser un número entero y mayor a 0.")
                    else:
                        print("Error: Ingrese un número entero válido para la edad.")

                posiciones_encontradas = funciones.buscar_edad(matriz_poblacion, edad_a_buscar)

                if posiciones_encontradas: # Si la lista no está vacía, se encontró la edad
                    print(f"La edad {edad_a_buscar} se encontró en las siguientes posiciones (fila, columna):")
                    for i in posiciones_encontradas:
                        print(f"-- Fila: {i[0]}, Columna: {i[1]}-- ")  # Mostramos cada posición encontrada
                else:
                    print(f"La edad {edad_a_buscar} no se encontró en la matriz.")
            else:
                print("!!!!! Error: Primero tenes que cargar las edades en la opcion 1 para buscar !!!!!")
            


        case "0":
            print("Gracias vuelvas prontos")
            break

        case _:
            print("Opcion no valida. Por favor ingrese un numero valido entre 0 y 2")