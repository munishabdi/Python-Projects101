
# **kwargs - is used to add multiple keyword arguments

def save_user(**user):
    print(f"Hello my name is {user['name']} and my age is {user['age']}")
    print(f'I work as an {user["title"]}')
save_user(name= 'Munasar', age= 24, title= 'engineer')
