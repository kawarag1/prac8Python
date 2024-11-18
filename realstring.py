class RealSting:
    def __init__(self, first:str, second:str):
        self.first = first
        self.second = second

    def checkSELF(self):
        if len(self.first) > len(self.second):
            print(f"Строка {self.first} больше")
        elif len(self.first) == len(self.second):
            print("Строки равны")
        else:
            print(f"Строка {self.second} больше")

    @staticmethod
    def check(firstword:str, secondword:str):
        if len(firstword) > len(secondword):
            print(f"Строка {firstword} больше")
        elif len(firstword) == len(secondword):
            print("Строки равны")
        else:
            print(f"Строка {secondword} больше")



some = RealSting("яблоко", "груша")
print(some.checkSELF())

RealSting.check("герой", "привет")