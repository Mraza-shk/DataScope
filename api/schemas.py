from datetime import datetime
from typing import Optional
from math import ceil
from pydantic import BaseModel


class JobResponse(BaseModel):
    job_id: int
    title: str
    redirect_url: str

    salary_min: Optional[float] = None
    salary_max: Optional[float] = None

    created_date: datetime


class PaginatedJobsResponse(BaseModel):
    page: int
    limit: int
    total_jobs: int
    total_pages: int
    jobs: list[JobResponse]