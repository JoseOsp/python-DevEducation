# Preguntamos edad y decimos si es mayor de edad o menor de edad
edad = int(input('Escribe tu edad: '))

# Condicional --> if
# Usamos pass para decir que luego escribiremos algo
# Siempre despues de : hay 4 espacios esto hace referencia a la identación
if edad > 17:
    print('Eres mayor de edad')
    pass
else:
    print('Eres menor de edad')


#Otro ejemplo
numero = int(input('Escribe un número: '))

if numero > 5:
    print('Es mayor a 5')
elif numero == 5:
    print('Es igual a 5')
else:
    print('Es menor a 5')