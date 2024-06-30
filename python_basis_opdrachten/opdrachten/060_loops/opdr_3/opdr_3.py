# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

getallen = []
for i in range(3, 81, 3):
  kwadraat = i**2
  gedeeld_door_3 = kwadraat / 3
  getallen.append(gedeeld_door_3)

print(getallen)