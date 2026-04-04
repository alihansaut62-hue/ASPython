class erorr:
    try:
        a = int(input("введите число "))
        b = int(input("введите число "))        
    except ValueError:  
        print("ошибка из за непавельного введения введите цифру")
    else:
        print(b + a)
