# Inventory Management System Django Backend

## About

This project is the backend component of the Inventory Management System. It provides the necessary APIs and logic to handle CRUD operations for managing inventory items and suppliers.

The website associated with this backend can be accessed at [Inventory Management System](https://yejui626.pythonanywhere.com/api/inventory/).

## Table of Contents

- [Installation](#installation)
- [Commands to Know](#commands-to-know)
- [API Documentation](#api-documentation)

## Installation

To run the backend locally, follow these steps:

1. Clone the repository: `git clone https://github.com/yejui626/inventory_management.git`
2. Navigate to the project directory: `cd inventory_management`
3. Install dependencies: `pip install -r requirements.txt`. It is recommended to set up your own virtual environement before installing the dependencies.
4. Run the development server: `python manage.py runserver`.

## Commands to Know

- `python manage.py populate_1000_books.py`: Populate 1000 dummy data into the database.
- `python manage.py migrate`: Apply migrations to create database tables.
- `python manage.py createsuperuser`: Create a superuser to access the Django admin interface.
- `python manage.py makemigrations`: Generate new migrations based on changes to models.
- `python manage.py shell`: Open a Python shell with Django environment loaded.

## API Documentation

### 1. List All Products

- **URL:** `/api/inventory`
- **Method:** GET
- **Description:** Retrieves a list of all products with optional filtering and sorting.
- **Query Parameters:**
  - `category`: Filter products by category.
  - `author`: Filter products by author.
  - `search`: Search products by title.
  - `ordering`: Sort products by a specific field (price, quantity).
- **Example Request:** `GET /api/inventory?category=educational&author=author1&search=book1&ordering=price`


### 2. Get Product by ID

- **URL:** `/api/inventory/{product-id}`
- **Method:** GET
- **Description:** Retrieves information for a specific product.
- **URL Parameters:**
  - `{product-id}`: Unique identifier of the product.
- **Example Request:** `GET /api/inventory/123`
- **Response:** 
  - Status Code: 200 OK
  - Body: JSON object representing the product.

### 3. Add Product

- **URL:** `/api/add-inventory`
- **Method:** POST
- **Description:** Adds a new product to the inventory.
- **Request Body:** JSON object representing the new product.
- **Example Request:** : `{
    "title": "123",
    "author": "John Doe",
    "category": "Fiction",
    "price": 29.99,
    "quantity": 10,
    "publication_date": "2022-01-01",
    "isbn": "978123456789",
    "image_url": "/images/image.png",
    "supplier": {
        "name": "Oxford University Press",
        "contact_person": "Goo Ye Jui",
        "email": "yjyejui626@gmail.com",
        "phone_number": "0184040438",
        "address": "Oxford University Press, Educational Supply Section, North Kettering Business Park, Hipwell Road, Kettering, Northamptonshire. NN14 1UA",
        "currency": "GBP"
    }
}`


### 4. Update Product

- **URL:** `/api/update-inventory/{product-id}`
- **Method:** PUT
- **Description:** Updates information for a product or its supplier.
- **URL Parameters:**
- `{product-id}`: Unique identifier of the product to update.
- **Request Body:** JSON object representing the updated product or supplier information.
- **Example Request:** `{
    "id": 99,
    "supplier": {
        "id": 99,
        "name": "Oxford University Press 99",
        "contact_person": "Goo Ye Jui",
        "email": "yjyejui626@gmail.com",
        "phone_number": "0184040438",
        "address": "Oxford University Press, Educational Supply Section, North Kettering Business Park, Hipwell Road, Kettering, Northamptonshire. NN14 1UA",
        "currency": "GBP"
    },
    "title": "Book9 99",
    "author": "Author9 99",
    "category": "Category 99",
    "price": "172.00",
    "quantity": 21,
    "publication_date": "2023-05-31",
    "isbn": "7963485905972",
    "image_url": "/images/99.png",
    "created_at": "2024-03-13T17:28:53.221047Z",
    "updated_at": "2024-03-15T13:14:15.801100Z"
}`

#### Delete Product

- **URL:** `/api/delete-inventory/{product-id}`
- **Method:** DELETE
- **Description:** Deletes a product from the inventory.
- **URL Parameters:**
- `{product-id}`: Unique identifier of the product to delete.
- **Example Request:** `DELETE /api/delete-inventory/123`


