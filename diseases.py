import diagnost

class Disease:
    name: str
    mkb10: str
    symptoms: dict

    def __init__(self):
        self.name = "Undefined disease"
        self.mkb10 = "Z00.0"
        self.symptoms = {}

    def __init__(self, name, mkb10, symptoms):
        self.name = name
        self.mkb10 = mkb10
        self.symptoms = symptoms

    def __str__(self):
        return f"Disease: {self.mkb10}:{self.name}"
# Different diseases are stored there
flu = Disease("Грипп", "J11.8", {"type": "soma", "headache" : True, "cough" : True, "loose_smell":False})
cold = Disease("Простуда", "J06.9", {"type": "soma", "headache" : False, "cough" : True, "loose_smell":False})
covid = Disease("COVID-19", "U07.2", {"type": "soma", "headache" : False, "cough" : True, "loose_smell":True})

shiza = Disease("Шизофрения", "F20.9", {"type": "psycho", "hal": True})
depression = Disease("Депрессия", "F32.9", {"type": "psycho", "hal": False})

default = Disease("Undefined disease", "Z00.0", {})
