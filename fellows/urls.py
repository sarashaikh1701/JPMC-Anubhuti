from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url('', views.index, name='index'),
    path('fellows-detail/<int:pk>/', views.ViewStudent, name='fellows-detail'),
    url('fellows-list/', views.ShowAll, name='fellows-list'),
    path('fellows-create/', views.CreateStudent, name='fellows-create'),
    path('fellows-update/<int:pk>/', views.UpdateStudent, name='fellows-update'),
    path('fellows-delete/<int:pk>/', views.DeleteStudent, name='fellows-delete'),
    path('api/fellow-list/', views.fellowlist, name='fellow-list'),
    path('api/fellow-detail/<str:pk>/', views.fellowDetail, name='fellow-detail'),
    path('api/fellow-create/', views.fellowCreate, name='fellow-create'),
    path('api/fellow-update/<str:pk>/', views.fellowUpdate, name='fellow-update'),
    path('api/fellow-delete/<str:pk>/', views.fellowDelete, name='fellow-delete'),
]
