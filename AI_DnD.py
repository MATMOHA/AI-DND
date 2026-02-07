import random
from ai import AICharacter
from cc import setup_party

def roll_dice(sides=20):
    result = random.randint(1, sides)
    print(f"\n DM rolled a d{sides}: {result}\n")
    return result

def run_game():
    print("Welcome to AI Dungeons & Dragons!\n")
    input("Press ENTER to begin character creation...")
    party = setup_party()

    print("\nYour AI party is ready!")
    print("0 = DM describes scene | 1–3 = Players respond | D = Roll dice | E = End session\n")

    dm_text = ""
    ai_history = [""] * len(party)

    while True:
        print("\n--- Turn Menu ---")
        for i, char in enumerate(party, 1):
            print(f"{i}. {char.name} speaks")
        print("0. DM describes event")
        print("D. Roll d20")
        print("E. End session")

        choice = input("\nWho acts next? (0–3, D, E): ").strip().upper()

        # DM input
        if choice == "0":
            dm_text = input("\nDM: Describe what’s happening: ").strip()
            print(f"\n DM narrates: {dm_text}")

        # Dice roll
        elif choice == "D":
            roll_dice()

        # AI responds
        elif choice in [str(i) for i in range(1, len(party)+1)]:
            idx = int(choice) - 1
            # Collect previous AI dialogue for context
            other_texts = [ai_history[i] for i in range(len(party)) if i != idx and ai_history[i]]
            response = party[idx].respond_to_event(dm_text, other_texts)
            print(f"\n{party[idx].name}: {response}")
            ai_history[idx] = response

        # End session
        elif choice == "E":
            print("\nGame session ended. Until next time, adventurer!")
            break

        else:
            print("Invalid input, try again.")

if __name__ == "__main__":
    run_game()
