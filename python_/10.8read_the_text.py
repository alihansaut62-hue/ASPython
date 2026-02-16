from pathlib import Path


file = Path("cat.txt")
fil = Path("Dojgs.txt")
try:
    s1 = file.read_text()
    a = fil.read_text()
except FileNotFoundError:
    print("фаил не найден")
else:   
    print(s1)
    print()
    print(a)
