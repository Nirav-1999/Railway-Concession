from django.conf.urls import url
from . import views
app_name = 'railway'
urlpatterns = [
    url(r'^$',views.RailwayLogin,name = 'login'),
]