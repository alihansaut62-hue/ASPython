class admin :
    



    def __init__(self, name, role, age, wel):
        self.name = name
        self.role = role
        self.age = age
        self.wel = wel
        self.reset = 0

    def nai(self):
        print(f"\nyour name {self.name}")  
        print(f"your role {self.role}") 
        print(f"your age {self.age}")
    
    def we(self):
        if self.role == 'admin':
            print(f"{self.role}, ваших привилегий хватает на:")
            print("добавлять людей\nудалять людей\nбанить людей") 
        else:
            print("у вас недостаточно прав")

    def log(self,):
        self.reset += 1
        print(f"вы регестрирвались {self.reset} раз")

    def res(self):
        self.reset = 0 
        print(f"вашый попытки были сброшаны до {self.reset}")

# admi = admin('ali', 'admin', 19, 'welcome')
# admi.nai()
# admi.we()
# admi.log()
# admi.log()
# admi.log()
# admi.log()
# admi.res()
use = admin.user('max')
use.lo()




