from django.urls import path
from . import views

urlpatterns = [
    # if http://127.0.0.1:8000/ is input as url,
    # hence the domain name is followed by nothing / the empty string,
    # then view.post_list is shown in the browser
    path('', views.post_list, name='post_list'),
    # add url to the post_detail link. post_datail is a view
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]


