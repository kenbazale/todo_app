from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('completed/<int:todo_id>',views.completed,name='complete'),
    path('deletecompleted',views.deletecompleted,name='deletecompleted'),
]
