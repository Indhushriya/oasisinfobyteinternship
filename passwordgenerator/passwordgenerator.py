import string
import random
print("🔒----------------------------------------------------🔒")
print("   ░█▀▀█ ─█▀▀█ ░█▀▀▀█ ░█▀▀▀█ ░█──░█ ░█▀▀▀█ ░█▀▀█ ░█▀▀▄ ")
print("   ░█▄▄█ ░█▄▄█ ─▀▀▀▄▄ ─▀▀▀▄▄ ░█░█░█ ░█──░█ ░█▄▄▀ ░█─░█ ")
print("   ░█─── ░█─░█ ░█▄▄▄█ ░█▄▄▄█ ░█▄▀▄█ ░█▄▄▄█ ░█─░█ ░█▄▄▀ ")
print("🔒----------------------------------------------------🔒")

length = int(input("\nEnter password length:"))
print("🔒----------------------------------------------------🔒")
print("Choose password complexity:")
print("1. Letters (e.g., abcDEF)")
print("2. Letters and digits (e.g., abc123)")
print("3. Letters, digits, and symbols (e.g., abc123!@#)")
choice = int(input("Choice : "))
print("🗝️----------------------------------------------------🗝️")
match choice:
    case 1: 
        characters = string.ascii_letters
    case 2: 
        characters = string.ascii_letters + string.digits
    case 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    case default:
        print("Invalid choice")
        exit()

password = ''.join(random.choice(characters) for i in range(length))

print(f"\n\033[33m Random password: {password}\033[0m\n")
print("🗝️----------------------------------------------------🗝️")

