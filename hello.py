# Ask user for their name, remove whitespaces and capitalize the user's name
__name__ = input("What's full name? ").strip().title()

#Split user's name into first name and last
first, last = __name__.split(" ")

# Say hello to user
print(f"hello, {first}")
print(f"how are you, Mr.{last}?")