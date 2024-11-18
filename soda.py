from pydantic import BaseModel

class Soda(BaseModel):
    Supplement:str

    def show_my_dring(self):
        if self.Supplement is None:
            return("Обычная газировка")
        else:
            return(f"Газировка с {self.Supplement}")
        

coke = Soda(Supplement="добавка")
print(coke.show_my_dring())