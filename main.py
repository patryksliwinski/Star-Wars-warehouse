from create_droid_batch import create_droid_batch
from edit_droid_batch import edit_droid_batch
from batchesprinter import batchesprinter

def main():
    droid_batches = []
    
    print("Witaj w programie do zarządzania droidami!")
    
    while True:
        print("")
        print("Wybierz jedną z opcji:")
        print("1. Dodaj nową partię droidów")
        print("2. Edytuj partię droidów")
        print("3. Wyświetl wszystkie partie droidów")
        print("4. Wyjdź z programu")
        print("")

        user_choice = input("Wybierz opcję: ")

        if user_choice == "1":
            droid_batch = create_droid_batch()
            droid_batches.append(droid_batch)
        elif user_choice == "2":
            edit_droid_batch(droid_batches)
        elif user_choice == "3":
            batchesprinter(droid_batches)
        elif user_choice == "4":
            exit()
        else:
            print("Niepoprawny wybór")
        
main()