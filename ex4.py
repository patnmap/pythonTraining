def jourAnnee(Jours, Mois, Nbr_j):
    année = []
    x = 4
    for y in range(12):
        for i in range(1,Nbr_j[0] + 1):
            res = (i, Jours[x], Mois[y])
            x = x + 1
            if x > 6:
                x = 0
            année.append(res) 
    return année

def determinationJour(month, number, an):
    for j, m, n in an:
        if (m == month and n == number):
            return j
        else:
            False

Jours = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
Mois = ['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre']
Nbr_j = [31,28,31,30,31,30,31,31,30,31,30,31]
an = jourAnnee(Jours, Mois, Nbr_j)

for j, m, n in an:
    print(m, j, n)
test = determinationJour('Fevrier', '14', an)
print(test)