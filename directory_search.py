#A mini data directory using a List and a Dictionary combined.

contacts = {
    "audrey":"0731661949",
    "regina":"0712550268",
    "punch":"0741006537"
}

friend = input("Enter the name of the friend you want to look for:").strip().lower()


if friend in contacts:
    print(f"Found! {friend}'s number is {contacts[friend]}")
else:
    print("Contact not found.")