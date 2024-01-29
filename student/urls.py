from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>',views.view_student,name='view_student'),
    path('add/',views.add,name='add'),
]