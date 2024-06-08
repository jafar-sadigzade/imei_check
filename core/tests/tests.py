from django.test import TestCase
from core.models import Phone, Recipient


class PhoneModelTest(TestCase):

    def setUp(self):
        self.phone = Phone.objects.create(
            brand="Samsung",
            model="Galaxy S21",
            imei="123456789012345",
            note="Test phone",
            status="Qeydiyyatdan keçib!"
        )

    def test_phone_creation(self):
        self.assertEqual(self.phone.brand, "Samsung")
        self.assertEqual(self.phone.model, "Galaxy S21")
        self.assertEqual(self.phone.imei, "123456789012345")
        self.assertEqual(self.phone.note, "Test phone")
        self.assertEqual(self.phone.status, "Qeydiyyatdan keçib!")
        self.assertIsNotNone(self.phone.added_date)

    def test_phone_str(self):
        self.assertEqual(str(self.phone), "Samsung Galaxy S21 - 123456789012345")


class RecipientModelTest(TestCase):

    def setUp(self):
        self.recipient = Recipient.objects.create(
            name="John Doe",
            email="john.doe@example.com"
        )

    def test_recipient_creation(self):
        self.assertEqual(self.recipient.name, "John Doe")
        self.assertEqual(self.recipient.email, "john.doe@example.com")

    def test_recipient_str(self):
        self.assertEqual(str(self.recipient), "John Doe")
