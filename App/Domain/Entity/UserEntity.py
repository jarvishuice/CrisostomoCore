from pydantic import BaseModel, EmailStr, Field, field_validator, validator
import re
from Domain.Exeptions.ExecptionEntity import ExeptionEntity


class UserEntity(BaseModel):
    id: int = None
    name: str = None
    lastname: str = None
    email: EmailStr = None
    password: str = None
    username: str = None
    birthDate: str = None
    phone: str = Field(..., description="number phone user")
    token: str = "NO POSEE TOKEN ACTIVO"
    profilePicture: str = None
    status: int = 2
    dateCreated : str = None
    dateUpdate : str = None

    @field_validator("name")
    def validatorName(cls, v):
        if len(v) < 3 or len(v) > 50:
            raise ValueError("Name must be between 3 and 50 characters long.")
        else:
            return v

    @field_validator('phone')
    def validate_phone_number(cls, value):
        phone_pattern = re.compile(r'^\+\d{9,15}$')
        if not phone_pattern.match(value):
            raise ExeptionEntity(
                'Phone number must be between 9 and 15 digits and can start with +')
        else:
            return value
