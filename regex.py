import re

def regex(string):
    costs = []
    total = 0
    index = 0
    for i in re.split(" |,|EUR |€", string):
        if (i.isdigit() and index > string.find("m2") and string.find("/an") != -1):
            costs.append(int(i))
            break
        if (i.isdigit() and index > string.find("m2") and string.find("/an") == -1):
            costs.append(int(i) * 12)
            break
        index += 1
    for j in range(len(costs)):
        total += costs[j]
    return total

def main():
    print(regex("Loyer en cours de 430 € /mois hors charges"))
    print(regex("cet appartement au premier étage est actuellement loué 400 euros par mois"))
    print(regex("Investissement locatif T2 loué 496€/mois dont 26€ de charges."))
    print(regex("type 1 rénové de 34 m2 vendu loué en bail meublé avec un loyer de 500EUR hors charges et 20EUR de provisions sur charges"))
    print(regex("Percevez 5548 € (sans les charges) de loyer garanti/an"))
    print(regex("le loyer actuel est de 5000,00 euros/an."))

main()

