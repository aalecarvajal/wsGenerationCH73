def eliminar_duplicados(arr): #función para eliminar duplicados de una lista
 
    vistos = set() #variable para almacenar los elementos ya vistos
    unicos = [] #variable para almacenar los elementos únicos
    for elemento in arr: #iterar sobre cada elemento de la lista
        if elemento not in vistos: #si el elemento no ha sido visto antes
            vistos.add(elemento) # marcar el elemento como visto
            unicos.append(elemento) # agregar el elemento a la lista de elementos únicos
    return unicos # devolver la lista de elementos únicos


# --- Pruebas ---
pruebas = [
    ([1, 2, 2, 3, 4, 4, 5], [1, 2, 3, 4, 5]),           # caso normal
    ([], []),                                            # lista vacía
    ([7], [7]),                                          # un solo elemento
    ([3, 3, 3, 3], [3]),                                 # todos iguales
    ([1, 2, 3], [1, 2, 3]),                              # sin duplicados
    (["a", "b", "a", "c", "b"], ["a", "b", "c"]),        # strings
    ([1, "1", 1.0, True], [1, "1"]),                     # tipos mezclados
    ([None, None, 0, 0], [None, 0]),                     # None y ceros
    ([-1, 1, -1, 0, 0], [-1, 1, 0]),                     # negativos
]

for entrada, esperado in pruebas: # iterar sobre cada prueba
    resultado = eliminar_duplicados(entrada) # llamar a la función con la entrada de prueba
    estado = "OK" if resultado == esperado else "FALLO" # determinar si el resultado es correcto    
    print(f"{estado} | {entrada} -> {resultado}") # imprimir el estado de la prueba, la entrada y el resultado