from fastapi import APIRouter, HTTPException, Query, Path
from api.services import get_jobs, get_job_by_id
from api.schemas import JobResponse
from typing import Optional
from typing import Literal
from api.schemas import JobResponse, PaginatedJobsResponse
router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Welcome to the DataScope API!",
        "status": "Running",
        "version": "1.0.0"
    }


@router.get(
    "/jobs",
    response_model=PaginatedJobsResponse,
    tags=["Jobs"],
    summary="Browse available jobs",
    description="""
Search and filter jobs using title, city, state, country,
sorting and pagination.
"""
)
def jobs(
    search: str | None = Query(
    default=None,
    description="Search jobs by title."
),
    city: str | None = Query(
    default=None,
    description="Filter jobs by city."
),
    state: str | None = Query(
    default=None,
    description="Filter jobs by state."
),
    country: str | None = Query(
    default=None,
    description="Filter jobs by country."
),
    sort: Literal["newest", "oldest"] = Query(
    default="newest",
    description="Sort jobs by creation date."
),
    page: int = Query(
    default=1,
    ge=1,
    description="Page number."
),
    limit: int = Query(
    default=20,
    ge=1,
    le=100,
    description="Jobs returned per page."
)
):
    return get_jobs(
    search=search,
    city=city,
    state=state,
    country=country,
    sort=sort,
    page=page,
    limit=limit
)


@router.get(
    "/jobs/{job_id}",
    response_model=JobResponse,
    tags=["Jobs"],
    summary="Get job details",
    description="Retrieve complete information about a specific job using its unique ID."
)
def get_job_details(
    job_id: int = Path(
        ...,
        ge=1,
        description="Unique ID of the job."
    )
):

    job = get_job_by_id(job_id)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found."
        )

    return job