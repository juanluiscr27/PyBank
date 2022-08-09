from dataclasses import dataclass
from datetime import datetime


@dataclass(kw_only=True, slots=True)
class Customer:
    customer_id: int = 0
    pin: str = ""
    first_name: str = ""
    last_name: str = ""
    address: str = ""
    phone_number: str = ""
    email: str = ""
    creation_date: datetime = None
    agent_id: str = ""
