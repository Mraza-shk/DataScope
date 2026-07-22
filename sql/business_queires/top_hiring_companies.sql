-- This SQL query retrieves the top hiring companies based on the number of job listings
SELECT
    company_name,
    COUNT(*) AS total_jobs
FROM vw_job_analytics
GROUP BY company_name
ORDER BY total_jobs DESC; 