from config.settings import (
    ADZUNA_APP_ID,
    ADZUNA_API_KEY,
    ADZUNA_BASE_URL,
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)

print("=" * 45)
print("DataScope Configuration Test")
print("=" * 45)

tests = {
    "ADZUNA_APP_ID": ADZUNA_APP_ID,
    "ADZUNA_API_KEY": ADZUNA_API_KEY,
    "ADZUNA_BASE_URL": ADZUNA_BASE_URL,
    "DB_HOST": DB_HOST,
    "DB_PORT": DB_PORT,
    "DB_NAME": DB_NAME,
    "DB_USER": DB_USER,
    "DB_PASSWORD": DB_PASSWORD,
}

all_passed = True

for name, value in tests.items():
    if value:
        print(f"✅ {name:<20} Loaded")
    else:
        print(f"❌ {name:<20} Missing")
        all_passed = False

print("\nConfiguration Status:")
if all_passed:
    print("✅ ALL TESTS PASSED")
else:
    print("❌ TEST FAILED")