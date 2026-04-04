while True:
    def al(nmae, w):
        print(f"испольнитель {nmae}")
        print(f"альбом {w}")
        print(f"описание {oips[nmae][w]}")



    oips =  {
        "macan" : {
            1 : {"вроде норм"},
            2 : {"zaebal"}
        },
        "santiz" : {
            1 : {"zaebis"},
            2 : {"ahutelna"}
        }
    }

    nmae = input("испольнитель ")
    w = int(input("альбом "))
    if w == 'q':
        break



    print(f"описание {oips[nmae][w]}")

    d = al(nmae, w)
    print(d)
