#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu_items_view'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item_view'),
]