
from string import digits
from traceback import print_tb


def add_digits(number):
    total = 0
    for i in number:
        total += int(i)
    return total

def is_in_list(number, number_list):
    for i in number_list:
        if (number == i):
            return 0
    return -1

def joining_point(s1, s2):
    n1 = int(s1)
    n2 = int(s2)
    n1_list = []
    n2_list = []
    if (n1 < 0 or n2 < 0):
        return -1
    while(1):
        if (is_in_list(n1, n2_list) == 0):
            return n1
        if (is_in_list(n2, n1_list) == 0):
            return n2
        n1 += add_digits(str(n1))
        n2 += add_digits(str(n2))
        n1_list.append(n1)
        n2_list.append(n2)

def main():
    print(joining_point("480", "471"))
    print(joining_point("471", "492"))
    print(joining_point("480", "483"))

main()
        