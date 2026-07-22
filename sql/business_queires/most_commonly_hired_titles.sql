--most commonly hired titles
SELECT
    title,
    COUNT(*) AS total_jobs

FROM vw_job_analytics

GROUP BY title

ORDER BY total_jobs DESC

LIMIT 20;