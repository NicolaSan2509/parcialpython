import funciones
import validaciones


def mostrar_menu():
    """ Aca mostramos el menu al usuario """
    print("### Menu Principal ###")
    print("Opcion 1. Vas a Cargar las edades")
    print("Opcion 2. Vas a Calcular el porcentaje de personas mayores a 60")
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

        case "0":
            print("Gracias vuelvas prontos")
            break

        case _:
            print("Opcion no valida. Por favor ingrese un numero valido entre 0 y 2")