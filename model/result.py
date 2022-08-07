from dataclasses import dataclass, field


def create_table() -> dict:
    error_table = {"00": ["OK", "Operation successful"],
                   "01": ["Agent username not found", "Invalid username or password"],
                   "02": ["Agent password incorrect", "Invalid username or password"],
                   "99": ["Unknown error", "Try again or contact system administrator"],
                   "03": ["Duplicate email address", "User email already registered"],
                   "04": ["Customer has open accounts", "Cannot delete a customer with open accounts"],
                   "05": ["Account balance is not 0", "Account balance must be 0 to be deleted"],
                   "06": ["Overdraft exceeded", "Value exceeds minimum balance"],
                   "07": ["Quantity limit exceeded", "Weekly movements exceeded"],
                   "08": ["Amount limit exceeded", "Weekly amount exceeded"],
                   "09": ["Destination account not found", "Check destination account"],
                   "10": ["Destination account not valid", "Use transfer own option"],
                   "11": ["Destination account not valid", "Use transfer others option"]}

    return error_table


@dataclass(kw_only=True, slots=True)
class Return:
    code: str = "99"
    cause: str = "Unknown error"
    message: str = "Try again or contact system administrator"
    error_table: dict = field(init=False, default_factory=create_table)

    def set_code(self, new_code: str):
        self.code = new_code
        self.cause = self.error_table[new_code]
        self.message = self.error_table[new_code]
