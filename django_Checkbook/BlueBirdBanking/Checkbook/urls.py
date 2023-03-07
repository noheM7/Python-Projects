from django.urls import path
from . import views
from .models import Account, Transaction

urlpatterns = [

    path('', views.home, name='index'),
    path('create/', views.create_account, name='create'),
    path('<int:pk>/balance/', views.balance, name='balance'),
    path('transaction/', views.transaction, name='transaction')
]