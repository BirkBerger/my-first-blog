from django.urls import path
from . import views

urlpatterns = [
    # if http://127.0.0.1:8000/ is input as url,
    # hence the domain name is followed by nothing / the empty string,
    # then view.post_list is shown in the browser
    path('', views.post_list, name='post_list'),

    # create url called post_detail that refers to a view called "views.post_detail"
    # 'post/<int:pk>/' is going to be the url name
    # Django expects and integer and transfer it as "pk" in views.post_detail
    # views.post_detail is a function call in views.py
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]


