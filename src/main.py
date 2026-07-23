from src.extract import AdzunaClient
from src.transform import transform_jobs
from src.load import load_job


def main():
    print("===================================")
    print("      DataScope ETL Pipeline")
    print("===================================\n")

    # -------------------------
    # Extract
    # -------------------------
    print("Starting extraction...")

    client = AdzunaClient()

    raw_data = client.fetch_multiple_pages(pages=10)

    total_jobs = len(raw_data["results"])

    print(f"✓ Extracted {total_jobs} jobs\n")

    # -------------------------
    # Transform
    # -------------------------
    print("Starting transformation...")

    transformed_jobs = transform_jobs(raw_data)

    print(f"✓ Transformed {len(transformed_jobs)} jobs\n")

    # -------------------------
    # Load
    # -------------------------
    print("Starting load...")

    loaded = 0

    for job in transformed_jobs:
        load_job(job)
        loaded += 1

    print(f"✓ Loaded {loaded} jobs\n")

    print("===================================")
    print(" ETL Pipeline Completed Successfully")
    print("===================================")


if __name__ == "__main__":
    main()