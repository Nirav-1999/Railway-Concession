from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'railway'
urlpatterns = [
    url(r'^$',views.RailwayLogin,name = 'login'),
    url(r'^table/',views.StudentDetailView.as_view(), name = 'table'),
    path('ticket/<int:pk>/',views.ticketview, name = 'ticket'),
]