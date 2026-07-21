from sqlalchemy import text

from src.database import engine

#Company Loader

def get_company_id(company_name):
    """
    Return the company_id for the given company name.

    If the company doesn't exist, insert it and return the new ID.
    """

    with engine.begin() as connection:

        # Step 1: Check if company already exists
        result = connection.execute(
            text("""
                SELECT company_id
                FROM companies
                WHERE company_name = :company_name
            """),
            {"company_name": company_name}
        )

        row = result.fetchone()

        if row:
            return row.company_id

        # Step 2: Insert new company
        result = connection.execute(
            text("""
                INSERT INTO companies (company_name)
                VALUES (:company_name)
                RETURNING company_id
            """),
            {"company_name": company_name}
        )

        return result.fetchone().company_id

# Category Loader

def get_category_id(category_name):
    """
    Return the category_id for the given category name.

    If the category doesn't exist, insert it and return the new ID.
    """

    with engine.begin() as connection:

        # Step 1: Check if category already exists
        result = connection.execute(
            text("""
                SELECT category_id
                FROM categories
                WHERE category_name = :category_name
            """),
            {"category_name": category_name}
        )

        row = result.fetchone()

        if row:
            return row.category_id

        # Step 2: Insert new category
        result = connection.execute(
            text("""
                INSERT INTO categories (category_name)
                VALUES (:category_name)
                RETURNING category_id
            """),
            {"category_name": category_name}
        )

        return result.fetchone().category_id
    
from sqlalchemy import text

from src.database import engine

#Contract Type Loader

def get_contract_type_id(contract_type):
    """
    Return the contract_type_id for the given contract type.

    If contract_type is None, return None.
    If the contract type doesn't exist, insert it and return the new ID.
    """

    # Handle missing contract type
    if contract_type is None:
        return None

    with engine.begin() as connection:

        # Step 1: Check if contract type already exists
        result = connection.execute(
            text("""
                SELECT contract_type_id
                FROM contract_types
                WHERE contract_type = :contract_type
            """),
            {"contract_type": contract_type}
        )

        row = result.fetchone()

        if row:
            return row.contract_type_id

        # Step 2: Insert new contract type
        result = connection.execute(
            text("""
                INSERT INTO contract_types (contract_type)
                VALUES (:contract_type)
                RETURNING contract_type_id
            """),
            {"contract_type": contract_type}
        )

        return result.fetchone().contract_type_id
    
# Location Loader

def get_location_id(location):
    """
    Return the location_id for the given location.

    If the location doesn't exist, insert it and return the new ID.
    """

    with engine.begin() as connection:

        # Step 1: Check if location already exists
        result = connection.execute(
            text("""
                SELECT location_id
                FROM locations
                WHERE city = :city
                  AND state = :state
                  AND country = :country
            """),
            {
                "city": location["city"],
                "state": location["state"],
                "country": location["country"]
            }
        )

        row = result.fetchone()

        if row:
            return row.location_id

        # Step 2: Insert new location
        result = connection.execute(
            text("""
                INSERT INTO locations
                (
                    city,
                    state,
                    country,
                    latitude,
                    longitude
                )
                VALUES
                (
                    :city,
                    :state,
                    :country,
                    :latitude,
                    :longitude
                )
                RETURNING location_id
            """),
            {
                "city": location["city"],
                "state": location["state"],
                "country": location["country"],
                "latitude": location["latitude"],
                "longitude": location["longitude"]
            }
        )

        return result.fetchone().location_id

# Job Loader

from sqlalchemy import text

from src.database import engine


def load_job(job_data):
    """
    Load one transformed job into the database.

    Returns the job_id.
    """
    with engine.begin() as connection:

        # -------------------------
        # Check if job already exists
        # -------------------------
        result = connection.execute(
            text("""
                SELECT job_id
                FROM jobs
                WHERE adzuna_job_id = :adzuna_job_id
            """),
            {
                "adzuna_job_id": job_data["job"]["adzuna_job_id"]
            }
        )

        row = result.fetchone()

        if row:
            return row.job_id
        
        # -------------------------
        # Resolve foreign keys
        # -------------------------
        
        company_id = get_company_id(
            job_data["company"]["company_name"]
        )

        location_id = get_location_id(
            job_data["location"]
        )

        category_id = get_category_id(
            job_data["category"]["category_name"]
        )

        contract_type_id = get_contract_type_id(
            job_data["contract_type"]["contract_type"]
        )

        # -------------------------
        # Insert new job
        # -------------------------
        result = connection.execute(
            text("""
                INSERT INTO jobs
                (
                    adzuna_job_id,
                    title,
                    description,
                    redirect_url,
                    salary_min,
                    salary_max,
                    salary_currency,
                    company_id,
                    location_id,
                    category_id,
                    contract_type_id,
                    source,
                    created_date
                )
                VALUES
                (
                    :adzuna_job_id,
                    :title,
                    :description,
                    :redirect_url,
                    :salary_min,
                    :salary_max,
                    :salary_currency,
                    :company_id,
                    :location_id,
                    :category_id,
                    :contract_type_id,
                    :source,
                    :created_date
                )
                RETURNING job_id
            """),
            {
                "adzuna_job_id": job_data["job"]["adzuna_job_id"],
                "title": job_data["job"]["title"],
                "description": job_data["job"]["description"],
                "redirect_url": job_data["job"]["redirect_url"],
                "salary_min": job_data["job"]["salary_min"],
                "salary_max": job_data["job"]["salary_max"],
                "salary_currency": job_data["job"]["salary_currency"],
                "company_id": company_id,
                "location_id": location_id,
                "category_id": category_id,
                "contract_type_id": contract_type_id,
                "source": job_data["job"]["source"],
                "created_date": job_data["job"]["created_date"]
            }
        )

        return result.fetchone().job_id