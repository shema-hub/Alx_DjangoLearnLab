# LibraryProject

Welcome to the LibraryProject! This project is a simple Django application for managing a library system.

## Features

- Add, update, and delete books
- Manage library members
- Track borrowed books and due dates
- Search for books by title, author, or genre

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/LibraryProject.git
    ```
2. Navigate to the project directory:
    ```bash
    cd LibraryProject
    ```
3. Create a virtual environment:
    ```bash
    python -m venv env
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source env/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Apply the migrations:
    ```bash
    python manage.py migrate
    ```
7. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
8. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin` to manage books and members.
- Use the main application to search for and borrow books.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact [yourname@example.com](mailto:yourname@example.com).
