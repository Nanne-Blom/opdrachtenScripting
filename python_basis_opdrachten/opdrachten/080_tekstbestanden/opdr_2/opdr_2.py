import random

def raad_een_nummertje():
    geheim_getal = random.randint(1, 100)
    aantal_pogingen = 0
    geraden = False

    print("Raad mijn geheime getal")

    while not geraden:
        try:
            gok = int(input())
            aantal_pogingen += 1
            
            if gok < geheim_getal:
                print("hoger")
            elif gok > geheim_getal:
                print("lager")
            else:
                geraden = True
                print(f"Je hebt het getal geraden het is {geheim_getal}!")
                print(f"Je hebt het in {aantal_pogingen} keer gedaan")
        except ValueError:
            print("Voer een geldig getal in tussen de 1 en 100.")

if __name__ == "__main__":
    raad_een_nummertje()
