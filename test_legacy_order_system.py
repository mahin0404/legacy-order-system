
import unittest

from legacy_order_system import order_total, print_receipt


class TestOrderSystem(unittest.TestCase):

    def setUp(self):
        self.items = [
            {'name': 'Notebook', 'category': 'book',
             'price': 300, 'qty': 2},
            {'name': 'USB Drive', 'category': 'electronics',
             'price': 800, 'qty': 1}
        ]

    def test_student_standard_order(self):
        self.assertEqual(
            order_total(self.items, 'student', 'standard'),
            1360.0
        )

    def test_staff_express_order(self):
        self.assertEqual(
            order_total(self.items, 'staff', 'express'),
            1580.0
        )

    def test_negative_quantity(self):
        items = [
            {'name': 'Notebook', 'category': 'book',
             'price': 300, 'qty': -2}
        ]

        with self.assertRaises(ValueError):
            order_total(items, 'student', 'standard')

    def test_negative_price(self):
        items = [
            {'name': 'Notebook', 'category': 'book',
             'price': -300, 'qty': 2}
        ]

        with self.assertRaises(ValueError):
            order_total(items, 'student', 'standard')

    def test_receipt_rejects_negative_quantity(self):
        items = [
            {'name': 'Notebook', 'category': 'book',
             'price': 300, 'qty': -1}
        ]

        with self.assertRaises(ValueError):
            print_receipt(items, 'student', 'standard')


if __name__ == '__main__':
    unittest.main()
