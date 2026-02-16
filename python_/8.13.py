def profile(first, last, **user_info):
    user_info['frist_name'] = first
    user_info['last_name'] = last
    return user_info

user = profile('saut', 'alihan',
                professia= 'progran', love= 'nout')
print(user)