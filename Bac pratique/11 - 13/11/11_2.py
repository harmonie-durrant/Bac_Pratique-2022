# BP - EX: 11.2

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

def position_alphabet(lettre):
    '''
        lettre [int]: une indice
    
        Renvoie la lettre a l'indice lettre
    '''
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    '''
        message [str]: une chaîne de charactères
        decalage [int]: décalage indice alphabet

        Renvoie la phrase avec les lettres decallée
    '''
    resultat = ''
    for lettre in message :
        if lettre in ALPHABET :
            indice = ( position_alphabet(lettre)+decalage )%26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + lettre
    return resultat

# ----------------------------------------------------------------

print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))
# ! Returns 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'

print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5))
# ! Returns 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'

# * Finished! 🎉