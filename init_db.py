from database import Base, engine
import models

print("Dropping old tables...")
Base.metadata.drop_all(bind=engine)

print("Creating new tables...")
Base.metadata.create_all(bind=engine)

print("Tables recreated successfully!")
