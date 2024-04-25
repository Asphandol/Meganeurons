import unittest
from polynomial import *
class PolynomialTests(unittest.TestCase):
    def test_push(self):
        poly1 = Polynomial()
        poly2 = Polynomial(Mono(1, 3), Mono(2, 2))
        mono1 = Mono(1, 2)
        poly1.push(mono1)
        self.assertEqual(str(poly1), "Polynomial: x**2")
        self.assertEqual(str(mono1), "Mono: x**2")

        mono2 = Mono(1, 1)
        poly1.push(mono2)
        self.assertEqual(str(poly1), "Polynomial: x**2+x")
        self.assertEqual(str(mono2), "Mono: x")

        mono3 = Mono(-1, 2)
        poly2.push(mono3)
        self.assertEqual(str(poly2), "Polynomial: x**3+2x**2-x**2")

        mono4 = Mono(-2, 1)
        poly1.push(mono4)
        self.assertEqual(str(poly1), "Polynomial: x**2+x-2x")
        self.assertEqual(str(mono4), "Mono: -2x")

    def test_copy(self):
        poly1 = Polynomial(Mono(1, 3), Mono(2, 2))
        poly3 = poly1.copy()
        self.assertEqual(str(poly3), str(poly1))
        self.assertIsNot(poly1, poly3)

    def test_sort(self):
        # Create an unsorted polynomial
        poly = Polynomial(Mono(3, 1), Mono(2, 2), Mono(1, 3))

        # Call the sort method
        poly.sort()

        # Test that the sorted polynomial is in increasing order by degree
        current = poly.head
        while current.next:
            self.assertGreaterEqual(current.degree, current.next.degree)
            current = current.next


    def test_simplify(self):
        # Create a polynomial that needs to be simplified
        poly = Polynomial(Mono(4, 2), Mono(1, 2), Mono(2, 2), Mono(2, 1))

        # Create another polynomial with the same monos
        poly1 = Polynomial(Mono(4, 2), Mono(1, 2), Mono(2, 2), Mono(2, 1))

        # Call the simplify method
        poly.simplify()
        poly1.simplify()

        # Check that the original and simplified polynomials are equal
        self.assertEqual(str(poly1), str(poly))

    def test_eval_at(self):
        # Create a polynomial
        poly = Polynomial(Mono(3,3), Mono(2,2), Mono(1,1))
        # Test evaluating the polynomial at a specific value
        x = 2
        expected = 3*(2**3)+2*(2**2)+1*(2**1)
        self.assertEqual(poly.eval_at(x), expected)

        # Test evaluating the polynomial at a negative value
        x = -1
        expected = 3 * (-1**3) + 2 * (-1**2) + 1 * (-1**1)
        self.assertEqual(poly.eval_at(x), expected)

        # Test evaluating the polynomial at zero
        x = 0
        self.assertEqual(poly.eval_at(x), 1)

    def test_hash(self):
        # Create two different polynomials
        c1 = Polynomial(Mono(2,3), Mono(5,2))
        c2 = Polynomial(Mono(2,2), Mono(1,3))
        c4 = c2

        # Verify that the polynomials are not equal but have the same hash value
        self.assertNotEqual(c1, c4)
        self.assertEqual(hash(c2), hash(c4))

        # Verify that the polynomials have different hash value
        self.assertNotEqual(hash(c1), hash(c2))

    def test_derivative(self):
        # Create a polynomial and its derivative
        original = Polynomial(Mono(4,3), Mono(3,2), Mono(2,1))
        expected = Polynomial(Mono(12,3), Mono(6,1))
        derived = original.derivative
        self.assertEqual(derived, expected)

    def test_add(self):
        # Create two different polynomials
        selfi = Polynomial(Mono(1,3), Mono(2,2), Mono(5,1))
        other = Polynomial(Mono(3,3), Mono(4,2), Mono(1,1))
        expected = Polynomial(Mono(4,3), Mono(6,2), Mono(6,1))
        added = selfi + other
        self.assertEqual(str(added), str(expected))

    def test_mul(self):
        # Create two different polynomials
        p1 = Polynomial(Mono(1,2), Mono(2,1))
        p2 = Polynomial(Mono(3,3), Mono(1,2), Mono(2,1))
        expected = Polynomial(Mono(3,4), Mono(2,2),Mono(2,3), Mono(1,1), Mono(1,5))
        mul = p1 * p2
        self.assertEqual(str(mul),str(expected))

if __name__ == '__main__':
    unittest.main()
