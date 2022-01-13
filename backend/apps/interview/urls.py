from django.urls import path
from . import views

urlpatterns = [
    path('', views.InterviewList.as_view(), name='application_list'),
    path('add/', views.InterviewAdd.as_view(), name='application_add'),
    path('update/<int:pk>/', views.InterviewUpdate.as_view(),
         name='application_update'),
]
