"""Polynomial"""
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
