def greet_users(names):
    """выводит простое приветствия для каждого пользвателя в списке."""
    for name in names:
        msg = f"Привет, {name.title()}!"
        print(msg)

sdsd = ['aziz', 'john', 'maria']
greet_users(sdsd)