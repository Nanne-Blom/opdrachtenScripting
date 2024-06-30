# Maak een lege list
personen = []

# Maak 4 dictionaries met persoonsgegevens
persoon1 = {"id": 1, "voornaam": "Jan", "achternaam": "de Vries"}
persoon2 = {"id": 2, "voornaam": "Piet", "achternaam": "Pietersen"}
persoon3 = {"id": 3, "voornaam": "Kees", "achternaam": "Bakker"}
persoon4 = {"id": 4, "voornaam": "Truus", "achternaam": "Visser"}

# Voeg de dictionaries toe aan de list met de append()-methode
personen.append(persoon1)
personen.append(persoon2)
personen.append(persoon3)
personen.append(persoon4)

# Druk de volledige naam van de 2e persoon af
print(f"{personen[1]['voornaam']} {personen[1]['achternaam']}")
