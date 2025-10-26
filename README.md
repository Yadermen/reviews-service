# ⭐ Reviews & Ratings Service

A microservice built with **FastAPI** and **PostgreSQL** that handles user reviews and product ratings for an online store.  
It provides endpoints for submitting, retrieving, and aggregating feedback, and is designed for integration into a modular e‑commerce architecture.

---

## 📦 Features

- Submit and update product reviews  
- Store and retrieve user ratings  
- Calculate average ratings per product  
- Filter reviews by product, user, or rating  
- Designed for integration with product and order services  

---

## ⚙️ Deployment

### 1. Environment setup

sudo nano .env
pip install -r requirements.txt
python -m app.main
2. Database migrations
Generate a new migration:


alembic revision --autogenerate -m "init"
Apply migrations:


alembic upgrade head
🗂 Project Structure
app/db → database models, sessions, and CRUD logic

app/api → FastAPI routes for reviews and ratings

app/schemas → Pydantic models for request/response validation

app/main.py → FastAPI app entry point

🛠 Tech Stack
Python 3.10+

FastAPI

PostgreSQL

SQLAlchemy

Alembic

Docker (optional)
