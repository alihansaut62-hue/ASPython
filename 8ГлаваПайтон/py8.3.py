


def forevorbook(size, picture = 'L'):
    print(f"you T-shirt size {size} \npicture {picture}")
    

size = input("T-shirt size ")


picture = input()
if picture == "":
    picture = 'L'



forevorbook(size=size, picture=picture)     


