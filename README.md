# Проект LearnPythonBot

Первый для меня проект, бот присылает картинки, вашу геолокацию, а также пересылает все, что вы ему напишете.

## Установка

1. Клонируйте репозиторий с github
2. Создайте виртуальное окружение
3. Установите зависимости `pip install -r requirements.txt`
4. Создайте файл `settings.py`
5. Впишите в settings.py переменные:
```
API_KEY = "API-ключ бота" 
PROXY_URL = "Адрес прокси" - при необходимости
PROXY_USERNAME = "Логин прокси" - при необходимости
PROXY_PASSWORD = "Пароль на прокси" - при необходимости
USER_EMOJI = [':cat:', ':hamster:', ':frog:', ':panda_face:', 
            ':baby_chick:', ':rabbit:', ':koala:', ':sheep:']
```
6. Запустите бота командой `python bot.py`
