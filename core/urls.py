from django.urls import path, include, re_path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from security import views as security_views

from . import views

urlpatterns = [
    path('license/', views.gpl_v3, name='license'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    re_path(r'^csp-report/$', security_views.csp_report, kwargs={'csp_save':True,'csp_log':True}),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^blog/', include(wagtail_urls)),
]
