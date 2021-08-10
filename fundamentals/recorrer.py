def run():
    nombre = input('Escribe tu nombre: ')
    for letra in nombre:
        print(letra)

    # Otro ejemplo
    frase = input('Escribe una frase: ')
    for caracter in frase:
        print(caracter.upper())

if __name__ == '__main__':
    run()