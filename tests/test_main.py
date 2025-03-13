import unittest
from src.main import calculate_order_total, apply_discount

class TestOrderFunctions(unittest.TestCase):
    def test_calculate_order_total(self):
        items = [
            {'name': 'Product 1', 'price': 10.0, 'quantity': 2},
            {'name': 'Product 2', 'price': 15.0, 'quantity': 1}
        ]
        self.assertEqual(calculate_order_total(items), 35.0)
    
    def test_apply_discount(self):
        self.assertEqual(apply_discount(100, 20), 80.0)
        
        # Test invalid discount
        with self.assertRaises(ValueError):
            apply_discount(100, 101)

if __name__ == '__main__':
    unittest.main()