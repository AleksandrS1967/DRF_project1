import re
from rest_framework.serializers import ValidationError

youtube = ['youtube.com']


def validate_forbidden_words(value):
    """ проверка на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com """
    if value.lower() not in youtube:
        raise ValidationError('Ссылку использовать нельзя')
