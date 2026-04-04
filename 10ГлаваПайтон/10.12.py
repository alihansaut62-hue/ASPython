from pathlib import Path
import json

class nomer:

    def get_save(self, path):
        if path.exists():
            conect = path.read_text()
            nom = json.loads(conect)
            return nom
        else:
            return None
        
    def sdf(self):
        path = Path('nom.json')
        nom = input("цифра ")
        conects = json.dumps(nom)
        path.write_text(conects)
        print(f"new nom {nom}")
    
        
    

    def greet_nom(self):
        path = Path('nom.json')
        nom = self.get_save(path)
        print(f"номер {nom}")
        a = input("это авши данные (y/n)")
        if a == "n":
            self.sdf()
        else:
            path = Path('nom.json')
            nom = self.get_save(path)
            if nom:
                print(f"номер {nom}")
            else:
                self.sdf()
    
    

    def greet_name(self):
        path = Path('name.json')
        name = self.get_save(path)
        if name:
            print(f"name {name}")
        else:
            name = input("name ")
            conects = json.dumps(name)
            path.write_text(conects)
            print(f"new nom {name}")

    def sive_last_name(self):
        path = Path('last_name.json')
        last_name = self.get_save(path)
        if last_name:
            print(f"last {last_name}")
        else:
            last_name = input("last_name ")
            conects = json.dumps(last_name)
            path.write_text(conects)
            print(f"new nom {last_name}")
    

    

fgh = nomer()
fgh.greet_nom()
fgh.greet_name()
fgh.sive_last_name()
    










