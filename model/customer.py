from dataclasses import dataclass, field


@dataclass(kw_only=True, slots=True)
class Customer:
    customer_id: int
    pin: str
    first_name: str
    last_name: str
    address: str
    phone_number: str
    email: str
    creation_date: str
    agent_id: int
