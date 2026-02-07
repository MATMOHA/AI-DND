from ai import AICharacter

def setup_party():
    print("\n--- Character Creation ---\n")
    while True:
        try:
            num_players = int(input("How many AI players do you want to create? (1–3): "))
            if 1 <= num_players <= 3:
                break
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 3.")

    party = []
    for i in range(num_players):
        print(f"\n Create Player {i+1}:")
        name = input("Name: ")
        personality = input("Describe their personality: ")
        backstory = input("Give a short backstory: ")

        capabilities = []
        print("\nEnter up to 3 abilities (press Enter to skip):")
        for j in range(3):
            ability = input(f"Ability {j+1}: ")
            if ability.strip():
                capabilities.append(ability.strip())

        character = AICharacter(name, personality, backstory, capabilities)
        party.append(character)

    print("\n Party created! Let the adventure begin.\n")
    print("Party Overview:")
    for char in party:
        print(f"• {char.name} ({char.personality}) — {len(char.capabilities)} abilities: {', '.join(char.capabilities)}")
    return party
