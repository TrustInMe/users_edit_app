class Config(object):
    """
    Конфигурация проекта.
    """

    SQLALCHEMY_DATABASE_URI = "postgresql://default_user:default_password!@pg_db:5432"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "secret_key"