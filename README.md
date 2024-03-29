# Airbnb Clone Project with Django

This repository contains the source code for an Airbnb clone web application implemented using Django, a high-level Python web framework. The project aims to replicate some of the core features of Airbnb, allowing users to list properties, search for listings, book accommodations, and manage their bookings.

## Features

- **User Authentication**: Allow users to sign up, log in, and manage their accounts securely.
- **Property Listings**: Enable users to list their properties for rent, including details such as description, location, amenities, and pricing.
- **Search and Filter**: Implement a search and filtering functionality to allow users to find properties based on various criteria like location, price range, amenities, etc.
- **Booking Management**: Enable users to book properties for specific dates and manage their bookings.
- **Reviews and Ratings**: Allow users to leave reviews and ratings for properties they have stayed in.
- **Admin Dashboard**: Provide an admin interface to manage user accounts, property listings, bookings, and other aspects of the application.

## Installation

**1. Clone the repository:**

   git clone https://github.com/your-username/airbnb-clone-django.git

**2. Navigate into the project directory:**

  cd airbnb-clone-django

**Install dependencies:**

  pip install -r requirements.txt
  Perform database migrations:

  python manage.py migrate
  Start the development server:

  python manage.py runserver
  Access the application at http://localhost:8000 in your web browser.

## Usage
**Create a superuser to access the admin dashboard:**

  python manage.py createsuperuser
  Visit http://localhost:8000/admin and log in with the credentials of the superuser.

**Use the admin dashboard to manage users, property listings, bookings, etc.**

**Explore the application by signing up, listing properties, searching for listings, making bookings, etc.**

## Contributing
**Contributions are welcome! If you'd like to contribute to this project, please follow these steps:**

  Fork the repository.
  Create a new branch (git checkout -b feature-branch).
  Make your changes.
  Commit your changes (git commit -am 'Add new feature').
  Push to the branch (git push origin feature-branch).
  Create a new Pull Request.

## Acknowledgements
The project structure and implementation are inspired by the official Django documentation and various Django tutorials.

**Special thanks to the contributor @salmane ben messoud**
