--dataset summary

SELECT

    COUNT(*) AS total_jobs,

    COUNT(DISTINCT company_name) AS total_companies,

    COUNT(DISTINCT category_name) AS total_categories,

    COUNT(DISTINCT country) AS total_countries,

    COUNT(average_salary) AS jobs_with_salary

FROM vw_job_analytics;