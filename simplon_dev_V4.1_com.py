#definir la salle cinema en liste 2 dimension 
salle=[[0 for j in range(9)] for i in range(8)]
# la variable chk correspond a la somme des places reservées et celles souhaitées
chk=0
#on redemande a l'utilisateur une nouvelle saisie tanqu'il y'a assez de place disponible pour sa demande 
while chk<=9:
    #la variable p c'est le nombre de place demandée par l'utilisateur et on verifie que la valeur saisie du p est correct 
    while True:
        try:
            p = int(input("Bonjour, combien de place souhaitez vous reservez ? (max 9): \n"))
            if p<1 or p>9:
                raise ValueError
            break
        except ValueError:
            print ("mauvaise valeur saisie, merci de choisir une valeur entre 1 à 9")
            continue
    #la variable r c'est rangée choisi par l'utilisateur et on verifie que la valeur saisie du r est correct
    while True:
        try:
            r = int(input("Dans quel rangee souhaitez vous placez ? (1 à 8): \n"))
            if r<1 or r>8:
                raise ValueError
            break
        except ValueError:
            print ("mauvaise valeur saisie, merci de choisir une valeur entre 1 à 8")
            continue
    #on corrige la valeur de la rangée pour corrrespondre à l'index de la liste
    rm=r-1
    #la variable s correspond aux places resérvées
    s = sum(salle[rm])
    chk=p+s
    #on vérifie s'il y a asser de place pour que l'utilisateur les reserves
    if chk>9:
        print(f"il n'y a pas assez de place dans la rangée {r}")
    else:
        # on rempli la rangée choisie avec le nombre de place souhaitées
        while s<chk:
            if salle[rm][s]==0:
                salle[rm][s]=1
                s = sum(salle[rm])
        #On affiche la salle de cinéma
        print(" 1   2   3   4   5   6   7   8   9 ")
        for row in salle:
            for elem in row:
                print(f"[{elem}]", end=' ')
            print()
input('\nAppuyer sur entrée pour quitter...')
