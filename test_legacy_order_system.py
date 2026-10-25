
import unittest
from legacy_order_system import order_total

ITEMS = [
    {'name': 'Notebook', 'category': 'book',
     'price': 300, 'qty': 2},
    {'name': 'USB Drive', 'category': 'electronics',
     'price': 800, 'qty': 1},
]


class TestOrderTotal(unittest.TestCase):

    def test_regular_customer(self):
        self.assertEqual(
            order_total(ITEMS, 'regular', 'standard'), 1500
        )

    def test_student_discount(self):
        self.assertEqual(
            order_total(ITEMS, 'student', 'standard'), 1360
        )

    def test_staff_discount(self):
        self.assertEqual(
            order_total(ITEMS, 'staff', 'standard'), 1430
        )

    def test_standard_delivery(self):
        self.assertEqual(
            order_total(ITEMS, 'regular', 'standard'), 1500
        )

    def test_express_delivery(self):
        self.assertEqual(
            order_total(ITEMS, 'regular', 'express'), 1650
        )

    def test_negative_quantity(self):
        bad_items = [
            {'name': 'Notebook', 'category': 'book',
             'price': 300, 'qty': -2}
        ]

        with self.assertRaises(ValueError):
            order_total(bad_items, 'regular', 'standard')

    def test_negative_price(self):
        bad_items = [
            {'name': 'Notebook', 'category': 'book',
             'price': -300, 'qty': 2}
        ]

        with self.assertRaises(ValueError):
            order_total(bad_items, 'regular', 'standard')


if __name__ == '__main__':
    unittest.main()
