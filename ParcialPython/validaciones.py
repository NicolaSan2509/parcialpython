

def es_numero_entero(valor):
    """ 
    Verificamos si el numero es un entero o un valor, osea una validacion
    """
    if type(valor) == int:  #Aca verificamos la entrada de un numero
        return True
    if type(valor) == str and valor.isdigit(): #Aca verificamos la entrada de un input
        return True
    return False    # si no cumple ninguna de las verificaciones va a devolver false y rechaza la futura verificacion