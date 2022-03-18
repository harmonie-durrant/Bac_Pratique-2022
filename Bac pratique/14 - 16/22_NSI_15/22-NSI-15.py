def nb_repetitions(elt, tab):
    rep = 0
    for i in range(len(tab)):
        if tab[i] == elt:
            rep += 1
    return rep  

print(nb_repetitions(5,[2,5,3,5,6,9,5]))
print(nb_repetitions('A',[ 'B', 'A', 'B', 'A', 'R']))
print(nb_repetitions(12,[1, '! ',7,21,36,44]))

def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a > 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a

print(binaire(0))
print(binaire(77))