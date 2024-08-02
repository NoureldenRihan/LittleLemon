from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('api/menu/', views.MenuItemsView.as_view()),
    path('api/menu_item/<int:pk>/', views.SingleMenuItemView.as_view()),  
    path('bookings', views.bookings, name='bookings'), 
    path('api/bookings/', views.BookingsView.as_view()),
]