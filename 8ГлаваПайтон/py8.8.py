oips = {
    "santiz": {
        1: "zaebis",
        2: "ahutelna"
    }
}

def al(name, album):
    print(f"\nИсполнитель: {name}")
    print(f"Альбом: {album}")
    print(f"Описание: {oips[name][album]}\n")

while True:
    all_desc = input("описание (или q для выхода): ")
    if all_desc == 'q':
        break

    name = input("исполнитель (или q для выхода): ")
    if name == 'q':
        break

    w = input("альбом (или q для выхода): ")
    if w == 'q':
        break
    w = int(w)

    # если исполнителя нет — создаём
    if name not in oips:
        oips[name] = {}

    # добавляем/обновляем описание
    oips[name][w] = all_desc

    # вывод результатов
    al(name, w)
       