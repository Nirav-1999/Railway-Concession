from django.conf.urls import url
from . import views
app_name = 'railway'
urlpatterns = [
    url(r'^$',views.RailwayLogin,name = 'login'),
    url(r'^table',views.StudentDetailView.as_view(), name = 'table'),
    url(r'^ticket/(?P<pk>[0-9]+)/$',views.ticketview.as_view(), name = 'ticket'),
]