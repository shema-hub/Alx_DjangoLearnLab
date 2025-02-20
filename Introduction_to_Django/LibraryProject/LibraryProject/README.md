# Django LibraryProject

A web application for managing a digital bookstore. Users can browse books, add them to a cart, and purchase them. The platform includes an admin panel for managing books, orders, and users.

## 🚀 Features
- User authentication (registration, login, logout)
- Book listings with categories and search functionality
- Shopping cart and order management
- Admin panel for managing books and orders
- API endpoints for book data

## 🏗️ Tech Stack
- Django (Backend Framework)
- SQLite/PostgreSQL (Database)
- Bootstrap (Frontend Styling)
- JavaScript (Optional Enhancements)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/LibraryProject.git
   cd LibraryProject
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the app:**
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## 🔑 Environment Variables
Create a `.env` file in the root directory and add:

```plaintext
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-database-url
```

## ✅ Running Tests
Run the test suite with:
```bash
python manage.py test
```

## 📜 License
This project is licensed under the MIT License.

---
Made with ❤️ using Django.

