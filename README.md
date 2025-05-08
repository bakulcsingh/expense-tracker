# Django Expense Tracker

A comprehensive web application for tracking personal expenses, managing budgets, and visualizing financial data, built with Django and Python.

## Features

- **User Authentication**: Secure registration, login, and profile management
- **Expense Management**: Create, view, update, and delete expenses with categories
- **Budget Planning**: Set budgets for different categories with period tracking
- **Interactive Dashboard**: Visualize spending patterns with charts and graphs
- **Data Filtering**: Sort and filter expenses by date, category, and amount
- **Responsive Design**: Works on desktop and mobile devices
- **Receipt Uploads**: Attach receipts to expense entries
- **Export Functionality**: Download expense reports as CSV or PDF

## Tech Stack

- **Backend**: Django + Python
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: Django Templates, Bootstrap 5, JavaScript
- **Data Visualization**: Chart.js
- **Forms**: django-crispy-forms

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd expense-tracker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**
   ```bash
   # For SQLite (default)
   python manage.py migrate
   
   # For PostgreSQL (edit settings.py first)
   # Uncomment the PostgreSQL config and set your credentials
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Admin interface: `http://127.0.0.1:8000/admin/`

## Project Structure

```
expense_tracker/
├── expense_tracker/         # Main project folder
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configurations
│   └── ...
├── expenses/                # Expense tracking app
│   ├── models.py            # Expense and Category models
│   ├── views.py             # Expense views and logic
│   ├── forms.py             # Expense forms
│   └── ...
├── budgets/                 # Budget management app
│   ├── models.py            # Budget models
│   ├── views.py             # Budget views and logic
│   └── ...
├── dashboard/               # Dashboard visualization app
│   ├── views.py             # Dashboard views and charts
│   └── ...
├── users/                   # User management app
│   ├── models.py            # Extended user profile model
│   ├── views.py             # User authentication views
│   └── ...
├── templates/               # HTML templates
├── static/                  # Static files (CSS, JS, images)
└── media/                   # User uploaded files (receipts)
```

## Usage

1. **Register an account** on the application
2. **Set up expense categories** (e.g., Food, Transportation, Utilities)
3. **Add your expenses** with dates, amounts, and optional receipts
4. **Create budgets** for different categories
5. **Visualize your spending** on the dashboard
6. **Generate reports** to analyze your financial habits

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## Deployment

For production deployment:

1. Set `DEBUG = False` in `settings.py`
2. Configure a production-ready database (PostgreSQL recommended)
3. Set up a proper web server (Nginx, Apache) with WSGI
4. Configure static and media file serving
5. Set up SSL for secure communication

## License

This project is licensed under the MIT License - see the LICENSE file for details.
