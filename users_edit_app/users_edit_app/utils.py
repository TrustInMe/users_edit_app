import hashlib

def make_password_hash(unhashed_password: str) -> str:
    """
    Функция для хеширования паролей.
    """

    m = hashlib.sha256()
    m.update(unhashed_password.encode("utf-8"))
    return m.hexdigest()


def check_password(hash_string: str, password: str) -> bool:
    """
    Функция проверки паролей.
    """

    m = hashlib.sha256()
    m.update(password.encode("utf-8"))
    return True if hash_string == m.hexdigest() else False
