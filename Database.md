# Database Schema Documentation

This document outlines the database schema for the E-commerce Admin API, explaining each table's purpose, structure, and relationships.

## Overview

The database consists of three main tables:
- `products`: Stores product information
- `sales`: Records sales transactions
- `inventory`: Tracks stock levels for products

## Tables

### Products Table

**Table Name**: `products`

**Purpose**: Stores information about all products available in the e-commerce system.

**Columns**:
- `id` (Integer, Primary Key): Unique identifier for each product
- `name` (String, 255 chars): Product name
- `category` (String, 100 chars): Product category for classification
- `price` (Float): Product price

**Relationships**:
- One-to-many with `sales`: A product can be associated with multiple sales
- One-to-one with `inventory`: Each product has exactly one inventory record


### Sales Table

**Table Name**: `sales`

**Purpose**: Records all sales transactions, including which products were sold, quantities, and revenue.

**Columns**:
- `id` (Integer, Primary Key): Unique identifier for each sale
- `product_id` (Integer, Foreign Key): References the product that was sold
- `quantity` (Integer): Number of units sold in this transaction
- `total_price` (Float): Total revenue from this sale
- `sale_date` (DateTime): When the sale occurred (defaults to current time)

**Relationships**:
- Many-to-one with `products`: Many sales can reference the same product


### Inventory Table

**Table Name**: `inventory`

**Purpose**: Tracks current stock levels for each product and when they were last updated.

**Columns**:
- `id` (Integer, Primary Key): Unique identifier for each inventory record
- `product_id` (Integer, Foreign Key): References the product this inventory belongs to
- `stock_level` (Integer): Current quantity in stock
- `updated_at` (DateTime): When the inventory was last updated

**Relationships**:
- One-to-one with `products`: Each inventory record belongs to exactly one product


## Relationships Diagram

```
┌───────────┐       ┌───────────┐       ┌───────────┐
│           │       │           │       │           │
│  Products │◄──────┤   Sales   │       │ Inventory │
│           │       │           │       │           │
└─────┬─────┘       └───────────┘       └─────▲─────┘
      │                                       │
      │                                       │
      └───────────────────────────────────────┘
```