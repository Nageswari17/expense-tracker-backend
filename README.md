# Expense Sharing Backend 

This is a backend system designed for an expense sharing application similar to Splitwise.

## Features
- Equal expense split
- Exact amount split
- Percentage split
- Balance tracking (who owes whom)
- Balance simplification
- REST APIs using FastAPI

## Tech Stack
- Python
- FastAPI
- Uvicorn

## API Endpoints
- POST /expense/equal
- POST /expense/exact
- POST /expense/percent
- GET  /balances

## How to Run Locally
pip install -r requirements.txt  
uvicorn main:app --reload

Swagger UI available at:
http://127.0.0.1:8000/docs
