import os
from secret_store import secret_store

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    PORT = os.environ.get('PORT') or 5000
    MODE = os.environ.get('MODE') or 'production' #'development'

    SECRET_KEY = secret_store.get_secret("app-secret-key", quiet_failure=(MODE=="development")).get("app-secret-key") or 'you-will-never-guess'

    DB_CREDENTIALS = secret_store.get_secret("crimson-db", quiet_failure=(MODE=="development"))
    DEV_POSTGRES_USER = os.environ.get('POSTGRES_USER') or 'postgres'
    DEV_POSTGRES_PW = os.environ.get('POSTGRES_PW') or ''
    SQLALCHEMY_DATABASE_URI = \
        f"postgresql://{DB_CREDENTIALS['username']}:{DB_CREDENTIALS['password']}@minerals.cpti2eeejc4n.us-east-1.rds.amazonaws.com/postgres" \
        if MODE == 'production' \
        else f"postgresql://{DEV_POSTGRES_USER}:{DEV_POSTGRES_PW}@localhost/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    USER_ENABLE_EMAIL = False