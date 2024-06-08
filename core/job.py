from core.models import Phone, Recipient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.core.mail import send_mail
from django.conf import settings


def my_job():
    phones = Phone.objects.filter(status="Qeydiyyatdan keçirilməyib!")
    if not phones.exists():
        return

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)

    phones_to_update = []
    emails_to_send = []

    try:
        for phone in phones:
            try:
                # Navigate to the page
                driver.get("https://portal.rinn.az/az/imei-check-service")

                # Find the input field by ID and clear it
                imei_input = wait.until(EC.visibility_of_element_located((By.ID, "imeiCheck")))
                imei_input.clear()

                # Type the phone's IMEI into the input field and press Enter
                imei_input.send_keys(phone.imei)
                imei_input.send_keys(Keys.RETURN)

                # Wait for the modal description to be present
                modal_description = wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, ".modal__content .imei-check-service__modal-description.mb-28"))
                )
                div_text = modal_description.text

                # Check the status in div_text and update accordingly
                if 'Qeydiyyatdan keçib' in div_text:

                    # Add the phone to the list of phones to update
                    phones_to_update.append(phone.id)

                    # Prepare email details
                    subject = "Yeni imei qeydiyyat"
                    body = f"Brand: {phone.brand}\nModel: {phone.model}\nIMEI: {phone.imei}\nNote: {phone.note}"
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [recipient.email for recipient in Recipient.objects.all()]

                    # Add email details to the list of emails to send
                    emails_to_send.append((subject, body, from_email, recipient_list))
                    print(subject, body, from_email, recipient_list)

            except Exception as e:
                print(f"An error occurred for phone IMEI {phone.imei}: {str(e)}")

    finally:
        # Perform bulk update
        Phone.objects.filter(id__in=phones_to_update).update(status='Qeydiyyatdan keçib!')

        # Send emails
        for subject, body, from_email, recipient_list in emails_to_send:
            send_mail(subject, body, from_email, recipient_list)

        # Close the WebDriver
        driver.quit()
