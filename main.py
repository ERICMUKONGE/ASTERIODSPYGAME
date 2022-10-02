class Human:
    def __init__(self,name,age):

        self.name=name
        self.age=age
        print(self)

    def __str__(self) -> str:
        return f"<Human {self.name}>"

name = ""

name.isupper()

human=Human(name="human 1",age=23)