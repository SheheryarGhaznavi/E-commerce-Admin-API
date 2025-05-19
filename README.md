# E-commerce Admin API

A FastAPI-based RESTful API for managing e-commerce operations including products, sales, and inventory.

## Features

- Product management
- Sales recording and analytics
- Inventory tracking and management
- Low stock alerts

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation and settings management
- **MySQL**: Database backend
- **Uvicorn**: ASGI server

## Prerequisites

- Python 3.10+
- MySQL database

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SheheryarGhaznavi/E-commerce-Admin-API.git
cd E-commerce-Admin-API
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following content:

```
DATABASE_URL=mysql+mysqlconnector://user:password@localhost/ecommerce_db
```
Replace `user`, `password`, and database name with your MySQL credentials.

5. Create the database tables:

# Create a script to initialize the database
there is schema.sql file just import that in your mysql and you will be good to go with your demo data

## Running the Application

Start the application with Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

Once the application is running, you can access the interactive API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Products

- `POST /products/`: Create a new product
  - Request body: `name`, `category`, `price`

### Sales

- `POST /sales/`: Record a new sale
  - Request body: `product_id`, `quantity`, `total_price`

- `GET /sales/summary`: Get sales summary between date ranges
  - Query parameters: `start_date`, `end_date`

- `GET /sales/comparison`: Compare revenue between two date ranges
  - Query parameters: `start_1`, `end_1`, `start_2`, `end_2`

### Inventory

- `GET /inventory/low-stock`: Get items with stock below threshold
  - Query parameter: `threshold` (default: 10)

- `PUT /inventory/update`: Update inventory stock level
  - Request body: `product_id`, `stock_level`


## Error Handling

The API includes comprehensive error handling with appropriate HTTP status codes and error messages. All endpoints are wrapped in try-except blocks to catch and log errors.

## Project Structure

```
Fastapi-project/
├── app/
│   ├── models/           # SQLAlchemy models
│   │   ├── product.py
│   │   ├── sale.py
│   │   └── inventory.py
│   ├── routers/          # API route handlers
│   │   ├── product.py
│   │   ├── sale.py
│   │   └── inventory.py
│   ├── schemas/          # Pydantic models for request/response
│   │   ├── product.py
│   │   ├── sale.py
│   │   └── inventory.py
│   ├── database.py       # Database connection
│   └── main.py           # FastAPI application
├── .env                  # Environment variables
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## License

[MIT License](LICENSE)
