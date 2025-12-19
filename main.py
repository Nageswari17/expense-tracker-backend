from fastapi import FastAPI
from schemas import EqualExpenseRequest, ExactExpenseRequest, PercentExpenseRequest
from services.split_service import equal_split, exact_split, percent_split
from services.balance_service import update_balance, simplify

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Expense Tracker Backend is running",
        "docs": "/docs"
    }

# EQUAL SPLIT
@app.post("/expense/equal")
def add_equal_expense(request: EqualExpenseRequest):
    splits = equal_split(request.users, request.amount)
    update_balance(request.paid_by, splits)
    return {"message": "Equal expense added"}

# EXACT SPLIT
@app.post("/expense/exact")
def add_exact_expense(request: ExactExpenseRequest):
    splits = exact_split(request.splits)
    update_balance(request.paid_by, splits)
    return {"message": "Exact expense added"}

# PERCENT SPLIT
@app.post("/expense/percent")
def add_percent_expense(request: PercentExpenseRequest):
    splits = percent_split(request.percentages, request.total_amount)
    update_balance(request.paid_by, splits)
    return {"message": "Percent expense added"}

@app.get("/balances")
def get_balances():
    return simplify()
