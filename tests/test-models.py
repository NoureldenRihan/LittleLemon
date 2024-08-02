from django.test import TestCase
from restaurant.models import Menu, Booking

# Models Unit Tests

class MenuTest(TestCase):
     def test_get_item(self):
         item = Menu.objects.create(name="Burger", price=80, menu_item_description='Tasty Burger')
         self.assertEqual(item.name, "Burger")
         self.assertEqual(item.price, 80)
         self.assertEqual(item.menu_item_description, "Tasty Burger")

class BookingTest(TestCase):
     def test_get_item(self):
         item = Booking.objects.create(first_name="Nour", reservation_date="2002-08-24", reservation_slot=8)
         self.assertEqual(item.first_name, "Nour")
         self.assertEqual(item.reservation_date, "2002-08-24")
         self.assertEqual(item.reservation_slot, 8)
