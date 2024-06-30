toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

beschikbare_toppings = [t for t, _ in toppings]  # Maak een lijst met alleen de topping namen

keuze = input(f"Kies je topping uit deze lijst: {beschikbare_toppings}\n").lower()

geselecteerde_topping = None
prijs = 0

for topping, prijs_topping in toppings:
  if topping.lower() == keuze:
    geselecteerde_topping = topping
    prijs = prijs_topping
    break

if geselecteerde_topping:
  print(f"U heeft {geselecteerde_topping} besteld. Dat kost {prijs:.2f}")
else:
  print(f"Uw keuze {keuze} zit niet in ons assortiment.")
