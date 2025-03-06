# cherryinteriordesigns
A comprehensive web application for managing content, products, and user interactions, built with Flask and SQLite3. Features include user authentication, content creation, product management, and M-Pesa payment integration.

# Onlne Market for Housing Interior Designs and Content Management System

## Overview
This project is a comprehensive web application designed for managing content, products, and user interactions. Built with Flask and SQLite3, it features user authentication, content creation, product management, and M-Pesa payment integration.

## Features
- User Authentication (Sign Up, Login, Logout)
- Admin Dashboard for managing content and products
- Content Creation and Management
- Product Management (Add, Update, Delete Products)
- Shopping Cart and Checkout System
- M-Pesa Payment Integration
- Search Functionality
- Profile Management
- Sales Reports (PDF Generation)
- Responsive Design

## Technologies Used
- Flask (Python Web Framework)
- SQLite3 (Database)
- HTML, CSS, JavaScript (Frontend)
- Bootstrap (CSS Framework)
- Quill.js (Rich Text Editor)
- WeasyPrint (PDF Generation)
- M-Pesa API (Payment Integration)

## Installation

### Prerequisites
- Python 3.x
- Flask
- SQLite3

### Steps
1. Clone the repository:
    ```bash
    git clone [https://github.com/Haroldke13/cherryinteriordesigns/]
    cd videoConverter
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Run the application:
    ```bash
    flask run
    ```

6. Access the application at `http://127.0.0.1:5000`.

## Configuration
- Update the configuration settings in [config.py](http://_vscodecontentref_/0) as needed.
- Ensure the M-Pesa credentials are set in the environment variables.

## Usage
- Navigate to the home page to view the available products and services.
- Admin users can log in to access the admin dashboard for managing content and products.
- Users can sign up, log in, and manage their profiles.
- Add products to the cart and proceed to checkout using M-Pesa payment integration.

## Routes
- `/` - Home Page
- `/signup` - User Sign Up
- `/login` - User Login
- `/logout` - User Logout
- `/profile/<int:customer_id>` - User Profile
- `/create_content` - Create New Content (Admin Only)
- `/content` - View All Content
- `/shop` - Shop Page
- `/cart` - Shopping Cart
- `/checkout` - Checkout Page
- `/order-confirmation` - Order Confirmation
- `/admin` - Admin Dashboard
- `/search` - Search Page
- `/search_random/<category>` - Search by Category

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For any inquiries or issues, please contact [your-email@example.com].
