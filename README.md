# BECP-wvalverde: Django Restaurant Project

Welcome to my Back-End Capstone Project, a restaurant web application developed with Django and the Django REST Framework.

## Description

This application allows users to view the restaurant menu, make table reservations, and access information about the restaurant. It also provides a RESTful API for interacting with the Menu and Booking models.

## Key features

- Displaying the restaurant menu
- Table reservations for authenticated users
- Restaurant information page
- RESTful API for interacting with the Menu and Booking models

## Installation

To install and run this project, follow these steps:

1. Clone the repository:

git clone https://github.com/wvalverde/restaurant-app.git


2. Create a virtual environment:

pypenv shell

3. Install the requirements:

pipenv install

4. Install the app:

python manage.py makemigrations
python manage.py migrate

5. Assuming you are using MySQL update settings.py with your username and password:
- 'USER': 'admindjango',
- 'PASSWORD': 'employee@123!',


6. Run the development server:
python manage.py runserver

7. Open your web browser and go to http://localhost:8000/restaurant
- Browse the restaurant menu and select the items you want to order.
- Make a reservation by selecting the date, time, and number of guests.
- View your reservations and modify or cancel them if needed.
- Access the restaurant information page to learn more about the establishment.
- Use the API to interact with the Menu and Booking models programmatically.


## Credits

This project was developed by Willie Valverde as a Back-End Capstone Project for the Tech Academy's Python Developer Bootcamp.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
