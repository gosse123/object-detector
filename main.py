import os

print("=== Détection Main & Visage ===\n")
print("1. Détection de Main")
print("2. Détection de Visage")
choice = input("\nChoisissez une option (1/2) : ")

if choice == "1":
    os.system("python src/hand.py")
elif choice == "2":
    os.system("python src/face.py")
else:
    print("Choix invalide !")