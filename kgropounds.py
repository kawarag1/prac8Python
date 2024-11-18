class KgToPounds:
    def __init__(self, kg):
        self._kg = kg

    def to_pounds(self):
        return self._kg * 2.205

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self._kg = new_kg
        else:
            raise ValueError("Килограммы задаются только числами")
        

_kg = KgToPounds(10)
print(_kg.to_pounds())