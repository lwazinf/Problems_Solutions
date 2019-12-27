from django.contrib import admin
from django.urls import path
from search.views import search, like, dislike, report

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search, name='home'),
    path('xxxxx00', like, name='like'),
    path('xxxxx01', dislike, name='dislike'),
    path('xxxxx02', report, name='report'),
]
