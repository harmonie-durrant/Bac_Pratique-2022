# BP - EX: 12.1

def moyenne(tab):
    '''
        tab [list]: liste de nombres

        Renvoie la moyenne des nombres dans tab
    '''
    if tab == []:
        return 'erreur'
    sum = 0
    for i in tab:
        sum += i
    return sum//len(tab)

# ----------------------------------------------------------------

print(moyenne([5,3,8]))
# ! Reuturns 5.333333333333333

print(moyenne([1,2,3,4,5,6,7,8,9,10]))
# ! Reuturns 5.5

print(moyenne([]))
# ! returns 'erreur'

# * Finished! 🎉