import unittest

class TestMono(unittest.TestCase):
    def test_mono_init(self):
        m1 = Mono(5, 2)
        self.assertEqual(m1.coefficient, 5)
        self.assertEqual(m1.degree, 2)
        self.assertIsNone(m1.next)

        m2 = Mono(5, 0)
        self.assertEqual(m2.coefficient, 5)
        self.assertEqual(m2.degree, 0)
        self.assertIsNone(m2.next)

        m3 = Mono(1, 1)
        self.assertEqual(m3.coefficient, 1)
        self.assertEqual(m3.degree, 1)
        self.assertIsNone(m3.next)

        m4 = Mono(0, 2)
        self.assertEqual(m4.coefficient, 0)
        self.assertEqual(m4.degree, 0)
        self.assertIsNone(m4.next)

    def test_mono_str(self):
        m1 = Mono(5, 2)
        self.assertEqual(str(m1), "Mono: 5x**2")

        m2 = Mono(5, 0)
        self.assertEqual(str(m2), "Mono: 5")

        m3 = Mono(1, 1)
        self.assertEqual(str(m3), "Mono: x")

        m4 = Mono(0, 2)
        self.assertEqual(str(m4), "Mono: 0")

    def test_mono_repr(self):
        m1 = Mono(5, 2)
        self.assertEqual(repr(m1), "Mono(coeff=5, degree=2)")

        m2 = Mono(5, 0)
        self.assertEqual(repr(m2), "Mono(coeff=5, degree=0)")

        m3 = Mono(1, 1)
        self.assertEqual(repr(m3), "Mono(coeff=1, degree=1)")

        m4 = Mono(0, 2)
        self.assertEqual(repr(m4), "Mono(coeff=0, degree=0)")

