from re import match, IGNORECASE
from django.shortcuts import redirect
from django.conf import settings


class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        whitelisted = request.path in settings.WHITELIST_ROUTES or any(match(route, request.path, IGNORECASE) for route in settings.WHITELIST_ROUTES)
        if request.user.is_authenticated or request.path == '/' or whitelisted:
            return response

        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
