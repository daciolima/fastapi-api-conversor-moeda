from pydantic import BaseModel, Field, validator
from typing import List
import re

class ConverterSchema(BaseModel):
    price: float = Field(gt=0)
    to_currencies: List[str]

    @validator('to_currencies')
    def validate_to_currencies(cls, value): # Função de classe
        for currency in value:
            if not re.match('^[A-Z]{3}$', currency):
                raise ValueError(f'Invalid currence{currency}')
            return value
       
class ConverterSchemaOutput(BaseModel):
    message: str
    data: List[dict]





