from sqlalchemy import text

from src.database import engine

from sqlalchemy import text

from src.database import engine

from math import ceil

def get_jobs(
    search: str | None = None,
    city: str | None = None,
    state: str | None = None,
    country: str | None = None,
    sort: str = "newest",
    page: int = 1,
    limit: int = 20
):

    offset = (page - 1) * limit

    with engine.connect() as connection:

        conditions = []
        parameters = {}

        if search:
            conditions.append(
                "LOWER(j.title) LIKE LOWER(:search)"
            )
            parameters["search"] = f"%{search}%"

        if city:
            conditions.append(
                "LOWER(l.city) = LOWER(:city)"
            )
            parameters["city"] = city

        if state:
            conditions.append(
                "LOWER(l.state) = LOWER(:state)"
            )
            parameters["state"] = state

        if country:
            conditions.append(
                "LOWER(l.country) = LOWER(:country)"
            )
            parameters["country"] = country

        where_clause = ""

        if conditions:
            where_clause = "WHERE " + " AND ".join(conditions)

        order_clause = "ORDER BY j.created_date DESC"

        if sort == "oldest":
            order_clause = "ORDER BY j.created_date ASC"

        total_jobs = connection.execute(
            text(f"""
                SELECT COUNT(*)
                FROM jobs j
                JOIN locations l
                    ON j.location_id = l.location_id
                {where_clause};
            """),
            parameters
        ).scalar()

        parameters["limit"] = limit
        parameters["offset"] = offset

        result = connection.execute(
            text(f"""
                SELECT
                    j.job_id,
                    j.title,
                    j.redirect_url,
                    j.salary_min,
                    j.salary_max,
                    j.created_date
                FROM jobs j
                JOIN locations l
                    ON j.location_id = l.location_id
                {where_clause}
                {order_clause}
                LIMIT :limit
                OFFSET :offset;
            """),
            parameters
        )

        jobs = [dict(row) for row in result.mappings()]

        return {
            "page": page,
            "limit": limit,
            "total_jobs": total_jobs,
            "total_pages": ceil(total_jobs / limit) if total_jobs else 0,
            "jobs": jobs
        }

def get_job_by_id(job_id: int):
    """
    Retrieve a single job by its ID.
    """

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT
                    job_id,
                    title,
                    redirect_url,
                    salary_min,
                    salary_max,
                    created_date
                FROM jobs
                WHERE job_id = :job_id;
            """),
            {
                "job_id": job_id
            }
        )

        job = result.mappings().fetchone()

        if job is None:
            return None

        return dict(job)