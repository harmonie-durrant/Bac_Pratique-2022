def recherche(char, mot):
    occ = 0
    for lettre in mot:
        if lettre == char:
            occ += 1
    return occ

print(recherche('e', "sciences"))
print(recherche('i', "mississippi"))
print(recherche('a', "mississippi"))