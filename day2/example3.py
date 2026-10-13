class vehcile:
    def __init__(self,name,model):
        self.name=name
        self.model=model

class car(vehcile):
    def __init__(self,name,model):
        super().__init__(name,model)

    def getname(self):
        return self.name


def main():
    car1=car("polo","vw")
    print(car1.getname())


if __name__ == "__main__":
    main()