#testlist = [{"unique_id": 1, "name": "AAA", "count": 10, "special_ability": "Brak", "software_version": 1.0}, {"unique_id": 2, "name": "BBB", "count": 20, "special_ability": "Karate", "software_version": 1.1}]

def batchesprinter(alist):
    print("Aktualny stan magazynowy droidów prezentuje się następująco:\n")
    for i in range(len(alist)):
        uid = alist[i]["unique_id"]
        name = alist[i]["name"]
        count = alist[i]["count"]
        spec = alist[i]["special_ability"]
        soft = alist[i]["software_version"]
        print(f"Batch o oznaczeniu {uid}: ")
        print(f"Nazwa droidów: {name}")
        print(f"Liczba droidów: {count}")
        print(f"Umiejętności specjalne droidów: {spec}")
        print(f"Wersja oprogramowania droidów: {soft}\n")


#batchesprinter(testlist)