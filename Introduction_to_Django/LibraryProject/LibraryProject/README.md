LibraryProject

## Overview

LibraryProject is a Django-based web application designed to manage a library system. It allows users to browse, borrow, and return books, as well as manage their accounts.

## Features

- User authentication and authorization
- Book catalog with search functionality
- Borrowing and returning books
- User account management
- Admin interface for managing books and users

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/LibraryProject.git
    ```
2. Navigate to the project directory:
    ```bash
    cd LibraryProject
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```bash
    python manage.py migrate
    ```
5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Log in with your credentials
- Browse the book catalog and manage your account

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
