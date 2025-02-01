import requests

url = "https://uselessfacts.jsph.pl/random.json?language=en"
file_name = "facts.txt"

def get_random_facts():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        fact = fact_data["text"]
        print(f"\nDid you know? {fact}\n")

        # Ask if user wants to save the fact
        save_choice = input("Do you want to save this fact? (y/n): ").lower()
        if save_choice == "y":
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(fact + "\n")
            print("Fact saved!\n")
        else:
            print("Fact not saved.\n")

    else:
        print("\nFailed to fetch the fact.\n")

while True:
    user_input = input("Press Enter to get a random fact or type 'q' to quit: ").lower()
    if user_input == "q":
        print("Goodbye! Your saved facts are in 'facts.txt'.")
        break
    get_random_facts()
