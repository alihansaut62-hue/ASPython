class user :
    def __init__(self, name, last, age, wel):
        self.name = name
        self.last = last
        self.age = age
        self.wel = wel
        self.reset = 0

    def nai(self):
        print(f"\nyour name {self.name}")  
        print(f"your last {self.last}") 
        print(f"your age {self.age}")
    
    def we(self):
        print(f"personal greeting \"{self.wel}\"")



use = user('ali', 'sau', 19, 'welcome')
use.nai()
use.we()




