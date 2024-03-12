from django.urls import path
from .views import my_first,members,home_views,remaining_views,add_task_views,delete_views,completed_views,task_views

urlpatterns = [
    #path('', members, name='members'),
    #path('my_first/', my_first, name='members'),
    path('',home_views,name='home'),
    path('completed/',completed_views,name='completed'),
    path('remaining/',remaining_views,name='remaining'),
    path('add_task',add_task_views,name='add_task'),
    path('delete/',delete_views,name='delete'),
    path('task_details',task_views,name='task_details'),


]
