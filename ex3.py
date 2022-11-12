points_lettres={"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,"K":10,"L":1,"M":2,"N":1,"O":1,"P":3,"Q":8,"R":1,"S":1,"T":1,"U":1,"V":4,"W":10,"X":10,"Y":10,"Z":10}

def comptePoints(word):
    scoreV = 0
    scoreC = 0
    for i in word:
        if i in ("AEIOUY"):
            scoreV = scoreV + points_lettres[i]
        else:
            scoreC = scoreC + points_lettres[i]
    return (scoreV, scoreC)

def nbr_Consonnes(word):
    voy = 0
    cons = 0
    for j in word:
        if j in ("AEIOUY"):
            voy = voy + 1
        else:
            cons = cons + 1
    return(voy, cons)

mot = (input("Entrez un mot\n")).upper()
print(comptePoints(mot))
print(nbr_Consonnes(mot))