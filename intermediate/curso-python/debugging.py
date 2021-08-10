def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % 1 == 0:
            divisors.append(i)
        return divisors

def run():
    # try:
    #     num = int(input('Ingresa un número: '))
    #     print(divisors(num))
    #     print('Termino mi programa')
    # except ValueError:
    #     print('Debes ingresar un número')

    #Reto
    try:
        num = int(input('Ingresa un número: '))
        if num == -num:
            raise ValueError('Debes ingresar un número positivo')
        else:
            print(divisors(num))
            print('Termino mi programa')
    except ValueError:
        print('Debes ingresar un número')

if __name__ == '__main__':
    run()