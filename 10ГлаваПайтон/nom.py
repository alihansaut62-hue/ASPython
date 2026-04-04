from pathlib import Path
import json

class nomer:

    def new_nom(path):
        nom = input("цифра ")
        path = Path('nom.jspn')
        conects = json.dumps(nom)
        path.write_text(conects)


sdf = nomer()
sdf.new_nom()


