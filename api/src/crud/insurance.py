from tortoise.exceptions import IntegrityError

from models.models import InsuranceBase


async def create_insurance_base_tariff(base):
    # Checking for records with the same cargo_type and overlapping dates
    overlapping_entries = await InsuranceBase.filter(
        cargo_type=base.cargo_type,
        start_date__lte=base.end_date,
        end_date__gte=base.start_date
    ).exists()

    if overlapping_entries:
        raise IntegrityError("A record with the same cargo_type and overlapping date range already exists.")
    else:
        return await InsuranceBase.create(**base.dict())

async def get_insurance_base(date, cargo_type):
    return await InsuranceBase.get_or_none(cargo_type=cargo_type, start_date__lte=date, end_date__gte=date)