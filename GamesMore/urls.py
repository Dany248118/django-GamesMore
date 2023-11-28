from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('login.urls'), name= 'login'),
    path('catalogos/', include('catalogos.urls'), name='Catalogos' ),
    path('', include('principal.urls'), name='home')
]
