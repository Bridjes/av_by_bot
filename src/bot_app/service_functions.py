import random
import string

def generate_password(n):
    characters = string.ascii_letters + string.digits  # все буквы и цифры
    password = ''.join(random.choice(characters) for i in range(n))  # генерация пароля из 8 символов
    return password