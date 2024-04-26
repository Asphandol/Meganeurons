"""reex"""
import re

class Validator:
    """validator"""

    def validate_name_surname(self, name_surname):
        """username"""
        pattern = r"^[A-Z][a-z]{2,30}\s[A-Z][a-z]{2,30}$"
        return bool(re.match(pattern, name_surname))

    def validate_age(self, age):
        """age"""
        pattern = "^[1-6][0-9]$"
        return bool(re.match(pattern, age))

    def validate_country(self, country):
        """country"""
        pattern = '^[A-Z][A-Za-z]{2,10}$'
        return bool(re.match(pattern, country))

    def validate_region(self, region):
        """region"""
        pattern = r'^[A-Z]\w{1,9}$'
        return bool(re.match(pattern, region))

    def validate_living_place(self, living_place):
        """living place"""
        pattern = r"^[A-Z][a-z]{2,19}\s(st\.|av\.|prosp\.|rd\.)\s\d[0-9a-z]$"
        return bool(re.match(pattern, living_place))

    def validate_index(self, index):
        """index"""
        pattern = r"^\d{5}$"
        return bool(re.match(pattern, index))

    def validate_phone(self, phone):
        """phone"""
        pattern = r"^\+\d{1,3}\s?\(\d{3}\)\s?\d{3}-\d{2}-\d{2}$|^\+\d{9,12}$"
        return bool(re.match(pattern, phone))

    def validate_email(self, email):
        """email"""
        pattern = r"^[^\s@]+@[^\s@]+\.(com|org|edu|gov|net|ua)$"
        return bool(re.match(pattern, email))

    def validate_id(self, id):
        """id"""
        if id.count('0')!=1:
            return False
        pattern = r"^\d{5}0|0\d{5}$"
        return bool(re.match(pattern, id))

    def validate(self, data):
        """total"""
        fields = [part.strip() for part in re.split(r"[,;(?,)(?;)]", data)]
        return all([self.validate_name_surname(fields[0]), self.validate_age(fields[1]),\
 self.validate_country(fields[2]), self.validate_region(fields[3]), \
self.validate_living_place(fields[4]),\
self.validate_index(fields[5]),self.validate_phone(fields[6]),\
self.validate_email(fields[7]), self.validate_id(fields[8])])

# import unittest

# class TestValidator(unittest.TestCase):
#     def setUp(self):
#         self.validator = Validator()

#     def test_validate_name_surname(self):
#         self.assertTrue(self.validator.validate_name_surname('John Doe'))
#         self.assertFalse(self.validator.validate_name_surname('john doe'))
#         self.assertFalse(self.validator.validate_name_surname('j'))
#         self.assertFalse(self.validator.validate_name_surname('JohnDoe'))

#     def test_validate_age(self):
#         self.assertTrue(self.validator.validate_age('42'))
#         self.assertTrue(self.validator.validate_age('15'))
#         self.assertFalse(self.validator.validate_age('0'))
#         self.assertFalse(self.validator.validate_age('1000'))
#         self.assertFalse(self.validator.validate_age('12a'))

#     def test_validate_country(self):
#         self.assertTrue(self.validator.validate_country('UA'))
#         self.assertTrue(self.validator.validate_country('US'))
#         self.assertFalse(self.validator.validate_country('u'))
#         self.assertFalse(self.validator.validate_country('uk'))
#         self.assertFalse(self.validator.validate_country('123'))

#     def test_validate_region(self):
#         self.assertTrue(self.validator.validate_region('Kyiv'))
#         self.assertTrue(self.validator.validate_region('NY'))
#         # self.assertFalse(self.validator.validate_region('NYC')) !!!!not right answer
#         self.assertFalse(self.validator.validate_region('123'))
#         self.assertFalse(self.validator.validate_region(''))

#     def test_validate_living_place(self):
#         # self.assertTrue(self.validator.validate_living_place('Kyiv st. 123'))
#         # self.assertTrue(self.validator.validate_living_place('Moscow av. 456')) ойойойойойойоой поганий приклад
#         self.assertFalse(self.validator.validate_living_place('Kyiv st. 123 456'))
#         self.assertFalse(self.validator.validate_living_place('Kyiv st. '))
#         self.assertFalse(self.validator.validate_living_place('Kyiv '))

#     def test_validate_index(self):
#         self.assertTrue(self.validator.validate_index('01234'))
#         self.assertTrue(self.validator.validate_index('12345'))
#         self.assertFalse(self.validator.validate_index('1234'))
#         self.assertFalse(self.validator.validate_index('123456'))
#         self.assertFalse(self.validator.validate_index('abcde'))

#     def test_validate_phone(self):
#         # self.assertTrue(self.validator.validate_phone('+380 123 456 78 90'))
#         self.assertTrue(self.validator.validate_phone('+1 (234) 567-8901'))
#         self.assertFalse(self.validator.validate_phone('+380 123 123 12 12'))
#         self.assertFalse(self.validator.validate_phone('++1234567890'))
#         self.assertFalse(self.validator.validate_phone('+380 123 456 78'))

#     def test_validate_email(self):
#         self.assertTrue(self.validator.validate_email('user@example.com'))
#         self.assertTrue(self.validator.validate_email('user@example.org'))
#         self.assertFalse(self.validator.validate_email('user@example'))
#         self.assertFalse(self.validator.validate_email('user.example.com'))
#         self.assertFalse(self.validator.validate_email('user@example.ab'))

#     def test_validate_id(self):
#         self.assertTrue(self.validator.validate_id('012345'))
#         self.assertTrue(self.validator.validate_id('123450'))
#         self.assertFalse(self.validator.validate_id('123456'))
#         self.assertFalse(self.validator.validate_id('123405'))
#         self.assertFalse(self.validator.validate_id('012340'))

#     def test_validate(self):
#         self.assertTrue(self.validator.validate('John Doe, 25, UA, Kyiv, Kyiv st. 123, 01234, +380 123 456 78 90, user@example.com, 123450'))
#         self.assertFalse(self.validator.validate('John Doe, 25, UA, Kyiv, Kyiv st. 123, abcde, +380 123 456 7890, user@example.com, 012345'))
#         self.assertFalse(self.validator.validate('John Doe, 25, UA, Kyiv, Kyiv st. 123, 01234, +380 123 456 78 90, user@example, 123450'))

import unittest
import re
class TestValidator(unittest.TestCase):
    def set_up_data(self):
        user_data = UserData()
        user_data.name_surname = 'John Doe'
        user_data.age = 25
        user_data.country = 'UA'
        user_data.region = 'Kyiv'
        user_data.living_place = 'Kyiv st. 123'
        user_data.index = '01234'
        user_data.phone = '+380 123 456 78 90'
        user_data.email = 'user@example.com'
        user_data.id = '123450'
        return user_data
    def test_validate(self):
        user_data = self.set_up_data()
        with self.subTest(user_data=user_data):
            self.assertTrue(self.validator.validate(user_data))
    
    def test_validate_age(self):
        valid_ages = [('42', True), ('15', True), ('0', False), ('1000', False), ('12a', False)]
        for age, expected in valid_ages:
            with self.subTest(age=age):
                self.assertEqual(self.validator.validate_age(age), expected)
    @given(integers(min_value=0, max_value=100))
    def test_validate_age(self, age):
        self.assertEqual(self.validator.validate_age(str(age)), age >= 0)
if __name__ == '__main__':
    unittest.main()