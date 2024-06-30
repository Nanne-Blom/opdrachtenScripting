# Maak een lege lijst
steden = []

# Vraag de gebruiker om 5 steden in te vullen
for i in range(5):
    stad = input("Voer een stad in: ")
    steden.append(stad)

# Sorteer de lijst in omgekeerde volgorde
steden.sort(reverse=True)

# Print de lijst
print(steden)