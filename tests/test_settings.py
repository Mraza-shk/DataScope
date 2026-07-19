from config.settings import (
    ADZUNA_APP_ID,
    ADZUNA_API_KEY,
    ADZUNA_BASE_URL,
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DATABASE_URL,
)


print("\n Testing API configuration...")

assert ADZUNA_APP_ID is not None
assert ADZUNA_API_KEY is not None

print(" API configuration passed")


print("\n Testing database variables...")

assert DB_HOST is not None
assert DB_PORT is not None
assert DB_NAME is not None
assert DB_USER is not None
assert DB_PASSWORD is not None

print(" Database variables passed")


print("\n Testing DATABASE_URL...")

assert DATABASE_URL.startswith("postgresql://")
assert DB_USER in DATABASE_URL
assert DB_HOST in DATABASE_URL
assert DB_PORT in DATABASE_URL
assert DB_NAME in DATABASE_URL

print(" DATABASE_URL passed")


print("\n All settings tests passed!")