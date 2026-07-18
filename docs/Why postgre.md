# ADR 001 — Why PostgreSQL?

## Status

Accepted

---

## Context

The project requires a relational database to store live job market data collected through an automated ETL pipeline.

The database should support:

- Complex SQL queries
- Large datasets
- Data integrity
- Integration with Power BI
- Scalability for future projects

---

## Options Considered

### MySQL

Pros
- Easy to learn
- Popular
- Good performance

Cons
- Less feature-rich for analytical workloads
- Slightly less common in modern data engineering stacks

---

### PostgreSQL

Pros
- Industry standard for analytics and data engineering
- Excellent SQL compliance
- Advanced indexing
- Strong support for JSON
- Powerful window functions
- Highly extensible
- Open source

Cons
- Slightly steeper learning curve

---

## Decision

PostgreSQL was selected as the primary database.

---

## Rationale

Project 3 is designed to bridge Data Analytics and Data Engineering.

Learning PostgreSQL provides skills directly applicable to modern analytics, ETL pipelines, and cloud data platforms.

---

## Consequences

Positive

- Industry-relevant experience
- Better SQL capabilities
- Easier transition to cloud databases

Negative

- Initial learning curve compared to MySQL