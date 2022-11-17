from unittest import TestCase

from django.core.exceptions import ValidationError

from testing_demos.web.validators import egn_validator


class EgnValidatorTests(TestCase):
    def test_egn_validator__when_valid__expect_ok(self):
        egn_validator('1234567890')

    def test_egn_validator__when_9_digits_valid__expect_ok(self):
        with self.assertRaises(ValidationError) as context:
            egn_validator('123456789')

        self.assertIsNotNone(context.exception)

    def test_egn_validator__when_11_digits__expect_ok(self):
        with self.assertRaises(ValidationError) as context:
            egn_validator('12345678901')

        self.assertIsNotNone(context.exception)

    def test_egn_validator__when_None__expect_ok(self):
        with self.assertRaises(ValidationError) as context:
            egn_validator('')

        self.assertIsNotNone(context.exception)

    def test_egn_validator__when_non_digit_char_valid__expect_ok(self):
        with self.assertRaises(ValidationError) as context:
            egn_validator('1234567s9')

        self.assertIsNotNone(context.exception)
