'''mixtral unittest'''

"""Polynomial 0.61"""
class Mono:
    """Mono"""
    def __init__(self, coefficient:int, degree: int, nexts = None) -> None:
        self.coefficient = coefficient
        self.degree = degree if coefficient!=0 else 0
        self.next = nexts

    def __str__(self) -> str:
        x = 'x**'+str(self.degree)
        coef = self.coefficient
        if self.degree == 1:
            x = 'x'
        elif self.degree == 0:
            x = ''
        if self.coefficient == 1:
            coef = ''
        if self.coefficient == 0:
            return 'Mono: 0'
        if self.coefficient == 1 and self.degree==0:
            coef = 1
        # if self.coefficient == -1 and self.degree==1:
        #     coef = '-'
        return f"Mono: {coef}{x}"

    def __repr__(self) -> str:
        return f'Mono(coeff={self.coefficient}, degree={self.degree})'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Mono):
            return self.coefficient == other.coefficient and self.degree == other.degree
        return False


class Polynomial:
    """polynomial"""
    def __init__(self, *monos) -> None:
        self.degree = 0
        self.head = Mono(None,None)
        curr = self.head
        for mono in monos:
            if isinstance(mono, Polynomial):
                loc_head = mono.head
                while loc_head:
                    curr.next = Mono(loc_head.coefficient, loc_head.degree)
                    curr = curr.next
                    loc_head = loc_head.next
            else:
                curr.next = Mono(mono.coefficient, mono.degree)
                curr = curr.next

        self.head = self.head.next
        curr = self.head
        while curr is not None:
            self.degree = curr.degree if (self.degree<curr.degree \
and curr.coefficient!=0) else self.degree
            curr = curr.next

    def __str__(self) -> str:
        s = str(self.head)[6:] if str(self.head)[6:]!='0' else ''
        current = self.head.next
        while current is not None:
            s += (('' if '-' in str(current)[6:] else '+') + \
(str(current)[6:]) if current.coefficient!=0 else '' )
            current = current.next
        return 'Polynomial: ' + s

    def __repr__(self) -> str:
        s = self.head.__repr__()
        current = self.head.next
        while current is not None:
            s += ' -> ' + repr(current)
            current = current.next
        return f'Polynomial({s})'

    def push(self, mono):
        """push"""
        curr = self.head
        if self.head is None:
            self.head = Mono(mono.coefficient, mono.degree)
            return
        while curr.next:
            curr = curr.next
        curr.next = Mono(mono.coefficient, mono.degree)


    def copy(self):
        """copy"""
        return Polynomial(self)

    @staticmethod
    def swap(ptr1, ptr2):
        """swap"""
        tmp = ptr2.coefficient, ptr2.degree
        ptr2.coefficient, ptr2.degree = ptr1.coefficient, ptr1.degree
        ptr1.coefficient, ptr1.degree = tmp

    def sort(self):
        """sorting"""
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.degree < current.next.degree:
                    self.swap(current, current.next)
                    swapped = True
                current = current.next

    def simplify(self):
        """simplifying"""
        self.sort()
        current = self.head
        while current.next:
            if current.degree == current.next.degree:
                current.coefficient += current.next.coefficient
                current.next = current.next.next
                if current.next:
                    if current.degree != current.next.degree:
                        current = current.next
            elif current.next.coefficient == 0:
                current.next = None
                current = current.next
            else:
                current = current.next
            if not current:
                break
    def eval_at(self, x):
        """evaluating"""
        ans = 0
        current = self.head
        while current:
            ans += current.coefficient * (x ** current.degree)
            current = current.next
        return ans

    def __hash__(self) -> int:
        s = self.copy()
        s.sort()
        return hash(str(s))

    @property
    def derivative(self):
        """derivative"""
        ans = Polynomial()
        current = self.head
        while current:
            if current.degree != 0:
                ans.push(Mono(current.coefficient*current.degree, current.degree-1))
            current = current.next
        return ans

    def __add__(self, other):
        """adding"""
        ans = self.copy()
        current = other.head
        while current:
            ans.push(current)
            current = current.next
        return ans

    def __eq__(self, other: object) -> bool:
        """
        A description of the entire function, its parameters, and its return types.
        """
        if isinstance(other, Polynomial):
            s = self.copy()
            o = other.copy()
            s.sort()
            o.sort()
            return str(s) == str(o)
        return False


