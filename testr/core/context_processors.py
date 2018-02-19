from django.utils.timezone import now
from django.conf import settings


def current_year(request):
    return {
        'current_year': __get_current_year(),
    }


def established_year(request):
    return {
        'established_year': settings.ESTABLISHED_YEAR,
    }


def formatted_copyright_year(request):
    y = __get_current_year()
    e = settings.ESTABLISHED_YEAR
    formatted = str(y)
    if y > e:
        formatted = '{} - {}'.format(e, y)

    return {
        'formatted_copyright_year': formatted,
    }


def app_name(request):
    return {
        'app_name': settings.APP_NAME,
    }


def title_delimiter(request):
    return {
        'title_delimiter': settings.APP_TITLE_DELIMITER,
    }

def __get_current_year():
    return now().year
