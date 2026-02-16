import mmap

a = input("Пароль: ").encode()

with open(r"C:\Users\Admin\Desktop\python_\experiments\rockyou2021.txt", "rb") as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    if mm.find(a) != -1:
        print("😹 вы взламаны лашары")
    else:
        print("❌ Не найден")
