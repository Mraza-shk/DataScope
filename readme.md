# 📊 DataScope -- A Product by Mohammadraza Shaikh

**DataScope** is a full-stack job analytics platform built around a modular ETL pipeline, a normalized PostgreSQL database, and a FastAPI backend. It collects job listings from the Adzuna API, transforms and stores them in a relational database, and exposes a clean REST API for searching, filtering, and analyzing jobs.

The long-term goal of the project is to provide an interactive web platform for exploring job market trends and opportunities.

---

# Features

## Backend

* FastAPI REST API
* PostgreSQL relational database
* Modular ETL architecture
* Normalized database design
* Pydantic response validation
* Interactive Swagger documentation

## Job Search

* Search by job title
* Filter by city
* Filter by state
* Filter by country
* Pagination
* Sorting (Newest / Oldest)
* Individual job detail endpoint

---

# Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL

### ETL

* Requests
* Python Dotenv

### API Source

* Adzuna Jobs API

---

# Project Structure

```text
DataScope/
│
├── api/
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   └── services.py
│
├── config/
│
├── data/
│   ├── processed/
│   └── raw/
│
├── database/
│
├── docs/
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── logs/
│
├── src/
│
├── .env.example
├── requirements.txt
└── README.md
```

---

# API Endpoints

## Home

```
GET /
```

Returns API status information.

---

## Browse Jobs

```
GET /jobs
```

Supports:

* Search
* City filter
* State filter
* Country filter
* Pagination
* Sorting

Example:

```
/jobs?search=data&city=Pune&state=Maharashtra&country=India&sort=newest&page=1&limit=20
```

---

## Job Details

```
GET /jobs/{job_id}
```

Returns complete information for a specific job.

---

# Database Design

The project uses a normalized PostgreSQL schema with separate tables for:

* Jobs
* Companies
* Locations
* Categories
* Contract Types
* ETL Runs

This minimizes duplication and improves maintainability.

---

# ETL Workflow

```
Adzuna API
      │
      ▼
Extract
      │
      ▼
Transform
      │
      ▼
Load
      │
      ▼
PostgreSQL
      │
      ▼
FastAPI
      │
      ▼
Frontend
```

---

# Current Status

## Completed

* PostgreSQL database
* Normalized schema
* ETL pipeline
* FastAPI backend
* Search
* Pagination
* Sorting
* City filtering
* State filtering
* Country filtering
* Job detail endpoint
* Swagger API documentation

## In Progress

* Frontend application
* Deployment
* Data quality improvements
* Dashboard & analytics

---

# Project Goal

Build a production-ready job analytics platform that enables users to explore, search, and analyze job market data through a clean web interface backed by a scalable data pipeline.

---

# License

This project is open for learning and portfolio purposes. All rights reserved to Author

---
# Author

Mohammadraza Shaikh | Aspiring Data Engineer and Analyst
