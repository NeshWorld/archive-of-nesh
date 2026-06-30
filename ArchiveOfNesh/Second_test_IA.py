

def apprentissage ():
    entree = 3
    poids = 1
    reponse = entree * poids
    bonne_reponse = 6
    erreur = bonne_reponse - reponse
    vitesse = 0.1

    for i in range(100):
        poids = poids + erreur * vitesse
        print(poids)
        reponse = entree * poids
        erreur = bonne_reponse - reponse

    return poids

def multiplier_2 (user_input, poids):
    return user_input * poids

poids_appris = apprentissage()
print("poids appris :", poids_appris
user_input = int(input("Entrer un nombre"))

while True:
    try :
        user_input = int(input("Entrer un nombre :"))
        resultat = multiplier_2(user_input, poids_appris)
        print("resultat:",
              resultat)
    except:
        raise TypeError("Entrée incorrect")
    else :
        print("Entrée incorrect")
