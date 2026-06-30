donnees = [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8),
    (5, 10)
]

poids = 1000
vitesse = 1

entree = 12
bonne_reponse = 9

for tour in range(10000):
    for entree, bonne_reponse in donnees:
        prediction = entree * poids
        erreur = bonne_reponse - prediction

        poids = poids + erreur * entree * vitesse

print("Poids trouvé :", poids)
print("Test :", 3 * poids)
print(7 * poids)
while True:
    test = float(input("Entre un nombre ici :"))
    print(test * poids)
