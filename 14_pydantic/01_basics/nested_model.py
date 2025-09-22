from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street="123 something",
    city="Jaipur",
    postal_code="10001"
)

user = User(
    id=1,
    name='vijay',
    address=address
)

user_data = {
    "id":1,
    "name":"Vijay",
    "address":{
        "street":"321 somthing",
        "city":"Paris",
        "postal_code":"2002"
    }
}

user = User(**user_data)
print(user)