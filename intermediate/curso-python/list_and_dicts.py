def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {
        'Firstname': 'Facundo',
        'lastname': 'Garcia'
    }

    #Lista que contiene diccionarios
    super_list = [
        {'Firstname': 'Facundo','lastname': 'Garcia'},
        {'Firstname': 'Miguel','lastname': 'Torres'},
        {'Firstname': 'Pepe','lastname': 'Rodelo'},
        {'Firstname': 'Susana','lastname': 'Martinez'},
        {'Firstname': 'Jose','lastname': 'Garcia'},
    ]
    #Diccionario de listas
    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'interger_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(f'{key} - {value}')

if __name__ == '__main__':
    run()