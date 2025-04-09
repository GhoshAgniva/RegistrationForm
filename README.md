# User Registration Form

A simple full-stack web application built with Flask, SQLAlchemy, and Bootstrap that performs CRUD operations on a user registration form.

## 📁 Folder Structure
```
project-directory/
├── main.py
├── db.sqlite3
├── README.md
└── website/
    ├── __init__.py
    ├── models.py
    ├── views.py
    ├── static/
    │   └── (optional CSS files)
    └── templates/
        ├── base.html
        ├── home.html
        ├── add.html
        └── edit.html
```

## 🧰 Technologies Used
- Python
- Flask
- SQLAlchemy
- SQLite
- HTML5
- Bootstrap 5 (via CDN)

## 💡 Features
- Create a new user with the following fields:
  - First Name
  - Last Name
  - Email
  - Date of Birth
  - Gender (Dropdown)
  - Mobile Number (10 digits)
- View all registered users
- Update user information
- Delete user
- Server-side validation with feedback via flash messages

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/flask-registration-app.git
cd flask-registration-app
```

### 2. Create a Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install Flask SQLAlchemy
```

### 4. Run the App
```bash
python main.py
```

App will run on `http://127.0.0.1:5000/`

## 🧪 Validation Rules
- Name: At least 2 characters
- Email: Valid format, must be unique
- DOB: Required
- Gender: Required (dropdown)
- Mobile: Must be 10 digits



## 📬 Submission
After completing the project:
- Push code to a public GitHub repository

---
**Author:** Agniva Ghosh  
