# Проект DRF_project1
 
## API Проекта онлайн-обучения, разработанный с использованием фреймворка Django.


Используемый стек:
- Код - Python
- Веб-фреймворк Django
- База данных - postgres
- Используемые в проекте сторонние библиотеки находятся в requirements.txt в корне проекта
___

### Запуск проекта производится с помощью Docker:

Рекомендации по запуску:
- Клонируйте проект
- настройки бaзы лежат в переменной DATABASES по пути ..\config\settings.py
- Переименуйте файл .env_sample в .env и заполните его своими данными
- Запустите проект выполнив команды
   - docker-compose build - сборка образа
   - docker-compose up - запуск контейнера
