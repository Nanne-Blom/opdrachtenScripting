# Opdracht 3 tekstfuncties
# Naam student: Nanne
# Groep:SIT1A

# Hier komt je code...
for i in range(5):
  # Kerstboom met hoogte 5
  for j in range(5):
    # Aantal sterren per regel berekenen
    aantal_sterren = 2 * j + 1
    print(" " * (5 - j) + "*" * aantal_sterren)

  # Stam van de boom
  print("    ***")

print()
