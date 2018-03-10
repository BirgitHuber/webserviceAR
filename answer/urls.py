
from django.conf.urls import url
from . import views

# define the url that are used in app to access the methods
urlpatterns = [
    #../answer/code/
    url(r'^code/$', views.code_return, name='code'),
    #../answer/code/
    url(r'^image/$', views.image_post, name='image'),
]