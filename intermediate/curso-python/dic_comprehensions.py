import math
# from math import sqrt

def run():
    # my_dict = {}

    #dictionary comprehensions
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # print(my_dict)

    my_dict2 = {i: round(i**0.5, 2) for i in range(1, 1001)}
    # print(my_dict2)

    my_dict3 = {i: math.sqrt(i) for i in range(1, 1001)}
    print(my_dict3)

if __name__ == '__main__':
    run()