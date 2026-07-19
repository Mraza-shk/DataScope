-- ===
-- DataScope Database Schema v1.0
-- Author: Mohammadraza Shaikh
-- Description: Database schema for the DataScope ETL project.
-- ===

-- COMPANIES TABLE

CREATE TABLE IF NOT EXISTS companies (
    company_id SERIAL PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- LOCATIONS TABLE

CREATE TABLE IF NOT EXISTS locations (
    location_id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- CATEGORIES TABLE

CREATE TABLE IF NOT EXISTS categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- CONTRACT TYPES TABLE

CREATE TABLE IF NOT EXISTS contract_types (
    contract_type_id SERIAL PRIMARY KEY,
    contract_type VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- JOBS TABLE

CREATE TABLE IF NOT EXISTS jobs (
    job_id SERIAL PRIMARY KEY,

    adzuna_job_id VARCHAR(100) UNIQUE NOT NULL,

    title VARCHAR(255) NOT NULL,

    description TEXT,

    redirect_url TEXT NOT NULL,

 salary_min NUMERIC(12,2)
    CHECK (salary_min IS NULL OR salary_min >= 0),

salary_max NUMERIC(12,2)
    CHECK (salary_max IS NULL OR salary_max >= salary_min),

    salary_currency VARCHAR(10),

    company_id INTEGER NOT NULL,

    location_id INTEGER NOT NULL,

    category_id INTEGER NOT NULL,

    contract_type_id INTEGER,

source VARCHAR(50)
CHECK (
    source IN (
        'Adzuna'
        )
),

    created_date TIMESTAMP,

    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_company
     FOREIGN KEY (company_id)
     REFERENCES companies(company_id)
     ON DELETE RESTRICT,

    CONSTRAINT fk_location
     FOREIGN KEY (location_id)
     REFERENCES locations(location_id)
     ON DELETE RESTRICT,

    CONSTRAINT fk_category
     FOREIGN KEY (category_id)
     REFERENCES categories(category_id)
     ON DELETE RESTRICT,

    CONSTRAINT fk_contract_type
     FOREIGN KEY (contract_type_id)
     REFERENCES contract_types(contract_type_id)
     ON DELETE RESTRICT
);
-- ETL RUNS TABLE

CREATE TABLE IF NOT EXISTS etl_runs (
    run_id SERIAL PRIMARY KEY,

    start_time TIMESTAMP NOT NULL,

    end_time TIMESTAMP,

status VARCHAR(20)
CHECK (
    status IN 
    ('SUCCESS',
    'FAILED',
    'RUNNING'
    )
),

    records_extracted INTEGER DEFAULT 0,

    records_loaded INTEGER DEFAULT 0,

    error_message TEXT
);

-- INDEXES

CREATE INDEX idx_jobs_company_id
ON jobs(company_id);

CREATE INDEX idx_jobs_location_id
ON jobs(location_id);

CREATE INDEX idx_jobs_category_id
ON jobs(category_id);

CREATE INDEX idx_jobs_created_date_id
ON jobs(created_date);