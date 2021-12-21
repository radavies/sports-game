class Places:

    def __init__(self, place_data):
        self.place_data = place_data

        self.places = {
            "Scotland": {
                "Cities": [],
                "Towns": [],
                "Villages": [],
                "Suburban Areas": [],
                "Education": []
            },
            "England & Wales": {
                "Cities": [],
                "Towns": [],
                "Villages": [],
                "Suburban Areas": [],
                "Education": []
            }
        }

        self.populate_place_object()

    def populate_place_object(self):

        for city in self.place_data["Cities"]:
            if city[2] == "Scotland":
                self.places["Scotland"]["Cities"].append(city)
            else:
                self.places["England & Wales"]["Cities"].append(city)

        for town in self.place_data["Towns"]:
            if town[2] == "Scotland":
                self.places["Scotland"]["Towns"].append(town)
            else:
                self.places["England & Wales"]["Towns"].append(town)

        for village in  self.place_data["Villages"]:
            if village[2] == "Scotland":
                self.places["Scotland"]["Villages"].append(village)
            else:
                self.places["England & Wales"]["Villages"].append(village)

        for sub in self.place_data["Suburban Areas"]:
            if sub[2] == "Scotland":
                self.places["Scotland"]["Suburban Areas"].append(sub)
            else:
                self.places["England & Wales"]["Suburban Areas"].append(sub)

        for edu in self.place_data["Education"]:
            if edu[2] == "Scotland":
                self.places["Scotland"]["Education"].append(edu)
            else:
                self.places["England & Wales"]["Education"].append(edu)
