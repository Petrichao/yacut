from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp
from settings import LENGTH_SHORT_URL

DESCRIPTION_URL = 'Длинная ссылка'
MISSING_DATA = 'Обязательное поле'
ERROR_URL = 'Некорректный URL'
DESCRIPTION_SHORT = 'Ваш вариант короткой ссылки'
ERROR_LEN = 'Длина ссылки не может быть больше 16 символов'
PATTERN_SHORT_URL = r'^[A-Za-z0-9_]+$'
ERROR_SHORT_URL = 'Указано недопустимое имя для короткой ссылки'


class URLForm(FlaskForm):
    original_link = URLField(
        DESCRIPTION_URL,
        validators=[DataRequired(message=MISSING_DATA),
                    URL(require_tld=True, message=ERROR_URL)]
    )
    custom_id = URLField(
        DESCRIPTION_SHORT,
        validators=[
            Length(
                max=LENGTH_SHORT_URL,
                message=ERROR_LEN),
            Optional(),
            Regexp(PATTERN_SHORT_URL,
                   message=ERROR_SHORT_URL)
        ]
    )
    submit = SubmitField('Создать')
