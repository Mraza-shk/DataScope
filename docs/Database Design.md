# ADR 004 — Database Design

## Status

Draft

---

## Objective

Design a relational database capable of storing historical job market information.

---

## Design Goals

- Avoid duplicate records
- Maintain data integrity
- Support analytical SQL queries
- Enable dashboard reporting
- Allow future expansion

---

## Initial Tables

jobs

Stores job postings.

companies

Stores employer information.

locations

Stores city and country information.

skills

Stores standardized skills.

job_skills

Bridge table for many-to-many relationships.

---

## Design Principles

- Primary Keys
- Foreign Keys
- Normalization
- Proper indexing
- Analytics-friendly schema

---

## Future Enhancements

- Salary history
- Skill trends
- Company hiring trends
- Historical snapshots