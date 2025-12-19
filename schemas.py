from pydantic import BaseModel
from typing import List

class EqualExpenseRequest(BaseModel):
    paid_by: int
    users: List[int]
    amount: float
from pydantic import BaseModel
from typing import List, Dict

class ExactExpenseRequest(BaseModel):
    paid_by: int
    splits: Dict[int, float]   # user_id -> amount

class PercentExpenseRequest(BaseModel):
    paid_by: int
    percentages: Dict[int, float]  # user_id -> percent
    total_amount: float
