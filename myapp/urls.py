
#from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('get_token/', views.getToken),
    path('', views.lobby),
    path('room/', views.room),
    
   
]
