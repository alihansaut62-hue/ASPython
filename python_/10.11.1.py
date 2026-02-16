from pathlib import Path
import json

path = Path('nom.jspn')
conects = path.read_text()
nom = json.loads(conects)
print("выша число", nom)