# ADR 003 — Why Modular ETL?

## Status

Accepted

---

## Context

The ETL pipeline could be implemented in either:

1. One large Python script
2. Multiple focused modules

---

## Options Considered

### Single Script

Pros

- Easy to start
- Fewer files

Cons

- Difficult to debug
- Difficult to test
- Difficult to extend
- Poor readability

---

### Modular ETL

Modules

- extract.py
- transform.py
- load.py
- database.py

Pros

- Clear responsibilities
- Easier debugging
- Better testing
- Higher maintainability
- Reusable components

Cons

- Slightly more files

---

## Decision

A modular ETL architecture was selected.

---

## Rationale

Each module follows the Single Responsibility Principle.

Changes in one stage of the pipeline should have minimal impact on other stages.

This mirrors professional software engineering practices.

---

## Consequences

Positive

- Easier maintenance
- Better scalability
- Cleaner architecture

Negative

- More initial planning