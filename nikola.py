class Nikola:
    def __init__(self, name:str, age:int):
        if name == "Николай" or name == "николай":
            self.name = name
        else:
            self.name = f"Я не {name}, а Николай"
        self.age = age
    
    def __setattr__(self, name, value):
        if name in ["name", "age"]:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"Нельзя добавить атрибут '{name}'")
    
    def __delattr__(self, name):
        raise AttributeError(f"Нельзя удалить атрибут '{name}'")