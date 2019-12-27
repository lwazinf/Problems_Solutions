from django.contrib import admin
from django.urls import path
from search.views import search, like, dislike

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search, name='home'),
    path('none', like, name='like'),
    path('none2', dislike, name='dislike'),
]
