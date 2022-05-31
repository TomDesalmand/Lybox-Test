def calc(array, n1, n2):
    count = 0
    if (n1 > n2 or n1 < 0 or n1 >= len(array) or n2 >= len(array)):
        return -1
    for i in range(n1, n2 + 1):
        count += array[i]
    return count

def main():
    array = [0, 1, 2, 3, 4, 5]
    n1 = 1
    n2 = 5
    print(calc(array, n1, n2))
    return 0

main()