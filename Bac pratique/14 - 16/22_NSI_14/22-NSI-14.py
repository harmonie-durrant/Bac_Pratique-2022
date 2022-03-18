
def correspond(mot, mot_a_trous):
    if mot == mot_a_trous:
        return True
    if len(mot) != len(mot_a_trous):
        return False
    for i in range(len(mot_a_trous)):
        if mot_a_trous[i] != mot[i]:
            if mot_a_trous[i] != '*':
                return False
    return True

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))

print(correspond('IUTOMATIQUE', 'INFO*MA*IQUE'))



def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant 
    à un plan d'envoi de messages entre `N` personnes A, B, C, 
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon. 
    '''
    personne = 'A'
    N = len(plan)
    for i in range(N-1):
        if plan[personne] == 'A':
            return False
        else:
            personne = plan[personne]
    return True

print(est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'})) 
print(est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'})) 
print(est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F', 'D':'E'})) 
print(est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'}))