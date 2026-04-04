from pathlib import Path
path= Path('higaa.txt')

path= Path('higaa.txt')






while True:
    try:
        n = input("нажмие entor(или для выхода q)")
        if n == 'q' or n == 'Q' :
            break
        a = int(input("введите число"))
        c = input("+ , -, *, /")  
        b = int(input("введите число "))   


           
    except ValueError:  
        print("ошибка из за непавельного введения введите цифру")
        continue
    try:

        if c == "+":
            d = a + b
        elif c == "-":
            d = a - b
        elif c == "*":
            d = a * b
        elif c == "/":
            if b == 0:
                print("на ноль не делится ")
                continue
            d = a / b
    except NameError:
        print("Оибка:в неправельном вводе") 
        continue       

    with open("higaa.txt", "a", encoding="utf-8") as f:
        f.write(f"{a} {c} {b} = {d}\n")
    print(d)









