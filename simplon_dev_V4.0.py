salle=[[0 for j in range(9)] for i in range(8)]
chk=0        
while chk<=9:
    while True:
        try:
            p = int(input("Bonjour, combien de place souhaitez vous reservez ? (max 9): \n"))
            if p<1 or p>9:
                raise ValueError
            break
        except ValueError:
            print ("mauvaise valeur saisie, merci de choisir une valeur entre 1 à 9")
            continue
    while True:
        try:
            r = int(input("Dans quel rangee souhaitez vous placez ? (1 à 8): \n"))
            if r<1 or r>8:
                raise ValueError
            break
        except ValueError:
            print ("mauvaise valeur saisie, merci de choisir une valeur entre 1 à 8")
            continue
    rm=r-1
    s = sum(salle[rm])
    chk=p+s
    if chk>9:
        print(f"il n'y a pas assez de place dans la rangée {r}")
    else:
        while s<chk:
            if salle[rm][s]==0:
                salle[rm][s]=1
                s = sum(salle[rm])
        print(" 1   2   3   4   5   6   7   8   9 ")
        for row in salle:
            for elem in row:
                print(f"[{elem}]", end=' ')
            print()
input('\nAppuyer sur entrée pour quitter...')