import unittest

class TestMono(unittest.TestCase):
    def test_initialization(self):
        m = Mono(2, 3)
        self.assertEqual(m.coefficient, 2)
        self.assertEqual(m.degree, 3)

    def test_zero_coefficient(self):
        m = Mono(0, 5)
        self.assertEqual(m.coefficient, 0)
        self.assertEqual(m.degree, 0)

    def test_next_attribute(self):
        m1 = Mono(2, 3)
        m2 = Mono(3, 2)
        m1.next = m2
        self.assertEqual(m1.next.coefficient, 3)
        self.assertEqual(m1.next.degree, 2)

    def test_str_method(self):
        m = Mono(2, 3)
        self.assertEqual(str(m), 'Mono: 2x**3')

        m2 = Mono(0, 5)
        self.assertEqual(str(m2), 'Mono: 0')

        m3 = Mono(1, 1)
        self.assertEqual(str(m3), 'Mono: x')

        m4 = Mono(1, 0)
        self.assertEqual(str(m4), 'Mono: 1')

        m5 = Mono(-2, 3)
        self.assertEqual(str(m5), 'Mono: -2x**3')

        m6 = Mono(-1, 1)
        self.assertEqual(str(m6), 'Mono: -x')


    def test_str_single_mono(self):
        p = Polynomial(Mono(1, 1))
        self.assertEqual(str(p), 'Polynomial: +x')

    def test_str_multiple_monos(self):
        p = Polynomial(Mono(1, 0), Mono(-2, 1), Mono(3, 2))
        self.assertEqual(str(p), 'Polynomial: +1 + -2x + 3x**2')

    def test_str_multiple_polynomials(self):
        p1 = Polynomial(Mono(1, 0), Mono(-2, 1), Mono(3, 2))
        p2 = Polynomial(Mono(2, 2), Mono(1, 1), Mono(4, 0))
        p = Polynomial(p1, p2)
        self.assertEqual(str(p), 'Polynomial: +1 + -2x + 3x**2 + 2x**2 + 1x + 4')

    def test_str_zero_degree_mono(self):
        p = Polynomial(Mono(1, 0), Mono(0, 0), Mono(-1, 0))
        self.assertEqual(str(p), 'Polynomial: +1 + 0 -1')

    def test_str_polynomial_with_zero_coefficients(self):
        p = Polynomial(Mono(1, 1), Mono(0, 2), Mono(-1, 3))
        p2 = Polynomial(Mono(1, 1), Mono(0, 2), Mono(0, 3), Mono(-1, 4))
        p = Polynomial(p, p2)
        self.assertEqual(str(p), 'Polynomial: +1x + 0x**2 + -1x**3 + 0x**3 + -1x**4')

    def test_str(self):
        p = Polynomial(Mono(1, 0), Mono(-2, 1), Mono(3, 2), Mono(-4, 3))
        self.assertEqual(str(p), 'Polynomial: 1 -2x + 3x**2 - 4x**3')

        p = Polynomial(Mono(0, 0))
        self.assertEqual(str(p), 'Polynomial: 0')

        p = Polynomial(Mono(2, 0), Mono(5, 1))
        self.assertEqual(str(p), 'Polynomial: 2 + 5x')

        p = Polynomial(Mono(5, 2))
        self.assertEqual(str(p), 'Polynomial: 5x**2')

        p = Polynomial(Mono(-5, 2))
        self.assertEqual(str(p), 'Polynomial: - 5x**2')

if __name__ == '__main__':
    unittest.main()