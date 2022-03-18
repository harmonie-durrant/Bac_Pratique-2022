P = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(arendre, s=[], i=0):
    if arendre == 0:
        return s
    p = P[i]
    if p <= arendre:
        s.append(p)
        return rendu_glouton(arendre - p, s, i)
    else:
        return rendu_glouton(arendre, s, i+1)

print(rendu_glouton(68, [], 0))
print(rendu_glouton(291, [], 0))