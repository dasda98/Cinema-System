from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('repertoire/', views.SeanceView.as_view(), name='search'),
    path('repertoire/buy/<int:seance_id>/', views.BuyTicketView, name='buyticket'),
    path('pricing/', views.PricingView.as_view(), name='pricing')
]
