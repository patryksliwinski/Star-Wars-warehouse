import uuid

def create_droid_batch():
    
    droid_batch = {
        "name": input("Podaj nazwę droidów: "),
        "count": int(input("Podaj liczbę droidów: ")),
        "special_ability": input("Podaj umiejętności specjalne droidów: "),
        "software_version": input("Podaj wersję oprogramowania droidów: "),
        "unique_id": str(uuid.uuid4())
    }

    return droid_batch