def run():
    # Para el primer ejemplo imprimiremos solo los numeros impares
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)

    # Otro ejemplo
    for i in range(10000):
        print(i)
        if i == 5678:
            break

    # Otro ejemplo recorriendo un string
    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()