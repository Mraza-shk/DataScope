from src.extract import AdzunaClient
from src.transform import transform_jobs
from src.load import load_job

print("DataScope ETL Test\n")

# Extract
client = AdzunaClient()
raw_data = client.fetch_multiple_pages(pages=10)

print(f"✓ Extracted {len(raw_data['results'])} jobs")

# Transform
transformed_jobs = transform_jobs(raw_data)

print(f"✓ Transformed {len(transformed_jobs)} jobs")

# Load
loaded = 0

for job in transformed_jobs:
    load_job(job)
    loaded += 1

print(f"Loaded {loaded} jobs")

print("\nETL Pipeline Completed Successfully!")
