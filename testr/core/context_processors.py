from django.utils.timezone import now

ESTABLISHED_YEAR = 2018


def current_year(request):
    return {
        'current_year': now().year,
    }


def established_year(request):
    return {
        'established_year': ESTABLISHED_YEAR,
    }


def formatted_copyright_year(request):
    y = now().year
    e = ESTABLISHED_YEAR
    formatted = y
    if y > e:
        formatted = '{} - {}'.format(e, y)

    return {
        'formatted_copyright_year': formatted,
    }
