montant_initial = 1000
taux_de_rendement = 10 #%
gain = montant_initial * (taux_de_rendement/100)

print (f"le montant initial est de {montant_initial}€ avec un taux  de rendement de {taux_de_rendement}")
print (f"du coup a un gain de {gain}€")
montant_initial = montant_initial + 5000
taux_de_rendement = taux_de_rendement + 2#%

gain = montant_initial * (taux_de_rendement/100)
print (f"le gain est de {gain}€ grâce à un nouvel investissement de 5000€ et un rendement de {taux_de_rendement}")

montant_initial = montant_initial * 0.9
taux_de_rendement = taux_de_rendement - 1 #%
gain = montant_initial * (taux_de_rendement/100)

print(f"la gain est de {gain}€ car un investisseur a retiré 10% du montant et on a perdu 1% de rendement")