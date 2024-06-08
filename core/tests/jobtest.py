from django.test import TestCase
from unittest.mock import patch, MagicMock
from core.models import Phone, Recipient
from core.job import my_job
from django.conf import settings
from selenium.webdriver.common.by import By
from django.core.mail import send_mail


class MyJobTestCase(TestCase):

    def setUp(self):
        # Create test data
        self.phone1 = Phone.objects.create(
            brand="TestBrand1",
            model="TestModel1",
            imei="123456789012345",
            status="Qeydiyyatdan keçirilməyib!"
        )
        self.phone2 = Phone.objects.create(
            brand="TestBrand2",
            model="TestModel2",
            imei="543210987654321",
            status="Qeydiyyatdan keçirilməyib!"
        )
        self.recipient = Recipient.objects.create(
            name="Test Recipient",
            email="test@example.com"
        )

    @patch('selenium.webdriver.Chrome')
    @patch('django.core.mail.send_mail')
    def test_my_job(self, mock_send_mail, MockWebDriver):
        # Mock the WebDriver and WebDriverWait
        mock_driver = MockWebDriver.return_value
        mock_wait = MagicMock()
        mock_driver_wait = patch('selenium.webdriver.support.ui.WebDriverWait', return_value=mock_wait)
        mock_driver_wait.start()

        # Set up the WebDriver behavior
        mock_imei_input = MagicMock()
        mock_modal_description = MagicMock()
        mock_modal_description.text = 'Qeydiyyatdan keçib!'

        mock_wait.until.side_effect = lambda x: mock_imei_input if x.func == 'find_element' and x.args == (By.ID, "imeiCheck") else mock_modal_description

        # Run the job function
        my_job()

        # Verify the phone statuses are updated
        self.phone1.refresh_from_db()
        self.phone2.refresh_from_db()
        self.assertEqual(self.phone1.status, 'Qeydiyyatdan keçib!')
        self.assertEqual(self.phone2.status, 'Qeydiyyatdan keçib!')

        # Verify emails are sent
        self.assertEqual(mock_send_mail.call_count, 2)

        # Verify email details
        expected_subject = "Yeni imei qeydiyyat"
        expected_body1 = f"Brand: {self.phone1.brand}\nModel: {self.phone1.model}\nIMEI: {self.phone1.imei}\nNote: {self.phone1.note}"
        expected_body2 = f"Brand: {self.phone2.brand}\nModel: {self.phone2.model}\nIMEI: {self.phone2.imei}\nNote: {self.phone2.note}"
        expected_from_email = settings.EMAIL_HOST_USER
        expected_recipient_list = [self.recipient.email]

        mock_send_mail.assert_any_call(expected_subject, expected_body1, expected_from_email, expected_recipient_list)
        mock_send_mail.assert_any_call(expected_subject, expected_body2, expected_from_email, expected_recipient_list)

        # Stop the WebDriverWait patch
        mock_driver_wait.stop()
