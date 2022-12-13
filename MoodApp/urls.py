from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # The mood paths
    path('happy/', views.happy, name='happy'),
    path('sad/', views.sad, name='sad'),
    path('angry/', views.angry, name='angry'),
    path('nervous/', views.nervous, name='nervous'),
]
