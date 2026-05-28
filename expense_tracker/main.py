from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

exp = []

current_id = 1


class Expenses(BaseModel):
    expense_name: str
    expense_type: str
    expense_description: str
    expense_price: float
    expense_payment_type: str


@app.post("/expenses/")
def create_expense(expense: Expenses):
    global current_id

    new_expense = {
        "expense_id": current_id,
        "expense_name": expense.expense_name,
        "expense_type": expense.expense_type,
        "expense_description": expense.expense_description,
        "expense_price": expense.expense_price,
        "expense_payment_type": expense.expense_payment_type,
        "is_deleted": False
    }

    exp.append(new_expense)
    current_id += 1

    return {
        "msg": "Expense created successfully",
        "data": new_expense
    }


@app.get("/expenses/")
def get_all_expenses():
    return {
        "msg": "All expenses fetched successfully",
        "data": exp
    }


@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):

    for expense in exp:
        if expense["expense_id"] == expense_id:
            return {
                "msg": "Expense found",
                "data": expense
            }

    return {"msg": "Expense not found"}


@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, updated: Expenses):

    for expense in exp:
        if expense["expense_id"] == expense_id:

            expense["expense_name"] = updated.expense_name
            expense["expense_type"] = updated.expense_type
            expense["expense_description"] = updated.expense_description
            expense["expense_price"] = updated.expense_price
            expense["expense_payment_type"] = updated.expense_payment_type

            return {
                "msg": "Expense updated successfully",
                "data": expense
            }

    return {"msg": "Expense not found"}


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    for expense in exp:
        if expense["expense_id"] == expense_id:
            exp.remove(expense)
            return {
                "msg": "Expense permanently deleted"
            }

    return {"msg": "Expense not found"}


@app.delete("/expenses/soft/{expense_id}")
def soft_delete(expense_id: int):

    for expense in exp:
        if expense["expense_id"] == expense_id:
            expense["is_deleted"] = True
            return {
                "msg": "Expense soft deleted",
                "data": expense
            }

    return {"msg": "Expense not found"}