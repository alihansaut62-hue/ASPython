from pathlib import Path
path = Path('text')
conects = path.read_text()  

for line in conects.splitlines():
    print(line)
