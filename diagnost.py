import diseases


class Therapist:
    symptoms = {}

    def diagnose(self):
        if self.symptoms.get("type") == "soma":
            if self.symptoms.get("headache"):
                return diseases.flu
            else:
                if self.symptoms.get("loose_smell"):
                    return diseases.covid
                elif not self.symptoms.get("loose_smell") and self.symptoms.get("cough"):
                    return diseases.cold
                else:
                    return diseases.default

        elif self.symptoms.get("type") == "psycho":
            if self.symptoms.get("hal"):
                return diseases.shiza
            elif not self.symptoms.get("hal") and self.symptoms.get("bad_mood"):
                return diseases.depression
            else:
                return diseases.default

        else:
            return diseases.default
