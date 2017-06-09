from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.post_list, name = 'post_list'),
    url(r'^post/(?P<pk>[\w\-]+)/$',views.post_detail, name='post_detail'),
]