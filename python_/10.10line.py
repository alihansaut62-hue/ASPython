from pathlib import Path

file = Path("Grimms.txt")
s1 = file.read_text(encoding="utf-8")
f = s1.count('the')
c = s1.lower().count('the')
v = s1.lower().count('the ')
print(f)
print(c)
print(v)