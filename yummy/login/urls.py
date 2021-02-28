from django.urls import path,re_path, include
from django.conf.urls import url
from login import views

urlpatterns = [ 
    path('', views.index, ),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
] 