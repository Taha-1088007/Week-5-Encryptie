import getpass
from datetime import datetime
from cryptography.fernet import InvalidToken
from storage import file_exists, load_diary, save_diary


def write_text(password):
    text = input("Your text: ").strip()
    if not text:
        print("You can't save an empty message ")
        return
    diary = load_diary(password)
    date = datetime.now().strftime("%d-%m-%Y %H:%M")
    diary += f"[{date}] {text}\n"
    save_diary(diary, password)
    print("Saved (encrypted).")

def show_diary(password):
    diary = load_diary(password)
    print("\n---Your diary---")
    print(diary if diary
          else "(is empty)")

def search_diary(password):
    keyword = input("Search for: ").strip().lower()
    if not keyword:
        print("You need to fill in a keyword")
        return
    found = [
        line for line in load_diary(password).splitlines()
            if keyword in line.lower()
    ]
    if found:
        print(f"\n {len(found)} result/results")
        for line in found:
            print(line)
    else:
        print("Not found.")


def change_password(password):
    new = getpass.getpass("New password:")
    if not new:
        print("Password can't be empty.")
        return password
    if getpass.getpass("repeat new password: ") != new:
        print("Password does not match.")
        return password
    diary = load_diary(password) #with the old password
    save_diary(diary, new) # save it with the new
    print("Password changed.")
    return new

def main():
    print("=== Secret diary ===")
    password = getpass.getpass("Password:")
    if not password:
        print("Password can't be empty.")
        return

    if not file_exists():
        if getpass.getpass("Repeat new password: ") != password:
            print("Password does not match.")
            return


    try:
        load_diary(password)
    except InvalidToken:
        print("Invalid password.")
        return

    while True:
        print("\n1. Schrijf een bericht")
        print("2. Lees het dagboek")
        print("3. Zoek in het dagboek")
        print("4. Wachtwoord wijzigen")
        print("5. Verlaten")
        choice = input("Voer uw keuze in: ").strip()

        if choice == "1":
            write_text(password)
        elif choice == "2":
            show_diary(password)
        elif choice == "3":
            search_diary(password)
        elif choice == "4":
            password = change_password(password)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

