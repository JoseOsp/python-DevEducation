# Imprimir los numeros del 1 al 1000
# Ejemplo con el ciclo while
contador = 1
print(contador)
while contador < 1000:
    # Forma 1 de aumentar el contador
    # contador = contador + 1
    # Forma 2 de aumentar el contador
    contador += 1
    print(contador)

# Un ejemplo de como convertimos un rango en lista
a = list(range(1000))
print(a)

# Ejemplo con ciclo for
for contador in range(1, 1001):
    print(contador)

# Otro ejemplo
for i in range(10):
    print(11 * i)