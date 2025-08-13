from django.contrib import admin
from django.urls import path, include
from core.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    # path("test/", test, name="test"),
    path('users/', include('users.urls'))
]
