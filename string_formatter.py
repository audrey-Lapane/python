#username and messager formatter

fname = input("Enter your name:").strip()
lname = input("Enter your last name:").strip()
bio_message = input("Enter a short bio message:").strip()

username = f"{fname[0].lower()}{lname.lower()}"
print(f"Welcome {fname.title()} {lname.title()}!")

num_char_bio = len(bio_message)
bio_message = bio_message.replace("I am","I'm" )


print(f"{username}'s bio {bio_message} has length of {num_char_bio}.")