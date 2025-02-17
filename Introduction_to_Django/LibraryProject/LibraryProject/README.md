# LibraryProject

Welcome to the LibraryProject! This project is a simple Django application designed to manage a library system.

## Features

- Add, update, and delete books
- Manage library members
- Track borrowed and returned books
- Search for books and members

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
4. Apply the migrations:
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

- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage the library.
- Use the main application to search for books and manage borrowing.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.