from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # <int:pk> >means that Django expects an integer value and 
    # will transfer it to a view as a variable called pk
    # if you enter http://127.0.0.1:8000/post/5/ into your browser, 
    # Django will understand that you are looking for a view called post_detail 
    # and transfer the information that pk equals 5 to that view.
]