class TestPolynomial(unittest.TestCase):
    def setUp(self):
        self.m1 = Mono(5, 2)
        self.m2 = Mono(5, 0)
        self.m3 = Mono(1, 1)
        self.m4 = Mono(0, 2)

    def test_polynomial_init(self):
        p1 = Polynomial(self.m1, self.m2, self.m3)
        self.assertEqual(p1.head, self.m1)
        self.assertEqual(p1.head.next, self.m2)
        self.assertEqual(p1.head.next.next, self.m3)

        p2 = Polynomial(Mono(-5, 2), Mono(-3, 1))
        self.assertEqual(str(p2), "Polynomial: -5x**2-3x")

        p3 = Polynomial(Mono(-5, 1), Mono(3, 1))
        self.assertEqual(str(p3), "Polynomial: -5x+3x")

        p4 = Polynomial(Mono(0, 2), Mono(-3, 1))
        self.assertEqual(str(p4), "Polynomial: -3x")

        p5 = Polynomial(self.m1, Polynomial(self.m2, self.m3))
        self.assertEqual(p5.head, self.m1)
        self.assertEqual(p5.head.next, self.m2)
        self.assertEqual(p5.head.next.next, self.m3)

        p6 = Polynomial(self.m1, Polynomial(self.m2, Polynomial(self.m3)))
        self.assertEqual(p6.head, self.m1)
        self.assertEqual(p6.head.next, self.m2)
        self.assertEqual(p6.head.next.next, self.m3)

    def test_polynomial_str(self):
        p1 = Polynomial(self.m1, self.m2, self.m3)
        self.assertEqual(str(p1), "Polynomial: 5x**2+5+x")

        p2 = Polynomial(Mono(-5, 2), Mono(-3, 1))
        self.assertEqual(str(p2), "Polynomial: -5x**2-3x")

        p3 = Polynomial(Mono(-5, 1), Mono(3, 1))
        self.assertEqual(str(p3), "Polynomial: -5x+3x")

        p4 = Polynomial(Mono(0, 2), Mono(-3, 1))
        self.assertEqual(str(p4), "Polynomial: -3x")

    def test_polynomial_repr(self):
        p1 = Polynomial(self.m1, self.m2, self.m3)
        self.assertEqual(repr(p1), "Polynomial(Mono(coeff=5, degree=2) -> Mono(coeff=5, degree=0) -> Mono(coeff=1, degree=1))")

        p7 = Polynomial(self.m1, self.m4, self.m3)
        self.assertEqual(repr(p7), "Polynomial(Mono(coeff=5, degree=2) -> Mono(coeff=0, degree=0) -> Mono(coeff=1, degree=1))")

    def test_polynomial_degree(self):
        p1 = Polynomial(self.m1, self.m2, self.m3)
        self.assertEqual(p1.degree, 2)

        p2 = Polynomial(Mono(-5, 2), Mono(-3, 1))
        self.assertEqual(p2.degree, 2)

        p3 = Polynomial(Mono(-5, 1), Mono(3, 1))
        self.assertEqual(p3.degree, 1)

        p4 = Polynomial(Mono(0, 2), Mono(-3, 1))
        self.assertEqual(p4.degree, 1)

    def test_polynomial_copy(self):
        p6 = Polynomial(self.m1, self.m2, self.m3)
        p_6 = p6.copy()
        self.assertEqual(repr(p_6), repr(p6))
        self.assertIsNot(p_6, p6)

    def test_polynomial_sort(self):
        p1 = Polynomial(self.m1, self.m2, self.m3)
        p1.sort()
        self.assertEqual(str(p1), "Polynomial: 5x**2+x+5")

        p3 = Polynomial(Mono(-5, 1), Mono(3, 1))
        p3.sort()
        self.assertEqual(str(p3), "Polynomial: -5x+3x")

        p7 = Polynomial(self.m1, self.m4, self.m3)
        p7.sort()
        self.assertEqual(repr(p7), "Polynomial(Mono(coeff=5, degree=2) -> Mono(coeff=1, degree=1) -> Mono(coeff=0, degree=0))")

    def test_polynomial_simplify(self):
        p3 = Polynomial(Mono(-5, 1), Mono(3, 1))
        p3.simplify()
        self.assertEqual(str(p3), "Polynomial: -2x")

        p7 = Polynomial(self.m1, self.m4, self.m3)
        p7.simplify()
        self.assertEqual(repr(p7), "Polynomial(Mono(coeff=5, degree=2) -> Mono(coeff=1, degree=1))")

        p8 =Polynomial(Mono(-5, 2), Mono(-3, 1), Mono(-3, 2), Mono(2, 1), Mono(1, 1))
        p8.simplify()
        self.assertEqual(str(p8), "Polynomial: -8x**2")

    def test_polynomial_eval_at(self):
        p1 = Polynomial(self.m1, self.m2, self.m3)
        self.assertEqual(p1.eval_at(0), 5)
        self.assertEqual(p1.eval_at(2), 27)

        p2 = Polynomial(Mono(-5, 2), Mono(-3, 1))
        self.assertEqual(p2.eval_at(0), 0)
        self.assertEqual(p2.eval_at(2), -26)

    def test_polynomial_eq(self):
        p1 = Polynomial(self.m1, self.m2, self.m3)
        p2 = Polynomial(self.m3, self.m2, self.m1)
        self.assertEqual(p1, p2)
        self.assertEqual(p1, Polynomial(self.m1, self.m2, self.m3))
        self.assertEqual(Polynomial(self.m1, self.m1, self.m2), Polynomial(self.m2, Polynomial(self.m1, self.m1)))
        self.assertNotEqual(Polynomial(self.m1, self.m2, self.m3), Polynomial(self.m1, self.m2))
        self.assertNotEqual(Polynomial(self.m1, self.m2, self.m3), 42)
        self.assertEqual(Polynomial(Mono(0, 2), Mono(0, 0), Mono(0, 1)), Polynomial(Mono(0, 1)))

    def test_polynomial_hash(self):
        p1 = Polynomial(self.m1, self.m2, self.m3)
        p2 = Polynomial(self.m3, self.m2, self.m1)
        s = set()
        s.add(p1)
        self.assertIn(p2, s)

    def test_polynomial_derivative(self):
        p1 = Polynomial(self.m1, self.m2, self.m3)
        p8 = p1.derivative
        self.assertEqual(str(p8), "Polynomial: 10x+1")

        p2 = Polynomial(Mono(-5, 2), Mono(-3, 1))
        p9 = p2.derivative
        self.assertEqual(str(p9), "Polynomial: -10x-3")

        p5 = Polynomial(self.m1, Polynomial(self.m2, self.m3))
        self.assertEqual(str(p5.derivative), "Polynomial: 10x+1")
        self.assertEqual(str(p5), "Polynomial: 5x**2+5+x")

    def test_polynomial_add(self):
        p1 = Polynomial(self.m1, self.m2, self.m3)
        p9 = Polynomial(Mono(-10, 1), Mono(-3, 0))
        p10 = p1 + p9
        self.assertEqual(str(p10), "Polynomial: 5x**2-9x+2")
        self.assertEqual(str(p1), "Polynomial: 5x**2+x+5")

        p10 = p1 - p9
        self.assertEqual(str(p10), "Polynomial: 5x**2+11x+8")
        self.assertEqual(str(p1), "Polynomial: 5x**2+x+5")

    def test_polynomial_mul(self):
        p1 = Polynomial(self.m1, self.m2, self.m3)
        p9 = Polynomial(Mono(-10, 1), Mono(-3, 0))
        p11 = p1 * p9
        self.assertEqual(str(p11), "Polynomial: -50x**3-25x**2-53x-15")

        p12 = p9 * 3
        self.assertEqual(str(p12), "Polynomial: -30x-9")

        p13 = 3 * p9
        self.assertEqual(p13, p12)

        self.assertEqual(Polynomial(self.m1, self.m1), 2 * Polynomial(self.m1))
        self.assertEqual(Polynomial(self.m1, self.m1, self.m1), 3 * Polynomial(self.m1))

        p14 = Polynomial(p1 * p9)
        self.assertEqual(p14, p11)

if __name__ == '__main__':
    unittest.main()
