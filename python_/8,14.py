def make_car(mark, model, **car):
    car['mark'] = mark
    car['model'] = model
    return car

carr = make_car('woldswagen', 'passat',
                condition= 'broken', What= 'repair')
print(carr)