from datetime import date

from _decimal import Decimal
from pydantic import BaseModel
class InsuranceRate(BaseModel):
    cargo_type: str
    rate: Decimal


class InsuranceCalculation(BaseModel):
    cost: Decimal


class InsuranceBaseCreate(BaseModel):
    cargo_type: str
    base_value: Decimal
    start_date: date
    end_date: date

