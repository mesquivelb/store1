Tienda2 – Backend E‑Commerce API
Overview

Tienda2 is a backend REST API for an e‑commerce application built with FastAPI. The project simulates a real online store workflow including authentication, cart management, order checkout, and payment processing.

The main goal of this project is to demonstrate solid backend fundamentals, proper business logic separation, and secure, user‑scoped access control, making it suitable as a portfolio project for a first backend developer role.

Tech Stack

Python 3.13

FastAPI – REST API framework

SQLAlchemy – ORM

PostgreSQL – Database

Pydantic v2 – Data validation

JWT (OAuth2) – Authentication & authorization

Docker & Docker Compose – Containerization

Uvicorn – ASGI server

Project Structure
app/
├── auth/           # Authentication logic (JWT, login, current user)
├── models/         # SQLAlchemy models
├── schemas/        # Pydantic schemas
├── services/       # Business logic layer
├── routers/        # API routes
├── database.py     # DB connection & session
├── main.py         # FastAPI app entry point
Core Features
Authentication

User login with email and password

JWT access token generation

Secure dependency get_current_user_payload

All sensitive routes are protected

Products & Categories

Public read access

Admin‑only create/update/delete

Role‑based access enforced at router level

Cart System

Each user has an isolated cart

Users can only:

View their own cart

Add items to their own cart

Clear their own cart

Cart access is fully protected by JWT

Checkout & Orders

Checkout converts cart items into an order

Order total is calculated server‑side

Product prices cannot be manipulated by the client

Each order belongs to a single user

Order lifecycle:

Cart contains products

Checkout creates an order (status: pending)

Order items are persisted

Payments

Payment endpoint validates:

Order existence

Order ownership

Correct payment amount

Order not already paid

Successful payment updates order status to paid

Security Rules

Users can only access their own:

Cart

Orders

Payments

Admin privileges required for:

Product management

Category management

No trust in client‑side data (price, user_id, totals)

API Documentation

The API is fully documented using Swagger UI.

After running the project, access:

http://localhost:8000/docs

From Swagger you can:

Authenticate using JWT (Authorize button)

Test protected routes

Simulate full purchase flow

Running the Project
Requirements

Docker

Docker Compose

Start the application
docker compose up --build

The API will be available at:

http://localhost:8000
Example Workflow

Register / Login user

Obtain JWT token

Add products to cart

Checkout cart

Pay order

Order status becomes paid

Why This Project Matters

This project demonstrates:

Clean separation between routers, services, and models

Proper authentication and authorization

Realistic e‑commerce business rules

Secure backend design

Dockerized development environment

It goes beyond basic CRUD and reflects real backend responsibilities.

Author

Manuel Alejandro Esquivel Briones

Backend Developer (Python / FastAPI)