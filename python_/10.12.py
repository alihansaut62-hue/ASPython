from pathlib import Path
import json

class nomer:

    def get_save(self):
        
    

    def greet_nom(self):
        path = Path('nom.json')
        
        if path.exists():
            conect = path.read_text()
            nom = json.loads(conect)
            print(f"your forewr nomer {nom}")
        else:
            nom = input("цифра ")
            conects = json.dumps(nom)
            path.write_text(conects)
            print(f"new nom {nom}")

fgh = nomer()
fgh.greet_nom()
    










