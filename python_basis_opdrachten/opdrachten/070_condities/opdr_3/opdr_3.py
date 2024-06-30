normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

def bepaal_leeftijdscategorie(leeftijd_in_jaren):
  for categorie, leeftijdsgrenzen in leeftijd.items():
    ondergrens, bovengrens = leeftijdsgrenzen
    if ondergrens <= leeftijd_in_jaren <= bovengrens:
      return categorie
  return None

while True:
  try:
    leeftijd_in_jaren = int(input("Geef uw leeftijd in aantal jaar: "))
    break
  except ValueError:
    print("Voer een getal in.")

leeftijdscategorie = bepaal_leeftijdscategorie(leeftijd_in_jaren)

if leeftijdscategorie is None:
  print(f"Leeftijd {leeftijd_in_jaren} jaar valt niet in een categorie.")
else:
  korting = kortings_percentages[leeftijdscategorie] / 100
  prijs_met_korting = normale_toegangsprijs * (1 - korting)

  print(f"U behoort tot de groep {leeftijdscategorie}")
  print(f"U krijgt {korting:.0f}% korting")
  print(f"U betaalt daarom {prijs_met_korting:.2f}")
