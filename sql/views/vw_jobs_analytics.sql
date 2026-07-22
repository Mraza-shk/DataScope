
--Purpose:
--Provide one clean, analyst-friendly row per job posting by joining
--all commonly used business information into a single reusable dataset.

CREATE OR REPLACE VIEW vw_job_analytics AS

SELECT

    -- Job Information

    j.job_id,
    j.adzuna_job_id,
    j.title,
    j.description,
    j.redirect_url,

    -- Company

    c.company_name,

    -- Category

    cat.category_name,

    -- Location

    l.city,
    l.state,
    l.country,

    -- Employment

    ct.contract_type,

    -- Salary

    j.salary_min,
    j.salary_max,

    CASE
        WHEN j.salary_min IS NOT NULL
         AND j.salary_max IS NOT NULL
        THEN (j.salary_min + j.salary_max) / 2.0
        ELSE NULL
    END AS average_salary,

    j.salary_currency,

    -- Metadata

    j.source,
    j.created_date

FROM jobs j

INNER JOIN companies c
ON j.company_id = c.company_id

INNER JOIN locations l
ON j.location_id = l.location_id

INNER JOIN categories cat
ON j.category_id = cat.category_id

LEFT JOIN contract_types ct
ON j.contract_type_id = ct.contract_type_id;

SELECT *
FROM vw_job_analytics;