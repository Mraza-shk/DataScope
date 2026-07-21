"""
Purpose:
Transform raw Adzuna API job data into the internal
DataScope format.
"""


def parse_location(area):
    """
    Convert Adzuna's location area list into
    country, state, and city.
    """

    if not area:
        return {
            "country": None,
            "state": None,
            "city": None
        }

    country = area[0]
    state = area[1] if len(area) >= 2 else None
    city = area[-1]

    return {
        "country": country,
        "state": state,
        "city": city
    }


def transform_job(job):
    """
    Transform one raw Adzuna job into the DataScope schema.
    """

    location = parse_location(job["location"]["area"])

    transformed = {
        "company": {
            "company_name": job["company"]["display_name"]
        },

        "location": {
            "city": location["city"],
            "state": location["state"],
            "country": location["country"],
            "latitude": job.get("latitude"),
            "longitude": job.get("longitude")
        },

        "category": {
            "category_name": job["category"]["label"]
        },

        "contract_type": {
            "contract_type": job.get("contract_type")
        },

        "job": {
            "adzuna_job_id": job["id"],
            "title": job["title"],
            "description": job.get("description"),
            "redirect_url": job["redirect_url"],
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max"),
            "salary_currency": job.get("salary_currency"),
            "source": "Adzuna",
            "created_date": job.get("created")
        }
    }

    return transformed

def transform_jobs(raw_data):
    """
    Transform all jobs from the raw Adzuna API response.
    """

    transformed_jobs = []

    for job in raw_data["results"]:
        transformed_jobs.append(transform_job(job))

    return transformed_jobs