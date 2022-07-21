from dataclasses import dataclass

from db.agent import AgentModel


@dataclass(kw_only=True, slots=True)
class Agent:
    username: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
    position_id: int = ""

    def login(self, username, password, result):

        AgentModel.validate_agent(self, username, result)

        if result.code == "00":
            if self.password == password:
                result.set_code("02")