from random import randint

from mimesis import Generic, Locale


class DataGenerator:
    generate = Generic(Locale.EN)

    @classmethod
    def name(cls):
        return cls.generate.person.name()

    @classmethod
    def email(cls):
        return cls.generate.person.email()

    @staticmethod
    def age(min_value: int = 18, max_value: int = 120):
        return randint(min_value, max_value)

    @staticmethod
    def address():
        return "123 Main St"

    @staticmethod
    def phone_number():
        return "+12345678901"

    @staticmethod
    def role(role: str = "user"):
        return role

    @staticmethod
    def referral_code():
        return "ABCDEFGH"
