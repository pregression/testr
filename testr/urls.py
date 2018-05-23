"""testr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include, re_path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from core.views import report_csp

# TODO: https://docs.djangoproject.com/en/2.0/ref/contrib/sitemaps/
sitemaps = {}

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^tellme/', include('tellme.urls')),
    re_path(r'^robots.txt', include('robots.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^report-csp/$', report_csp, name="report_csp"),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^blog/', include(wagtail_urls)),
]

urlpatterns += i18n_patterns(
    path(r'accounts/', include('allauth.urls')),
    path('projects/', include('projects.urls')),
    path('', include('marketing.urls')),
    re_path(r'', include('core.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
