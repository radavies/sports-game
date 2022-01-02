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

        self._populate_place_object()

    def _populate_place_object(self):

        added_names_scotland = {}
        added_names_england_and_wales = {}

        for city in self.place_data["Cities"]:
            if city[2] == "Scotland":
                if city[0] not in added_names_scotland:
                    self.places["Scotland"]["Cities"].append(
                        {"Name": city[0], "Sub Area": city[1], "Main Area": city[2],
                         "Type": "City", "Has Team": False}
                    )
                    added_names_scotland[city[0]] = True
            else:
                if city[0] not in added_names_england_and_wales:
                    self.places["England & Wales"]["Cities"].append(
                        {"Name": city[0], "Sub Area": city[1], "Main Area": city[2],
                         "Type": "City", "Has Team": False}
                    )
                    added_names_england_and_wales[city[0]] = True

        for town in self.place_data["Towns"]:
            if town[2] == "Scotland":
                if town[0] not in added_names_scotland:
                    self.places["Scotland"]["Towns"].append(
                        {"Name": town[0], "Sub Area": town[1], "Main Area": town[2],
                         "Type": "Town", "Has Team": False}
                    )
                    added_names_scotland[town[0]] = True
            else:
                if town[0] not in added_names_england_and_wales:
                    self.places["England & Wales"]["Towns"].append(
                        {"Name": town[0], "Sub Area": town[1], "Main Area": town[2],
                         "Type": "Town", "Has Team": False}
                    )
                    added_names_england_and_wales[town[0]] = True

        for village in self.place_data["Villages"]:
            if village[2] == "Scotland":
                if village[0] not in added_names_scotland:
                    self.places["Scotland"]["Villages"].append(
                        {"Name": village[0], "Sub Area": village[1], "Main Area": village[2],
                         "Type": "Village", "Has Team": False}
                    )
                    added_names_scotland[village[0]] = True
            else:
                if village[0] not in added_names_england_and_wales:
                    self.places["England & Wales"]["Villages"].append(
                        {"Name": village[0], "Sub Area": village[1], "Main Area": village[2],
                         "Type": "Village", "Has Team": False}
                    )
                    added_names_england_and_wales[village[0]] = True

        for sub in self.place_data["Suburban Areas"]:
            if sub[2] == "Scotland":
                if sub[0] not in added_names_scotland:
                    self.places["Scotland"]["Suburban Areas"].append(
                        {"Name": sub[0], "Sub Area": sub[1], "Main Area": sub[2],
                         "Type": "Suburban Area", "Has Team": False}
                    )
                    added_names_scotland[sub[0]] = True
            else:
                if sub[0] not in added_names_england_and_wales:
                    self.places["England & Wales"]["Suburban Areas"].append(
                        {"Name": sub[0], "Sub Area": sub[1], "Main Area": sub[2],
                         "Type": "Suburban Area", "Has Team": False}
                    )
                    added_names_england_and_wales[sub[0]] = True

        for edu in self.place_data["Education"]:
            if edu[2] == "Scotland":
                if edu[0] not in added_names_scotland:
                    self.places["Scotland"]["Education"].append(
                        {"Name": edu[0], "Sub Area": edu[1], "Main Area": edu[2],
                         "Type": "Education", "Has Team": False}
                    )
                    added_names_scotland[edu[0]] = True
            else:
                if edu[0] not in added_names_england_and_wales:
                    self.places["England & Wales"]["Education"].append(
                        {"Name": edu[0], "Sub Area": edu[1], "Main Area": edu[2],
                         "Type": "Education", "Has Team": False}
                    )
                    added_names_england_and_wales[edu[0]] = True
