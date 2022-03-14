# BP - EX: 12.2

def tri(tab):
    '''
        tab [list]: liste des 1 et 0 non triée

        Renvoie tab triée
    '''
    i= 0
    j= len(tab)-1
    while i != j :
        if tab[i]== 0: i+=1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j= j-1
    return tab

# ----------------------------------------------------------------

print(tri([0,1,0,1,0,1,0,1,0]))
# ! returns [0, 0, 0, 0, 0, 1, 1, 1, 1]

# * Finished! 🎉