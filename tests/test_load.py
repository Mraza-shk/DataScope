
# Testing Company Loader

from src.load import get_company_id

print("Testing Company Loader...\n")

company_id = get_company_id("Neysa")

print(f"Company ID: {company_id}")

# Testing Category Loader

from src.load import get_category_id

print("Testing Category Loader...\n")

category_id = get_category_id("Electronics")

print(f"Category ID: {category_id}")

# Testing Contract Type Loader

from src.load import get_contract_type_id

print("Testing Contract Type Loader...\n")

contract_type_id = get_contract_type_id("Full-Time")

print(f"Contract Type ID: {contract_type_id}")

# Testing Location Loader

from src.load import get_location_id

print("Testing Location Loader...\n")

location_id = get_location_id({
    "city": "New York",
    "state": "NY",
    "country": "USA",
    "latitude": 40.7128,
    "longitude": -74.0060
})

print(f"Location ID: {location_id}")

# Testing ETL Pipeline and Job Loading

from src.extract import AdzunaClient
from src.transform import transform_job
from src.load import load_job

print("Testing ETL Pipeline...\n")

# 1-Extract
client = AdzunaClient()
raw_data = client.fetch_jobs()

# 2-Take the first raw job
raw_job = raw_data["results"][0]

# 3-Transform
transformed_job = transform_job(raw_job)

# 4-Load
job_id = load_job(transformed_job)

print(f"Job loaded successfully! Job ID: {job_id}")