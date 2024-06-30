def get_party_info():
    questions = [
        "Wat is je voornaam?",
        "Wat is je achternaam?",
        "Wat neem je mee aan drank?",
        "Wat neem je mee om te eten?"
    ]

    guest_info = {}

    for i, question in enumerate(questions, 1):
        print(f"{i}. {question}")
        answer = input()
        if i == 1:
            guest_info['voornaam'] = answer
        elif i == 2:
            guest_info['achternaam'] = answer
        elif i == 3:
            guest_info['drank'] = answer
        elif i == 4:
            guest_info['eten'] = answer

    print("\nBedankt voor het invullen!")
    print("Zie je op het feest.\n")

    return guest_info

def save_to_file(guest_info, filename="feestje.txt"):
    with open(filename, 'a') as file:
        file.write("----\n")
        for key, value in guest_info.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")

if __name__ == "__main__":
    guest_info = get_party_info()
    save_to_file(guest_info)
