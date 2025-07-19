from decimal import Decimal
from enum import Enum
from typing import Optional


class ParcelType(str, Enum):
    DOCUMENT = "Document"
    PERISHABLE = "Perishable"
    FRAGILE = "Fragile"
    NORMAL = "Normal"