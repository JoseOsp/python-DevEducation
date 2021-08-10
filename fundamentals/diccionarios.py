def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # Muestro el elemento con el nombre de la llave
    print(mi_diccionario['llave1'])
    print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3'])


    # Otro diccionario
    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    print(poblacion_paises['Argentina'])

    # Recorrer el diccionario con el ciclo for e imprimir los nombres de las llaves en el diccionario
    for pais in poblacion_paises.keys():
        print(pais)

    # Recorrer el diccionario con el ciclo for e imprimir los valores de cada llave
    for pais in poblacion_paises.values():
        print(pais)

    # Mostrar tanto valores como keys usando el metodo .items()
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
    run()