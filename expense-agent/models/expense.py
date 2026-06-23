from dataclasses import dataclass


@dataclass
class Expense:
    amount: float
    category: str
    description: str
    expense_date: str