import random

class Names:

    def __init__(self, name_input):
        self.name_elements = {
            "Animals": [],
            "Things": [],
            "Pre-Names": []
        }

        self.populate_name_elements(name_input)

        self.animal_prob = 70
        self.alliteration_prob = 60

    def populate_name_elements(self, name_input):
        for animal in name_input["Animals"]:
            self.name_elements["Animals"].append(
                {"Singular": animal[0], "Plural": animal[1], "Used": False}
            )

        for thing in name_input["Things"]:
            self.name_elements["Things"].append(
                {"Singular": thing[0], "Plural": thing[1], "Used": False}
            )

        for prename in name_input["Pre-Names"]:
            self.name_elements["Pre-Names"].append(
                {"Name": prename, "Used": False}
            )

    def generate_name(self, place_name, allow_alliteration):
        available_animals = [option for option in self.name_elements["Animals"] if not option["Used"]]
        available_things = [option for option in self.name_elements["Things"] if not option["Used"]]
        available_prenames = [option for option in self.name_elements["Pre-Names"] if not option["Used"]]

        alliteration = allow_alliteration and random.randint(1, 100) <= self.alliteration_prob

        if alliteration:
            return self.generate_alliterative_name(place_name, available_animals, available_things, available_prenames)

        parts = random.randint(1, 2)
        animal = random.randint(1, 100) <= self.animal_prob

        if animal:
            choice = random.randint(0, len(available_animals) - 1)
            name = available_animals[choice]["Plural"]
            available_animals[choice]["Used"] = True
        else:
            choice = random.randint(0, len(available_things) - 1)
            name = available_things[choice]["Plural"]
            available_things[choice]["Used"] = True

        if parts > 1:
            choice = random.randint(0, len(available_prenames) - 1)
            name = "{} {}".format(available_prenames[choice]["Name"], name)
            available_prenames[choice]["Used"] = True

        if not place_name.startswith("The "):
            final_name = "The {} {}".format(place_name, name)
        else:
            final_name = "{} {}".format(place_name, name)

        return final_name

    def generate_alliterative_name(self, place_name, available_animals, available_things, available_prenames):
        alliterate_with = place_name[0]
        alliterate_animals = [option for option in available_animals if option["Singular"].startswith(alliterate_with)]
        alliterate_things = [option for option in available_things if option["Singular"].startswith(alliterate_with)]
        alliterate_prenames = [option for option in available_prenames if option["Name"].startswith(alliterate_with)]

        parts = random.randint(1, 2)
        animal = random.randint(1, 100) <= self.animal_prob

        if len(alliterate_animals) == 0 and len(alliterate_things) == 0:
            return self.generate_name(place_name, False)
        elif animal and len(alliterate_animals) == 0:
            animal = False
        elif not animal and len(alliterate_things) == 0:
            animal = True

        if animal:
            choice = random.randint(0, len(alliterate_animals) - 1)
            name = alliterate_animals[choice]["Plural"]
            alliterate_animals[choice]["Used"] = True
        else:
            choice = random.randint(0, len(alliterate_things) - 1)
            name = alliterate_things[choice]["Plural"]
            alliterate_things[choice]["Used"] = True

        if parts > 1:
            if len(alliterate_prenames) == 0:
                return self.generate_name(place_name, False)

            choice = random.randint(0, len(alliterate_prenames) - 1)
            name = "{} {}".format(alliterate_prenames[choice]["Name"], name)
            alliterate_prenames[choice]["Used"] = True

        if not place_name.startswith("The "):
            final_name = "The {} {}".format(place_name, name)
        else:
            final_name = "{} {}".format(place_name, name)

        return final_name
