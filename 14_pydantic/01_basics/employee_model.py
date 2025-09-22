from typing import List, Optional
from pydantic import BaseModel, Field
import re   

class Employee(BaseModel):
    id: int
    name: str
    age: int = Field(
        ...,
        min_length=3,
        max_length=50, 
        # gt=0, 
        description="Age must be a positive integer",
        example="Vijay J"
    )  # ... required
    department: Optional[str] = 'General'  # default value
    salary: float = Field(
        ..., 
        ge=10000, 
        description="Salary must be a positive number"
    )  # ... required

class User(BaseModel):
    email: str = Field(
        ..., 
        regex=r'^\S+@\S+\.\S+$', 
        description="Must be a valid email address"
    )  # ... required
    is_active: bool = True  # default value
    phone: str = Field(
        ...,
        regex=r'^\+?[1-9]\d{1,14}$',
        description="Must be a valid phone number"
    )  # ... required
    age: int = Field(
        ...,
        gt=0,
        le=150,
        description="Age must be a positive integer"
    )  # ... required
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount must be between 0 and 100"
    )  # ... required