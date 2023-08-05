from random import choices
from string import ascii_letters, digits
from settings import LENGTH_UNIQUE_SHORT_GENERATE

from .models import URLMap


def get_unique_short():
    '''Генерация ссылки.'''
    while True:
        short_id = ''.join(choices(ascii_letters + digits, k=LENGTH_UNIQUE_SHORT_GENERATE))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id
