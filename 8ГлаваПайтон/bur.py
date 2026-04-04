def make_but(size, *toppings):
    print(f"приготовьте бургер размером {size} и с начинками:")
    for topping in toppings:
        print(f"- {topping}")