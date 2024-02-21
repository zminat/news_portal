from django import template


register = template.Library()


class StrException(Exception):
    pass


CENSOR_WORDS = {
    'Редиска': 'Р******',
    'редиска': 'р******',
    'редиске': 'р******',
}


@register.filter()
def censor(text):
    if not (isinstance(text, str)):
        raise StrException('Variable is not a string')

    for key in CENSOR_WORDS:
        text = text.replace(key, CENSOR_WORDS[key])
    return text
