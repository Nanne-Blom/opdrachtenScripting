
import os

def stel_vraag(vraag):
  """
  Stelt de vraag en retourneert het antwoord van de gebruiker.

  Args:
      vraag (str): De vraag die aan de gebruiker wordt gesteld.

  Returns:
      str: Het antwoord van de gebruiker.
  """
  antwoord = input(f"{vraag}: ")
  return antwoord

def sla_op(antwoorden):
  """
  Slaat de antwoorden op in een tekstbestand.

  Args:
      antwoorden (dict): De antwoorden van de gebruiker.
  """
  with open("enquete_uitslagen.txt", "a", encoding="utf-8") as bestand:
    bestand.write(f"\n--- Nieuwe enquete ---\n")
    for vraag, antwoord in antwoorden.items():
      bestand.write(f"{vraag}: {antwoord}\n")

vragen = {
    "Wat vind je van de huidige regering?": "",
    "Wat vind je van de Python-lessen tot nu toe?": "",
    "Wat vind jij de mooiste stad van Nederland?": "",
}

for vraag, antwoord in vragen.items():
  vragen[vraag] = stel_vraag(vraag)

sla_op(vragen)

print("\nBedankt voor het invullen van de enquete!")
