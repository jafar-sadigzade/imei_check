# Phone IMEI Registration Checker
This Django application allows users to input their phone's IMEI number to check whether the phone is registered or not. It is designed to provide a simple and efficient way to verify the registration status of mobile devices.

## Features
- User-Friendly Interface: A clean and intuitive web interface for users to input their phone IMEI numbers.
- IMEI Validation: Checks the validity of the inputted IMEI number before processing.
- Registration Status Check: Connects to a backend database or external service to verify if the phone is registered.
- Secure and Reliable: Ensures data privacy and integrity while performing checks.
## Technologies Used
- Backend: Django (Python)
- Frontend:
- Database: PostgreSQL
- API Integration: No yet
## Getting Started
### Prerequisites
- Python 3.x
- Django 3.x or higher
Installation
1. Clone the repository:
git clone https://github.com/jafar-sadigzade/imei_check.git
cd imei_check

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the dependencies:
pip install -r requirements/production.txt

4. Run database migrations:
python manage.py migrate

5. Start the development server:
python manage.py runserver

6. Open your browser and navigate to:
http://127.0.0.1:8000/

## Usage
Enter IMEI Number: On the home page, users can input their phone's IMEI number.
Check Registration: Submit the IMEI number to check if the phone is registered.
View Results: The application will display whether the phone is registered or not based on the verification result.
## Project Structure
- app/: Contains the main application code including views, models, and templates.
- static/: Contains static files such as CSS, JavaScript, and images.
- templates/: Contains HTML templates for rendering the web pages.
- manage.py: Django's command-line utility for administrative tasks.
## Contributing
We welcome contributions! Please read our Contributing Guidelines for more information on how to get involved.
## Contact
If you have any questions, feel free to reach out to us at:

- Email: jafarsadigzade@gmail.com
- GitHub: jafar-sadigzade
