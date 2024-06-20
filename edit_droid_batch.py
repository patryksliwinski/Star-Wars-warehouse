def edit_droid_batch(droid_batches):

    print("Dostępne partie droidów:")
    for i, batch in enumerate(droid_batches):
        print(f"{i + 1}. {batch['name']} (ID: {batch['unique_id']})")

    batch_number = int(input("Podaj numer partii do edycji: ")) - 1

    if batch_number < 0 or batch_number >= len(droid_batches):
        print("Nieprawidłowy numer partii.")
        return

    droid_batch = droid_batches[batch_number]

    print("Aktualne dane partii droidów:")
    for key, value in droid_batch.items():
        print(f"{key}: {value}")

    print("\nKtóre pole chcesz edytować?")
    print("1. Nazwa")
    print("2. Liczba")
    print("3. Umiejętności specjalne")
    print("4. Wersja oprogramowania")
    print("5. Anuluj edycję")

    choice = int(input("Wybierz numer pola do edycji: "))

    if choice == 1:
        droid_batch["name"] = input("Podaj nową nazwę droidów: ")
    elif choice == 2:
        droid_batch["count"] = int(input("Podaj nową liczbę droidów: "))
    elif choice == 3:
        droid_batch["special_ability"] = input("Podaj nowe umiejętności specjalne droidów: ")
    elif choice == 4:
        droid_batch["software_version"] = input("Podaj nową wersję oprogramowania droidów: ")
    elif choice == 5:
        print("Edycja anulowana.")
    else:
        print("Nieprawidłowy wybór, spróbuj ponownie.")

    print("Zaktualizowano partię droidów")

    droid_batches[batch_number] = droid_batch