# Spirits Database README

## Overview
The `spirits.db` SQLite database contains information about various spiritual entities, organized into the following tables:

1. **`angels_enoch`**: Angels from the Book of Enoch and their teachings.
2. **`spirits_kabbalah_qliphoth`**: Spirits of the Kabbalah (Sephiroth) and Qliphoth.
3. **`spirits_testament_solomon`**: Spirits and demons from the Testament of Solomon.

This README provides guidance on performing advanced SQL operations, including creating views, using joins, and optimizing queries with indexes.

---

## Advanced Queries

### 1. Retrieve All Spirits with Specific Influences
```sql
SELECT name, description, power_or_influence
FROM spirits_testament_solomon
WHERE power_or_influence LIKE '%destruction%';
```
This query retrieves all spirits from the *Testament of Solomon* table that influence destruction.

---

### 2. Find Kabbalistic Spirits and Their Counterpoints in Qliphoth
```sql
SELECT k.name AS kabbalah_name, k.association AS kabbalah_association,
       q.name AS qliphoth_name, q.association AS qliphoth_association
FROM spirits_kabbalah_qliphoth k
INNER JOIN spirits_kabbalah_qliphoth q
ON k.id = q.id - 10
WHERE k.association LIKE '%Tree of Life%'
  AND q.association LIKE '%Tree of Death%';
```
This query joins the `spirits_kabbalah_qliphoth` table to match the Sephiroth and their corresponding Qliphoth counterparts.

---

### 3. Retrieve All Spirits and Their References
```sql
SELECT 'Angels of Enoch' AS source, name, reference
FROM angels_enoch
UNION ALL
SELECT 'Kabbalah and Qliphoth' AS source, name, reference
FROM spirits_kabbalah_qliphoth
UNION ALL
SELECT 'Testament of Solomon' AS source, name, reference
FROM spirits_testament_solomon;
```
This query aggregates all spirits across tables with their references.

---

### 4. Identify Spirits Without Detailed Descriptions
```sql
SELECT name, association, details
FROM spirits_kabbalah_qliphoth
WHERE details IS NULL OR details = '';
```
This query finds spirits in the *Kabbalah and Qliphoth* table that lack additional descriptive information.

---

### 5. Count Spirits per Source
```sql
SELECT 'Angels of Enoch' AS source, COUNT(*) AS total
FROM angels_enoch
UNION ALL
SELECT 'Kabbalah and Qliphoth' AS source, COUNT(*) AS total
FROM spirits_kabbalah_qliphoth
UNION ALL
SELECT 'Testament of Solomon' AS source, COUNT(*) AS total
FROM spirits_testament_solomon;
```
This query counts the number of spirits in each table.

---

## Views

### Create a View for Comprehensive Spirit Information
```sql
CREATE VIEW comprehensive_spirits AS
SELECT name, teaching AS description, details, reference
FROM angels_enoch
UNION ALL
SELECT name, association AS description, details, reference
FROM spirits_kabbalah_qliphoth
UNION ALL
SELECT name, description, details, reference
FROM spirits_testament_solomon;
```
Use the view to query comprehensive spirit information:
```sql
SELECT * FROM comprehensive_spirits WHERE reference LIKE '%Testament of Solomon%';
```

---

## Indexes

### Create Indexes for Faster Querying
1. Index on `angels_enoch.reference`:
```sql
CREATE INDEX idx_angels_reference ON angels_enoch(reference);
```
2. Index on `spirits_kabbalah_qliphoth.association`:
```sql
CREATE INDEX idx_kabbalah_association ON spirits_kabbalah_qliphoth(association);
```
3. Index on `spirits_testament_solomon.power_or_influence`:
```sql
CREATE INDEX idx_solomon_influence ON spirits_testament_solomon(power_or_influence);
```

---

## Joining Tables

### Combine Data from All Tables
Retrieve all spirits with their teachings or influences:
```sql
SELECT e.name AS spirit_name, e.teaching AS knowledge, e.reference AS source
FROM angels_enoch e
UNION ALL
SELECT k.name AS spirit_name, k.association AS knowledge, k.reference AS source
FROM spirits_kabbalah_qliphoth k
UNION ALL
SELECT s.name AS spirit_name, s.power_or_influence AS knowledge, s.reference AS source
FROM spirits_testament_solomon s;
```

### Join and Analyze Shared References
Find spirits across tables with similar references:
```sql
SELECT a.name AS enoch_spirit, s.name AS solomon_spirit, a.reference
FROM angels_enoch a
INNER JOIN spirits_testament_solomon s
ON a.reference = s.reference;
```

---

## Optimized Query Example
Use the index on `reference` for a faster search:
```sql
SELECT name, teaching
FROM angels_enoch
WHERE reference LIKE '%Book of Enoch 8%';
```

---

This README provides examples of how to query, join, and optimize operations in the `spirits.db` SQLite database. Tailor these queries to suit your specific needs.

