def short (nak, size='L'):
    print(f"размер {size} стиль {nak}")

nak = input("stile ")
size = input("size ")
if size == "":
    size =  'L'



short(nak=nak, size=size)