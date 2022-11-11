def greet(name, isEnemy):
    if isEnemy:
        return f'Hello {name}! I will kill you, bastard!'
    else:
        return f'Hello {name}! How are you?'

def eat_burgers(number):
    if number > 3:
        return f'Oh! I am overate!'
    else:
        return f'Mmm! That was excellent!'

def can_fly(name):
    if name == 'Batman':
        return True
    else:
        return False