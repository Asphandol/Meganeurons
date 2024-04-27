import unittest

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_validate_name_surname(self):
        self.assertTrue(self.validator.validate_name_surname("Elvis Presley"))
        self.assertFalse(self.validator.validate_name_surname("ElvisPresley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis Presley forever"))
        self.assertFalse(self.validator.validate_name_surname("elvis Presley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis presley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis PResley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis Presleyqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"))
        self.assertFalse(self.validator.validate_name_surname("Elvis P"))
        self.assertFalse(self.validator.validate_name_surname("Elvis P,resley"))
        self.assertFalse(self.validator.validate_name_surname("El1vis Presley"))

    def test_validate_age(self):
        self.assertTrue(self.validator.validate_age("20"))
        self.assertFalse(self.validator.validate_age("7"))
        self.assertFalse(self.validator.validate_age("100"))
        self.assertFalse(self.validator.validate_age("20."))
        self.assertFalse(self.validator.validate_age("20a"))

    def test_validate_country(self):
        self.assertTrue(self.validator.validate_country("Ukraine"))
        self.assertFalse(self.validator.validate_country("U"))
        self.assertFalse(self.validator.validate_country("UUUUUUUUUUUUUUUUUUUUUUU"))
        self.assertFalse(self.validator.validate_country("Ukraine1"))
        self.assertFalse(self.validator.validate_country("ukraine"))
        self.assertTrue(self.validator.validate_country("USA"))

    def test_validate_region(self):
        self.assertTrue(self.validator.validate_region("Lviv"))
        self.assertTrue(self.validator.validate_region("Lviv1"))
        self.assertFalse(self.validator.validate_region("L"))
        self.assertFalse(self.validator.validate_region("lviv"))

    def test_validate_living_place(self):
        self.assertTrue(self.validator.validate_living_place("Koselnytska st. 2a"))
        self.assertFalse(self.validator.validate_living_place("koselnytska st. 2a"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska provulok 2a"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 2"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. a2"))
        self.assertTrue(self.validator.validate_living_place("Koselnytska st. 22"))

    def test_validate_index(self):
        self.assertTrue(self.validator.validate_index("79000"))
        self.assertFalse(self.validator.validate_index("7900"))
        self.assertFalse(self.validator.validate_index("790000"))
        self.assertFalse(self.validator.validate_index("7900q"))
        self.assertFalse(self.validator.validate_index("790 00"))

    def test_validate_phone(self):
        self.assertTrue(self.validator.validate_phone("+380951234567"))
        self.assertTrue(self.validator.validate_phone("+38 (095) 123-45-67"))
        self.assertFalse(self.validator.validate_phone("38 (095) 123-45-67"))
        self.assertFalse(self.validator.validate_phone("380951234567"))
        self.assertFalse(self.validator.validate_phone("-380951234567"))
        self.assertFalse(self.validator.validate_phone("+3810951234567"))
        self.assertTrue(self.validator.validate_phone("+20951234567"))

    def test_validate_email(self):
        self.assertTrue(self.validator.validate_email("username@domain.com"))
        self.assertTrue(self.validator.validate_email("username+usersurname@domain.com"))
        self.assertTrue(self.validator.validate_email("username@ucu.edu.ua"))
        self.assertFalse(self.validator.validate_email("usernamedomain.com"))
        self.assertFalse(self.validator.validate_email("username@domaincom"))
        self.assertFalse(self.validator.validate_email("username@domain.aaa"))
        self.assertFalse(self.validator.validate_email("username@aaa"))
        self.assertFalse(self.validator.validate_email("@domain.com"))

    def test_validate_id(self):
        self.assertTrue(self.validator.validate_id("123450"))
        self.assertTrue(self.validator.validate_id("011111"))
        self.assertFalse(self.validator.validate_id("123456"))
        self.assertFalse(self.validator.validate_id("123006"))
        self.assertFalse(self.validator.validate_id("1230916"))
        self.assertFalse(self.validator.validate_id("12306"))

    def test_validate(self):
        self.assertTrue(self.validator.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450"))
        self.assertTrue(self.validator.validate("Elvis Presley;20;Ukraine;Lviv;Koselnytska st. 2a;79000;+380951234567;username@domain.com;123450"))
        self.assertTrue(self.validator.validate("Elvis Presley; 20; Ukraine; Lviv; Koselnytska st. 2a; 79000; +380951234567; username@domain.com; 123450"))
        self.assertTrue(self.validator.validate("Elvis Presley, 20, Ukraine, Lviv, Koselnytska st. 2a, 79000, +380951234567, username@domain.com, 123450"))

    def test_validate_name_surname_edge_cases(self):
        # Leading/trailing whitespace
        self.assertFalse(self.validator.validate_name_surname(" Elvis Presley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis Presley "))

        # Multiple whitespaces
        self.assertFalse(self.validator.validate_name_surname("Elvis  Presley"))

    def test_validate_age_edge_cases(self):
        # Leading zeros
        self.assertFalse(self.validator.validate_age("01"))
        self.assertFalse(self.validator.validate_age("001"))

    def test_validate_country_edge_cases(self):
        # Empty string
        self.assertFalse(self.validator.validate_country(""))

    def test_validate_region_edge_cases(self):
        # Empty string
        self.assertFalse(self.validator.validate_region(""))

    def test_validate_living_place_edge_cases(self):
        # Leading/trailing whitespace
        self.assertFalse(self.validator.validate_living_place(" Koselnytska st. 2a"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 2a "))

        # Multiple whitespaces
        self.assertFalse(self.validator.validate_living_place("Koselnytska  st. 2a"))

        # Invalid street type
        self.assertFalse(self.validator.validate_living_place("Koselnytska street 2a"))

    def test_validate_index_edge_cases(self):
        # Leading/trailing whitespace
        self.assertFalse(self.validator.validate_index(" 79000"))
        self.assertFalse(self.validator.validate_index("79000 "))

    def test_validate_phone_edge_cases(self):
        # Leading/trailing whitespace
        self.assertFalse(self.validator.validate_phone(" +380951234567"))
        self.assertFalse(self.validator.validate_phone("+380951234567 "))
        self.assertFalse(self.validator.validate_phone(" +38 (095) 123-45-67"))
        self.assertFalse(self.validator.validate_phone("+38 (095) 123-45-67 "))

    def test_validate_email_edge_cases(self):
        # Leading/trailing whitespace
        self.assertFalse(self.validator.validate_email(" username@domain.com"))
        self.assertFalse(self.validator.validate_email("username@domain.com "))

        # Multiple consecutive dots in username
        self.assertFalse(self.validator.validate_email("user..name@domain.com"))

        # Dot at the start/end of username
        self.assertFalse(self.validator.validate_email(".username@domain.com"))
        self.assertFalse(self.validator.validate_email("username.@domain.com"))

    def test_validate_id_edge_cases(self):
        # Leading/trailing whitespace
        self.assertFalse(self.validator.validate_id(" 123450"))
        self.assertFalse(self.validator.validate_id("123450 "))

    def test_validate_edge_cases(self):
        # Leading/trailing whitespace
        self.assertFalse(self.validator.validate(" Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450"))
        self.assertFalse(self.validator.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450 "))

        # Multiple separators
        self.assertFalse(self.validator.validate("Elvis Presley,,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450"))
        self.assertFalse(self.validator.validate("Elvis Presley,20,,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450"))

        # Too few/many parts
        self.assertFalse(self.validator.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com"))
        self.assertFalse(self.validator.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450,extra"))

if __name__ == '__main__':
    unittest.main()
