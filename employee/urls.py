from django.urls import path
from employee import views

app_name = 'employees'
urlpatterns = [
    path('employees/', views.index, name='index'),
    path('employee/<int:id>/', views.show, name='show'),
    path('create/employee/', views.create, name='create'),
    path('update/employee/<int:id>/', views.update, name='update'),
    path('delete/employee/<int:id>/', views.destroy, name='destroy'),
]