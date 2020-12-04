from examples.basic_usage import get_environment_variable, get_server_connection
from vardef import vardef


@vardef
def secret_key() -> str:
    print("'secret_key' variable definition started")
    key_id = get_environment_variable("KEY_ID")
    conn = get_server_connection()
    secret = conn.get_secret(key_id)
    print("'secret_key' variable definition finished")
    return secret
