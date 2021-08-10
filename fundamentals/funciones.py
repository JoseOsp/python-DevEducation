# Definimos la función
def imprimir_mensaje():
    print('Mensaje especial: ')
    print('¡Estoy aprendiendo a usar funciones')

# Invocamos la función ---> para poder usarla
imprimir_mensaje()

# Otro ejemplo ---------------------------------------->
# Usando parametros 

def conversacion(mensaje):
    print('Hola')
    print('Cómo estás')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opción (1, 2, 3): '))
if opcion == 1:
    conversacion('Elegiste la opción 1')
elif opcion == 2:
    conversacion('Elegiste la opción 2')
elif opcion == 3:
    conversacion('Elegiste la opción 3')
else:
    print('Escribe la opción correcta')

#return --> Para devolver un valor del bloque de codigo y usarlo en otro lado
def suma(a, b):
    print('Se suman dos números')
    resultado = a + b
    return resultado
sumatoria = suma(1, 4)
print(sumatoria)