def palindromo(palabra):
    #Eliminamos los espacios -.-
    palabra = palabra.replace(' ','')
    #Pasamos la labra a minusculas
    palabra = palabra.lower()
    #Invertimos la palabra -.-
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()