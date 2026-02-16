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

    def log(self,):
        self.reset += 1
        print(f"вы регестрирвались {self.reset} раз")

    def res(self):
        self.reset = 0 
        print(f"вашый попытки были сброшаны до {self.reset}")

use = user('ali', 'sau', 19, 'welcome')
use.nai()
use.we()
use.log()
use.log()
use.log()
use.log()
use.res()



