import csv
from pathlib import Path
from game.enums.misc import Misc


def get_name_data_from_file():
    folder = Path(Misc.NamesFolderPath.value)
    animals_file = folder / "animals.txt"
    things_file = folder / "things.txt"
    prename_file = folder / "pre_name.txt"

    name_data = {
        "Animals": [],
        "Things": [],
        "Pre-Names": []
    }

    animals = open(animals_file)
    for animal in animals:
        name_data["Animals"].append(list(map(str.strip, animal.split(','))))
    animals.close()

    things = open(things_file)
    for thing in things:
        name_data["Things"].append(list(map(str.strip, thing.split(','))))
    things.close()

    prenames = open(prename_file)
    for prename in prenames:
        name_data["Pre-Names"].append(prename.strip())
    prenames.close()

    return name_data


def get_place_data_from_file():
    folder = Path(Misc.PlaceFolderPath.value)
    place_data = {
        "Cities": [],
        "Towns": [],
        "Villages": [],
        "Suburban Areas": [],
        "Education": []
    }

    cities_file = folder / "cities.txt"
    towns_file = folder / "towns.txt"
    villages_file = folder / "villages.txt"
    suburban_file = folder / "suburban.txt"
    education_file = folder / "education.txt"

    cities = open(cities_file)
    for city in cities:
        place_data["Cities"].append(list(map(str.strip, city.split(','))))
    cities.close()

    towns = open(towns_file)
    for town in towns:
        place_data["Towns"].append(list(map(str.strip, town.split(','))))
    towns.close()

    villages = open(villages_file)
    for village in villages:
        place_data["Villages"].append(list(map(str.strip, village.split(','))))
    villages.close()

    suburban = open(suburban_file)
    for sub in suburban:
        place_data["Suburban Areas"].append(list(map(str.strip, sub.split(','))))
    suburban.close()

    education = open(education_file)
    for edu in education:
        place_data["Education"].append(list(map(str.strip, edu.split(','))))
    education.close()

    return place_data


def __create_place_data_from_os_csv():
    folder = Path(Misc.RawDataFolderPath.value)
    out_folder = Path(Misc.DataFolderPath.value)
    iterator = folder.glob("*.csv")

    errors = []
    cities = []
    towns = []
    villages = []
    suburban = []
    education = []

    for item in iterator:
        if item.is_file():
            with open(item, newline="") as csvfile:
                reader = csv.reader(csvfile, delimiter=",", quotechar='"')
                try:
                    for row in reader:
                        if row[7] == "City":
                            cities.append([row[2], row[24], row[27]])
                        elif row[7] == "Village":
                            villages.append([row[2], row[24], row[27]])
                        elif row[7] == "Town":
                            towns.append([row[2], row[24], row[27]])
                        elif row[7] == "Suburban Area":
                            suburban.append([row[2], row[24], row[27]])
                        elif row[7] == "Higher or University Education" or row[7] == "Further Education,Secondary Education" or row[7] == "Further Education,Higher or University Education":
                            education.append([row[2], row[24], row[27]])
                except Exception as ex:
                    errors.append(item.name)

    cities_file = out_folder / "cities.txt"
    with open(cities_file, "x") as f:
        for city in cities:
            f.write(",".join(city) + "\n")

    towns_file = out_folder / "towns.txt"
    with open(towns_file, "x") as f:
        for town in towns:
            f.write(",".join(town) + "\n")

    villages_file = out_folder / "villages.txt"
    with open(villages_file, "x") as f:
        for village in villages:
            f.write(",".join(village) + "\n")

    suburban_file = out_folder / "suburban.txt"
    with open(suburban_file, "x") as f:
        for sub in suburban:
            f.write(",".join(sub) + "\n")

    education_file = out_folder / "education.txt"
    with open(education_file, "x") as f:
        for edu in education:
            f.write(",".join(edu) + "\n")
