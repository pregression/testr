from django.utils.timezone import now

ESTABLISHED_YEAR = 2018


def current_year(request):
    return {
        'current_year': __get_current_year(),
    }


def established_year(request):
    return {
        'established_year': ESTABLISHED_YEAR,
    }


def formatted_copyright_year(request):
    y = __get_current_year()
    e = ESTABLISHED_YEAR
    formatted = str(y)
    if y > e:
        formatted = '{} - {}'.format(e, y)

    return {
        'formatted_copyright_year': formatted,
    }


def __get_current_year():
    return now().year
