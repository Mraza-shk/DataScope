from src.extract import AdzunaClient


print("Starting Adzuna extraction test...")

client = AdzunaClient()

jobs = client.fetch_jobs()

print("Extraction successful!")
print(type(jobs))

print(jobs.keys())
print(f"Jobs received: {len(jobs['results'])}")
print(jobs["results"][0])