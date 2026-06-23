from dotenv import dotenv_values
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

config = dotenv_values(".env")
db_url = f"postgresql://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}"
engine = create_engine(db_url)
SessionLocal = sessionmaker(bind=engine)

try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    print("Successfully connected to the sme-learning-db")
except Exception as error:
    print(error)
