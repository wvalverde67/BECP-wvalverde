#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('about/', views.about, name='about'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu_items_view'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item_view'),
    path('reservations/', views.BookingViewSet.as_view({'get':'list'}), name='reservations'),
    path('reservations/<int:pk>', views.SingleBookingView.as_view(), name='single_reservation'),
]