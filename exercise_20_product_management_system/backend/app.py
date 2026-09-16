from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import csv
from pathlib import Path

app = FastAPI(title="Bank Account Management API")
DATA_FILE = Path(__file__).resolve().parent / "accounts.csv"


class Account(BaseModel):
    id: int = Field(gt=0)
    account_holder: str = Field(min_length=1, max_length=100)
    account_type: str = Field(min_length=1, max_length=30)
    balance: float = Field(ge=0)


def ensure_data_file():
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow(["id", "account_holder", "account_type", "balance"])


def read_accounts():
    ensure_data_file()
    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        return [Account(id=int(row["id"]), account_holder=row["account_holder"], account_type=row["account_type"], balance=float(row["balance"])) for row in csv.DictReader(file)]


def write_accounts(accounts: List[Account]):
    with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "account_holder", "account_type", "balance"])
        for account in accounts:
            writer.writerow([account.id, account.account_holder, account.account_type, account.balance])


@app.get("/accounts", response_model=List[Account])
def list_accounts():
    return read_accounts()


@app.get("/accounts/{account_id}", response_model=Account)
def get_account(account_id: int):
    for account in read_accounts():
        if account.id == account_id:
            return account
    raise HTTPException(status_code=404, detail="Account not found")


@app.post("/accounts", response_model=Account)
def create_account(account: Account):
    accounts = read_accounts()
    if any(item.id == account.id for item in accounts):
        raise HTTPException(status_code=400, detail="Account id already exists")
    accounts.append(account)
    write_accounts(accounts)
    return account


@app.put("/accounts/{account_id}", response_model=Account)
def update_account(account_id: int, account: Account):
    accounts = read_accounts()
    for index, item in enumerate(accounts):
        if item.id == account_id:
            accounts[index] = account
            write_accounts(accounts)
            return account
    raise HTTPException(status_code=404, detail="Account not found")


@app.delete("/accounts/{account_id}")
def delete_account(account_id: int):
    accounts = read_accounts()
    updated = [account for account in accounts if account.id != account_id]
    if len(updated) == len(accounts):
        raise HTTPException(status_code=404, detail="Account not found")
    write_accounts(updated)
    return {"message": "Account deleted successfully"}


@app.get("/")
def root():
    return {"message": "Bank Account Management API is running"}
