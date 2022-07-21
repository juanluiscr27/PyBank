from dataclasses import dataclass, field


def create_table() -> dict:
    error_table = {"00": ["OK", "Operation successful"],
                   "01": ["Agent username not found", "Invalid username or password"],
                   "02": ["Agent password incorrect", "Invalid username or password"],
                   "99": ["Unknown error", "Try again or contact system administrator"]}
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