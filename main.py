from create_droid_batch import create_droid_batch
from edit_droid_batch import edit_droid_batch
from load_and_save_batches import save_batches_to_csv, load_batches_from_csv

def main():
    droid_batches = []
    file_path = None
    
    print("Witaj w programie do zarządzania droidami!")
    
    while True:
        print("")
        print("Wybierz jedną z opcji:")
        print("1. Dodaj nową partię droidów")
        print("2. Wczytaj partie droidów z pliku")
        print("3. Edytuj partię droidów")
        print("4. Wyświetl wszystkie partie droidów")
        print("5. Zapisz partie droidów do pliku")
        print("6. Wyjdź z programu")
        print("")

        user_choice = input("Wybierz opcję: ")

        if user_choice == "1":
            droid_batch = create_droid_batch()
            droid_batches.append(droid_batch)
        elif user_choice == "2":
            file_path = input("Podaj ścieżkę do pliku CSV: ")
            droid_batches = load_batches_from_csv(file_path)
            print("Partie droidów zostały wczytane z pliku.")
        elif user_choice == "3":
            edit_droid_batch(droid_batches)
        elif user_choice == "4":
            print(droid_batches)
        elif user_choice == "5":
            if file_path is None:
                file_path = input("Podaj ścieżkę do pliku CSV: ")
            save_batches_to_csv(file_path, droid_batches)
            print("Partie droidów zostały zapisane do pliku.")
        elif user_choice == "6":
            if file_path is None:
                file_path = input("Podaj ścieżkę do pliku CSV: ")
            save_batches_to_csv(file_path, droid_batches)
            print("Zapisano, trwa wyjście z programu.")
            exit()
        else:
            print("Niepoprawny wybór")
        
main()