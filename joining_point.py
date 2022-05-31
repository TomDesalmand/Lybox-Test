
from string import digits


def add_digits(number):
    total = 0
    for i in number:
        total += int(i)
    return total

def joining_point(s1, s2):
    n1 = int(s1)
    n2 = int(s2)
    if (n1 < 0 or n2 < 0):
        return -1
    while(1):
        if (n1 == n2):
            break
        n1 += add_digits(str(n1))
        n2 += add_digits(str(n2))
    return n1

def main():
    print(joining_point("480", "471"))

main()
        