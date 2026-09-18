from models.database import Base, engine
from models.models import User, Scenario


Base.metadata.create_all(bind=engine)

print("Database initialized successfully.")