from django.urls import path
from . import views

urlpatterns = [
    path('', views.WishList.as_view() , name='home'),
    path('wishlist/create/', views.CreateWish.as_view(), name='list_create'),
    path('wishlist/<int:pk>/delete/', views.DeleteWish.as_view(), name='wish_delete'),

]