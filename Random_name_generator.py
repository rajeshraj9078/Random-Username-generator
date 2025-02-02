import random

# Pre-defined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Brave", "Wild", "Gentle", "Clever", "Mystic", "Fierce", "Lucky", "Silent"]
nouns = ["Tiger", "Dragon", "Phoenix", "Wolf", "Eagle", "Bear", "Lion", "Fox", "Hawk", "Panther"]

def generate_username(include_numbers=False, include_special_chars=False, length=None):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    username = f"{adjective}{noun}"
    
    if include_numbers:
        username += str(random.randint(0, 999))
    
    if include_special_chars:
        special_chars = ["!", "@", "#", "$", "%", "&", "*"]
        username += random.choice(special_chars)
    
    
    if length and len(username) > length:
        username = username[:length]
    
    return username

def save_usernames(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {filename}")

def main():
    print("Welcome to the Random Username Generator!")
    
    num_usernames = int(input("How many usernames would you like to generate? "))
    include_numbers = input("Include numbers? (y/n): ").lower() == "y"
    include_special_chars = input("Include special characters? (y/n): ").lower() == "y"
    length = input("Set a maximum length for the username (press Enter to skip): ")
    length = int(length) if length.isdigit() else None
    
    usernames = []
    for _ in range(num_usernames):
        username = generate_username(include_numbers, include_special_chars, length)
        usernames.append(username)
        print(f"Generated: {username}")
    
    save_option = input("Would you like to save the usernames to a file? (y/n): ").lower()
    if save_option == "y":
        save_usernames(usernames)

    print("Thank you !")


if __name__ == "__main__":
    main()