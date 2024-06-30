def write_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text + "\n")

# Voorbeeld van het gebruik van de functie
my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)

# Voeg nog een voorbeeld toe om te laten zien dat het wordt toegevoegd
another_text = "Voeg deze tekst ook toe"
write_to_file(my_file, another_text)
