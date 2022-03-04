def burbuja(Cantidad):
    # Calculamos la longitud de los numeros para tener un código más limpio
    longitud = len(Cantidad)
    # Recorremos todo los numeros
    for i in range(longitud):
        # Dentro del ciclo, volvemos a recorrerlo. Pero ahora hasta el penúltimo elemento
        for indice_actual in range(longitud - 1):
            indice_siguiente_elemento = indice_actual + 1
            # Si el actual es mayor que el siguiente, ...
            if Cantidad[indice_actual] > Cantidad[indice_siguiente_elemento]:
                # cambiamos los numeros
                Cantidad[indice_siguiente_elemento], Cantidad[indice_actual] = Cantidad[indice_actual], Cantidad[indice_siguiente_elemento]
    # No hace falta volver atras, pues los numeros ya fueron modificados


# Modo de uso.
numeros = [3, 4, 1, 2, 3, 7, 55, 34, 43, 3]
print("Original: ")
print(numeros)
burbuja(numeros)
print("Ordenado: ")
print(numeros)