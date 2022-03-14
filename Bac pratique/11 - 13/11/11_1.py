# BP - EX: 11.1

def recherche(tab, n):
    '''
        tab [list]: nombres entiers triés par ordre croissant
        n [int]: nombre qu'on cherche

        Renvoie un indice correspondant au nombre cherché s’il est dans le tableau, -1 sinon.
    '''
    indice, debut, fin = -1, 0, len(tab)-1
    while (debut <= fin):
        m = (debut + fin) // 2
        if tab[m] == n: return m
        elif tab[m] < n: debut = m+1
        elif tab[m] > n: fin = m - 1
    return indice

# ----------------------------------------------------------------

print(recherche([2, 3, 4, 5, 6], 5))
# ! Returns 3

print(recherche([2, 3, 4, 6, 7], 5))
# ! Returns -1

# * Finished! 🎉