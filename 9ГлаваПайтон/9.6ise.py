class iceCream :
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.servis = 0

    def ingridient(self,):
        if self.type == "plan":
            print(f"{self.type} ingredients")
            print("Milk \nCream \nButter \nSugar \nEgg \nyolk \nVanilla \nCondensed \nmilk (optional)") 
        else:
            print("We don't have that kind of ice cream.")
        

    



rest = iceCream('bon', 'plan')

rest.ingridient()

