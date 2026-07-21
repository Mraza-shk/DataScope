from src.extract import AdzunaClient
from src.transform import transform_jobs
from src.io import save_json, load_json

print("Starting Adzuna extraction test...")

client = AdzunaClient()

raw_jobs = client.fetch_jobs()

print("Extraction successful!")

print("Saving raw API response...")
save_json(raw_jobs, "data/raw/jobs.json")
print("Raw data saved successfully!")

# Transform the raw jobs into the DataScope schema
transformed_jobs = transform_jobs(raw_jobs)
# save the transformed jobs to a JSON file
save_json(
    transformed_jobs,
    "data/processed/jobs_processed.json"
)

print("\nTransformation completed successfully!")

print(f"Raw jobs: {len(raw_jobs['results'])}")
print(f"Processed jobs: {len(transformed_jobs)}")

print("\nProcessed data saved to:")
print("data/processed/jobs_processed.json")

