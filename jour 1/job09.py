nom = "desertheagle"
prix_unité = 329.09
quantité_stock = 32
nouveau_stock = int(input("entrer la quantité ajouté au stock = "))
somme = quantité_stock + nouveau_stock
print (somme)
nouveau_prix = float (prix_unité /0.9)
produit = nouveau_prix
print (f"l'article {nom} au prix de {produit}€ et il en reste {somme}")
