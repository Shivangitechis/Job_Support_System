from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApplicationList.as_view(), name='application_list'),
    path('add/', views.ApplicationAdd.as_view(), name='application_add'),
    path('update/<int:pk>/', views.ApplicationUpdate.as_view(),
         name='application_update'),
]
