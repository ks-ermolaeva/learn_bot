# Проект VkBot

VkBot - это бот для Telegram , который присылает пользователю фотографии с VK-FEST и напоминает о приятных моментах, проведенных на фестивале.

### Установка

1. Клонировать репозиторий с github
2. Создать виртуальное окружение
3. Установить зависимости `pip install -r requirements.txt`
4. Создать файл `settings.py`
5. Впишите в settings.py переменные: 
```
API_KEY = 'API-ключ бота' 

USER_EMOJI = [':sloth:', ':smiling_face_with_open_hands:', ':winking_face:', ':waving_hand:']
```
6. Запустите бота командой `python bot.py`