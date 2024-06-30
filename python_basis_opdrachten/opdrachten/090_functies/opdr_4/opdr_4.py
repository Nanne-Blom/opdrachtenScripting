def volledige_naam(lijst_met_namen):
    for naam in lijst_met_namen:
        volledige_naam = naam['voornaam']
        if naam['tussenvoegsel']:
            volledige_naam += f" {naam['tussenvoegsel']}"
        volledige_naam += f" {naam['achternaam']}"
        print(volledige_naam)

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)
