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
