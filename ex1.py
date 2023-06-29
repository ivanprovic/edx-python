# Ask user for their name
name = input("Whats your name? ").strip().title()

first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")
