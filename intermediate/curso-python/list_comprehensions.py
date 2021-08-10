def run():
    # Forma sin list comprehensions
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # Usando list comprehensions
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    # print(squares)

    #Reto
    listChallenge = [i for i in range(1, 10000) if i % 36 == 0]
    # print(listChallenge)
    listChallenge2 = [i for i in range(1, 10000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]
    print(listChallenge2)

if __name__ == '__main__':
    run()