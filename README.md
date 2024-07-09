# Droid Batch Manager

Witamy w aplikacji do zarządzania droidami pozwalającej na tworzenie, edytowanie, wczytywanie, zapisywanie i wyświetlanie partii droidów.
Aplikacja została stworzona przez zespół w składzie:
- Zuzanna Dul
- Piotr Kowalczyk
- Mateusz Kuczyński
- Nina Nowocień
- Patryk Śliwiński 

## Opcje aplikacji

1. **Dodaj nową partię droidów** - pozwala na dodanie nowej partii droidów.
2. **Wczytaj partie droidów z pliku** - umożliwia wczytanie partii droidów z pliku CSV.
3. **Edytuj partię droidów** - umożliwia edytowanie istniejącej partii droidów.
4. **Wyświetl wszystkie partie droidów** - wyświetla wszystkie istniejące partie droidów.
5. **Zapisz partie droidów do pliku** - zapisuje partie droidów do pliku CSV.
6. **Wyjdź z programu** - zapisuje aktualny stan partii droidów do pliku CSV i wychodzi z programu.


## Funkcje aplikacji

### `create_droid_batch`
Funkcja odpowiedzialna za tworzenie nowej partii droidów. Pyta użytkownika o szczegóły nowej partii i zwraca utworzoną partię.

### `edit_droid_batch`
Funkcja umożliwiająca edycję istniejącej partii droidów. Użytkownik może modyfikować szczegóły wybranej partii.

### `save_batches_to_csv`
Funkcja zapisująca partie droidów do pliku CSV. Wymaga ścieżki do pliku oraz listy partii droidów do zapisania.

### `load_batches_from_csv`
Funkcja wczytująca partie droidów z pliku CSV. Wymaga podania ścieżki do pliku i zwraca listę wczytanych partii droidów.

### `batchesprinter`
Funkcja wyświetlająca wszystkie partie droidów w czytelnej formie.


## Instrukcja

1. **Dodanie nowej partii droidów**
    - Wybierz opcję `1`.
    - Postępuj zgodnie z instrukcjami, aby dodać szczegóły nowej partii droidów.
    - Nowa partia zostanie dodana do listy partii droidów.

2. **Wczytanie partii droidów z pliku**
    - Wybierz opcję `2`.
    - Podaj ścieżkę do pliku CSV.
    - Partie droidów zostaną wczytane z podanego pliku.

3. **Edycja partii droidów**
    - Wybierz opcję `3`.
    - Postępuj zgodnie z instrukcjami, aby edytować wybraną partię droidów.
    - Zaktualizowana partia zostanie zapisana w liście partii droidów.

4. **Wyświetlenie wszystkich partii droidów**
    - Wybierz opcję `4`.
    - Wszystkie partie droidów zostaną wyświetlone w czytelnej formie.

5. **Zapisanie partii droidów do pliku**
    - Wybierz opcję `5`.
    - Podaj ścieżkę do pliku CSV.
    - Partie droidów zostaną zapisane do podanego pliku.

6. **Wyjście z programu**
    - Wybierz opcję `6`.
    - Podaj ścieżkę do pliku CSV, jeśli jeszcze tego nie zrobiłeś.
    - Partie droidów zostaną zapisane, a program zakończy działanie.
