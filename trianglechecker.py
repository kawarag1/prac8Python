from pydantic import BaseModel

class TriangleChecker(BaseModel):
    a:int
    b:int
    c:int

    def is_triangle(self):
        if (type(self.a) == str and type(self.b) == str and type(self.c) == str):
            return("Нужно вводить только числа!")
        elif ((self.a or self.b or self.c) <= 0):
            return("С отрицательными числами ничего не получится!")
        else:
            if(self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
                return("Ура, можно построить треугольник")
            else:
                return("Жаль, но из этого треугольник не сделать")
            


checker = TriangleChecker(a=12, b=13, c=14)
print(checker.is_triangle())