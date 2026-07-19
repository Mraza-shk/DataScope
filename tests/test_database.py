from src.database import engine


print("\n Testing database connection...")

connection = engine.connect()

assert connection is not None

connection.close()

print(" Database connection successful!")