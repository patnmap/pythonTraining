age = float(input("Saisissez votre age\n"))
poids = float(input("Saisissez votre poids en kg\n"))
taille = float(input("Saisissez votre taille en cm\n"))
sexe = int(input("Quel est votre sexe ?\n 1. Homme\n 2. Femme\n"))

if sexe == 1:
    brm = 66 + (13.7 * poids) + (5 * taille) - (6.8 * age)
elif sexe == 2:
    brm = 655 + (9.6 * poids) + (1.7 * taille) - (4.7 * age)

level = int(input("Quel est votre niveau d'activité ?\n1. Sédentaire\n2. Très faible activité\n3. Activité légère\n4. Activité modérée\n5. Haute activité\n6. Activité extrême\n"))
if level == 1:
    brma = brm
elif level == 2:
    brma = brm * 1.2
elif level == 3:
    brma = brm * 1.4
elif level == 4:
    brma = brm * 1.6
elif level == 5:
    brma = brm * 1.8
elif level == 6:
    brma = brm * 2

souhait = int(input("Vous voulez ?\n1. Maigrir\n2. Grossir\n"))
if souhait == 1:
    res = brma + brma * 0.1
    print("Votre nombre de calories par jour pour maigrir est ",res)
elif souhait == 2:
    res = brma - brma * 0.1
    print("Votre nombre de calories par jour pour grossir est ",res)