## Data Models

### Product

```
id: int
name: str
category: str
price: float
```

### Sale

```
id: int
product_id: int
quantity: int
total_price: float
sale_date: datetime
```

### Inventory

```
id: int
product_id: int
stock_level: int
updated_at: datetime
```

## Error Handling

The API includes comprehensive error handling with appropriate HTTP status codes and error messages. All endpoints are wrapped in try-except blocks to catch and log errors.

