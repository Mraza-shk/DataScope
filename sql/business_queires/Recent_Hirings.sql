-- Recent hirings query
SELECT
    title,
    company_name,
    category_name,
    created_date

FROM vw_job_analytics

ORDER BY created_date DESC

LIMIT 20;