class Restaurant :
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.servis = 0

    def ser(self, kli):
        if kli >= self.servis:
            self.servis = kli
        else :
            print("крутить назат запрешено !!")
        print(f"new servis = {kli}")



    def nai(self):
        print(f"\n{self.name} That's the name of the restaurant")  
        print(f"{self.type} is now roll_over") 
        print("open the Restaurant")


rest = Restaurant('bon', 'yep')

rest.nai()
rest.ser(1)
