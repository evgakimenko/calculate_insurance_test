import uuid

from tortoise.models import Model
from tortoise import fields

class InsuranceBase(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    cargo_type = fields.CharField(max_length=255)
    base_value = fields.DecimalField(max_digits=5, decimal_places=2)
    start_date = fields.DateField()
    end_date = fields.DateField()

    class Meta:
        name = "insurance_base"