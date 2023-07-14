from uuid import UUID

from _decimal import Decimal
from fastapi import APIRouter

from crud.insurance import create_insurance_base_tariff, get_insurance_base
from schemas.schemas import InsuranceBaseCreate, InsuranceCalculation, InsuranceRate, Insurance


router = APIRouter()

@router.post('/api/insurance/tariff/create', tags=["Insurance Tariff"], response_model=UUID)
async def create_insurance_tariff(base_tariff: InsuranceBaseCreate):
    base_tariff = await create_insurance_base_tariff(base_tariff)
    return base_tariff.id

@router.post('/api/insurance/calculate', tags=["Insurance Calculate"], response_model=InsuranceCalculation)
async def calculate_insurance_(insurance:Insurance):
    base_tariff = await get_insurance_base(date= insurance.date, cargo_type=insurance.type.cargo_type)
    if not base_tariff is None:
        cost = base_tariff.base_value * insurance.type.rate
        return InsuranceCalculation(cost=cost.quantize(Decimal('0.01')))
    else:
        raise ValueError("No base tariff found for this cargo type")
