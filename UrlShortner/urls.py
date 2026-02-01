from django.contrib import admin
from django.urls import path, include
from shortener.views import redirect_short_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shortener.urls')),
    path('', include('accounts.urls'))
]
