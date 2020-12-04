from typing import Optional


def get_environment_variable(var_name) -> Optional[str]:
    # fake method
    return "MY_KEY_ID"


class ServerConnection:
    # Fake Connection class
    def get_secret(self, key_id: str) -> str:
        return "MySecret"


def get_server_connection() -> ServerConnection:
    return ServerConnection()
