from celery import shared_task
import requests
import random
import string

def generate_random_name(length=8):
    # Генерируем случайное имя, состоящее из букв и цифр
    letters_and_digits = string.ascii_letters + string.digits
    random_name = ''.join(random.choice(letters_and_digits) for _ in range(length))
    
    # Добавляем расширение файла
    return random_name + ".jpg"

@shared_task
def download_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    r = requests.get(r.json()[0]['url'])

    with open('/cats/' + generate_random_name(), "wb") as file:
        file.write(r.content)