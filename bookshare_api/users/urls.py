
# _*_ coding=utf8 _*_

from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<username>.+)',views.user_detail),
]

