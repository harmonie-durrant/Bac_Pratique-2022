# BP - EX: 13.1

def rendu(s):
    '''
        s [int]: somme a rendre

        Renvoie une liste avec le nombre de pièces à rendre
    '''
    P, pieces, i = [5, 2, 1], [0, 0, 0], 0
    while s > 0:
        if P[i] <= s:
            s -= P[i]
            pieces[i] += 1
        else: i += 1
    return pieces

# ----------------------------------------------------------------

print(rendu(13))
# ! returns [2,1,1]

print(rendu(64))
# ! returns [12,2,0]

print(rendu(89))
# ! returns [17,2,0]

# * Finished! 🎉