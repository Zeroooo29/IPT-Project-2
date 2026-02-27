# Store Management System - Django Application

A comprehensive Django-based store management system with features for product catalog, inventory management, order processing, and staff/customer management.

## Features

### Products Module
- **Product Management**: Add, edit, and manage products with SKU, pricing, and inventory tracking
- **Categories**: Organize products into categories for better organization
- **Suppliers**: Track supplier information and manage relationships
- **Inventory Tracking**: Monitor stock levels with automatic low-stock alerts
- **Inventory History**: Complete audit trail of all stock transactions

### Orders Module
- **Order Management**: Create, track, and manage customer orders
- **Order Items**: Add multiple items to orders with unit pricing
- **Order Status**: Track orders through pending, confirmed, shipped, delivered, and cancelled statuses
- **Order Calculations**: Automatic calculation of totals, taxes, shipping, and discounts
- **Delivery Tracking**: Track shipping and delivery dates

### Customers Module
- **Customer Profiles**: Store detailed customer information
- **Customer Types**: Support for retail, wholesale, and corporate customers
- **Company Information**: Track company details and tax IDs
- **Credit Management**: Manage customer credit limits
- **Order History**: View all orders from each customer

### Staff Module
- **Staff Profiles**: Manage employee information integrated with Django user accounts
- **Department Management**: Organize staff by department (Sales, Warehouse, Accounting, Management)
- **Position Tracking**: Track employee positions and roles
- **Employment Information**: Manage salary, hire date, and employment status

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package installer)
- Virtual Environment

### Step 1: Create Virtual Environment
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install django
```

### Step 3: Run Migrations
The database has already been migrated. If you need to re-migrate:
```bash
python manage.py migrate
```

### Step 4: Create Superuser (if needed)
```bash
python manage.py createsuperuser
```

A default superuser has been created:
- **Username**: admin
- **Password**: admin123
- **Email**: admin@example.com

## Running the Application

Start the development server:
```bash
python manage.py runserver
```

The application will be available at: `http://localhost:8000/`

### Access Admin Panel
Navigate to: `http://localhost:8000/admin/`
- Username: `admin`
- Password: `admin123`

## Project Structure

```
store_management/
├── store_management/          # Main project configuration
│   ├── settings.py           # Project settings
│   ├── urls.py               # Main URL router
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
│
├── products/                 # Products app
│   ├── models.py             # Product, Category, Supplier, InventoryHistory models
│   ├── admin.py              # Admin interface configuration
│   ├── urls.py               # Product URLs
│   └── views.py              # Product views
│
├── orders/                   # Orders app
│   ├── models.py             # Order, OrderItem models
│   ├── admin.py              # Admin interface configuration
│   ├── urls.py               # Order URLs
│   └── views.py              # Order views
│
├── customers/                # Customers app
│   ├── models.py             # Customer model
│   ├── admin.py              # Admin interface configuration
│   ├── urls.py               # Customer URLs
│   └── views.py              # Customer views
│
├── staff/                    # Staff app
│   ├── models.py             # StaffMember model
│   ├── admin.py              # Admin interface configuration
│   ├── urls.py               # Staff URLs
│   └── views.py              # Staff views
│
├── manage.py                 # Django management script
└── db.sqlite3               # SQLite database
```

## API Endpoints

### Products
- `GET /products/` - List all products
- `GET /products/product/<id>/` - View product details
- `GET /products/categories/` - List all categories
- `GET /products/suppliers/` - List all suppliers
- `GET /products/low-stock/` - List low-stock products

### Orders
- `GET /orders/` - List all orders
- `GET /orders/order/<id>/` - View order details
- `GET /orders/customer/<customer_id>/` - View customer orders

### Customers
- `GET /customers/` - List all customers
- `GET /customers/customer/<id>/` - View customer details

### Staff
- `GET /staff/` - List all staff members
- `GET /staff/member/<id>/` - View staff member details
- `GET /staff/department/<department>/` - List staff by department

## Database Models

### Products
- **Category**: Product categories
- **Supplier**: Supplier information
- **Product**: Products with pricing and inventory
- **InventoryHistory**: Transaction log for inventory changes

### Orders
- **Order**: Customer orders with status tracking
- **OrderItem**: Individual items in orders

### Customers
- **Customer**: Customer profiles with contact and credit information

### Staff
- **StaffMember**: Employee profiles linked to Django users

## Admin Features

The Django admin interface provides:
- **Full CRUD operations** for all models
- **Search and filtering** capabilities
- **Inline editing** for related models
- **Proper fieldset organization** for better UX
- **Read-only fields** for audit trails

## Development

### Create Sample Data
Use the Django shell to create sample data:
```bash
python manage.py shell
```

### Run Tests
```bash
python manage.py test
```

### Collect Static Files
```bash
python manage.py collectstatic
```

## Database

The application uses SQLite by default. To use PostgreSQL or MySQL, update the `DATABASES` setting in `store_management/settings.py`.

## Security Notes

⚠️ **Important**: The current settings are for development only. For production:
1. Set `DEBUG = False` in settings.py
2. Change the `SECRET_KEY`
3. Update `ALLOWED_HOSTS`
4. Use environment variables for sensitive data
5. Set up proper user authentication

## Troubleshooting

### Port Already in Use
If port 8000 is already in use:
```bash
python manage.py runserver 8001
```

### Migration Issues
If you encounter migration issues:
```bash
python manage.py showmigrations
python manage.py migrate --fake <app> 0001
python manage.py migrate
```

### Admin Access Issues
If you forgot the admin password, reset it:
```bash
python manage.py changepassword admin
```

## Future Enhancements

- [ ] RESTful API with Django REST Framework
- [ ] User authentication and authorization
- [ ] Advanced reporting and analytics
- [ ] Email notifications for orders
- [ ] Payment gateway integration
- [ ] Barcode/QR code scanning
- [ ] Mobile app integration
- [ ] Multi-warehouse support

## Contributing

To contribute to this project:
1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue in the project repository.
