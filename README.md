# 🧮 Carpet Inventory Management System

A web-based inventory management system for carpets in a store, built with **Django**. The project allows store managers to add, edit, delete, and view carpet listings with images and availability status.

---

## ✨ Features

- Add, edit, and delete carpets
- List carpets with images and descriptions
- View detailed information for each carpet
- Display availability status (In stock / Out of stock)
- Upload image per carpet
- Fully RTL and Persian interface with custom font

---

## 🧰 Technologies Used

- Python 3
- Django
- HTML5, CSS3
- Bootstrap 5 (RTL version)
- Persian Font: IRANSansWebFaNum

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/parinaz1990/carpetstore.git
cd carpetstore
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  .venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the app in your browser.

---

## 📁 Project Structure

```bash
carpetstore/
│
├── inventory/           # Main Django app
│   ├── models.py        # Carpet model
│   ├── views.py         # View functions
│   ├── templates/       # HTML templates
│   ├── forms.py         # Forms for CRUD
│   └── urls.py
│
├── static/              # Static files (fonts, CSS)
│   └── font/            # IRANSansWebFaNum font files
│
├── media/               # Uploaded carpet images
├── manage.py
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 📸 Screenshots

*You can add some screenshots of your app here.*

---

## 👤 Developer

**[Your Name]**  
GitHub: [https://github.com/parinaz1990](https://github.com/parinaz1990)  
Email: your.email@example.com

---

## 📝 License

This project is licensed under the MIT License.