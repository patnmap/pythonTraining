import random
max = int(input("Entrez le nombre maximum "))
nombreDeBase = random.randint(1,max)
count = 0
while(True):
    print("Choisissez un nombre entre 1 et ", max)
    choice = int(input())
    if choice < nombreDeBase:
        print("C'est plus")
        count = count + 1
    if choice > nombreDeBase:
        print("C'est moins")
        count = count + 1
    if choice == nombreDeBase:
        count = count + 1
        print("Bravo vous avez réussi en ", count," coups")
        exit()
