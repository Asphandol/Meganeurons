import unittest
import re
from validator import *

class TestValidator(unittest.TestCase):

    def setUp(self) -> None:
        self.validator = Validator()


    def test_validate_name_surname_valid_format(self):
        valid_inputs = ["Andrii Bilynskyi"]
        for name_surname in valid_inputs:
            formatter = Validator()
            self.assertTrue(formatter.validate_name_surname(name_surname))

    def test_validate_name_surname_no_words(self):
        invalid_inputs = [
            ("Andrii123",),
            ("Andriibilynskyi",),
            ("123AndriiBilynskyi",),
            ("Andrii bilynskyi123",),
            ("Andrii Bilynsk 123",)
        ]

        for name_surname in invalid_inputs:
            formatter = Validator()
            with self.subTest(input=name_surname[0]):
                self.assertFalse(formatter.validate_name_surname(name_surname[0]))

    def test_validate_name_surname_invalid_capitalization(self):
        invalid_inputs = [
            ("andrii bilynskyi",),
            ("ANDrii Bilynskyi",),
            ("Andrii BilynskI",),
            ("Andrii BilynsKyi",),
            ("Andrii Bilynskyi123")
        ]

        for name_surname in invalid_inputs:
            formatter = Validator()
            with self.subTest(input=name_surname[0]):
                self.assertFalse(formatter.validate_name_surname(name_surname[0]))

    def test_validate_age_valid(self):
        valid_inputs = [16, 18, 23, 67, 98]
        for age in valid_inputs:
            formatter = Validator()
            self.assertTrue(formatter.validate_age(str(age)))

    def test_validate_age_invalid(self):
        invalid_inputs = [0, -1, 100, 150, "abc"]
        for age in invalid_inputs:
            formatter = Validator()
            with self.subTest(input=age):
                self.assertFalse(formatter.validate_age(str(age)))

    def test_validate_country_valid(self):
        valid_inputs = ["UK", "Spain", "India", "Germany", "ARGENTINA", "EGYPT"]
        for country in valid_inputs:
            formatter = Validator()
            self.assertTrue(formatter.validate_country(country))

    def test_validate_country_invalid(self):
        invalid_inputs = [
            "India123",
            "india",
            "India_with_underscores",
            "CountryWithOverTenChars",
            "Country123"
        ]
        for country in invalid_inputs:
            formatter = Validator()
            with self.subTest(input=country):
                self.assertFalse(formatter.validate_country(country))


    def test_validate_region_valid(self):
        valid_inputs = ["MT1", "London", "Paris1", "NYC01"]
        for region in valid_inputs:
            formatter = Validator()
            self.assertTrue(formatter.validate_region(region))

    def test_validate_region_invalid(self):
        invalid_inputs = ["Lond1on", "regionWithTenChars", "RegionW1thDigitsInWrongPlace"]
        for region in invalid_inputs:
            formatter = Validator()
            with self.subTest(input=region):
                self.assertFalse(formatter.validate_region(region))


    def test_validate_living_place_valid(self):
        valid_inputs = ["Koselnytska st. 22", "Moskovskaya av. 1b", "Peremohy prosp. 4c"]
        for living_place in valid_inputs:
            formatter = Validator()
            self.assertTrue(formatter.validate_living_place(living_place))

    def test_validate_living_place_invalid(self):
        invalid_inputs = [
            "Koselnytska Ave. 2a",
            "Malaya Pushkinskaya st. 12b",
            "Prospekt Mazepina 2C",
            "Koselnytska st. twenty",
            "Prospekt peremohy 4",
            "St Vitus Gasse 3a",
            "Prospekt peremohy 4X"
        ]
        for living_place in invalid_inputs:
            formatter = Validator()
            with self.subTest(input=living_place):
                self.assertFalse(formatter.validate_living_place(living_place))

    def test_validate_index_valid(self):
        valid_inputs = ["12345", "67890"]
        for index in valid_inputs:
            formatter = Validator()
            self.assertTrue(formatter.validate_index(index))

    def test_validate_index_invalid(self):
        invalid_inputs = [
            "12345abc",
            "12345A",
            "1a2b3c4d5",
            "67890X",
            "abc123",
            "123"
        ]
        for index in invalid_inputs:
            formatter = Validator()
            with self.subTest(input=index):
                self.assertFalse(formatter.validate_index(index))

    def test_validate_email_valid(self):
        valid_emails = [
            "test@example.com",
            "test.user@edu.ua",
        ]
        for email in valid_emails:
            formatter = Validator()
            self.assertTrue(formatter.validate_email(email))

    def test_validate_email_invalid_username(self):
        invalid_emails = [
            "test@.example.com",
            ".test@example.com",
            "test@example.",
            "test.@example.com",
            "test@example..com",
            "test@example.com@",
            "test@example.com !!!",
            "@example.com",
            "test@example.com123",
            "test@.com"
        ]
        for email in invalid_emails:
            formatter = Validator()
            with self.subTest(input=email):
                self.assertFalse(formatter.validate_email(email))

    def test_validate_email_invalid_domain(self):
        invalid_emails = [
            "test@example",
            "test@.example",
            "test@example.",
            "test@..example",
            "test@example.com@",
            "test@example.com123",
            "test@example!.com",
            "test@example:com",
            "test@example%com",
            "test@example^com",
            "test@example~com"
        ]
        for email in invalid_emails:
            formatter = Validator()
            with self.subTest(input=email):
                self.assertFalse(formatter.validate_email(email))

    def test_validate_email_invalid_type(self):
        invalid_emails = [
            "test@example.com invalid",
            "test@example.com xyz"
        ]
        for email in invalid_emails:
            formatter = Validator()
            with self.subTest(input=email):
                self.assertFalse(formatter.validate_email(email))

    def test_validate_id_valid(self):
        valid_ids = ["012345", "234501", "120345", "512406"]
        for id_str in valid_ids:
            validator = Validator()
            self.assertTrue(validator.validate_id(id_str))

    def test_validate_id_invalid_digits(self):
        invalid_ids = ["1234b5", "1234#5", "1234!5", "12a345", "1234$5"]
        formatter = Validator()
        for invalid_id in invalid_ids:
            with self.subTest(input=invalid_id):
                self.assertFalse(formatter.validate_id(invalid_id))

    def test_validate_id_invalid_length(self):
        invalid_ids = ["123", "45678"]
        formatter = Validator()
        for invalid_id in invalid_ids:
            with self.subTest(input=invalid_id):
                self.assertFalse(formatter.validate_id(invalid_id))

    def test_validate_id_no_zero(self):
        invalid_ids = ["123455"]
        formatter = Validator()
        for invalid_id in invalid_ids:
            with self.subTest(input=invalid_id):
                self.assertFalse(formatter.validate_id(invalid_id))

    def test_validate_success(self):
        input_str = "Andrii Bilynskyi,27,Ukraine,Lviv city,Bohdana Khmelnytskoho st. 2a,12345,+380622334567,andrii.bilynskyi@example.com,UA624500"
        self.assertTrue(self.validator.validate(input_str))

    def test_validate_failure_missing_separator(self):
        input_str = "Andrii Bilynskyi,27Ukraine,Lviv city,Bohdana Khmelnytskoho st. 2 a,12345,+380622334567,andrii.bilynskyi@example.com,UA624500"
        self.assertFalse(self.validator.validate(input_str))

    def test_validate_failure_missing_data(self):
        input_str = "name_surname,,,living_place,index,phone,email,id"
        self.assertFalse(self.validator.validate(input_str))

    def test_validate_failure_incorrect_data_format(self):
        input_str = "Andrii Bilynskyi,27UkraineLviv cityBohdana Khmelnytskoho st. 2 a,12345,+380622334567,andrii.bilynskyi@example.com,UA624500"
        self.assertFalse(self.validator.validate(input_str))

# if __name__ == '__main__':
#     unittest.main()
