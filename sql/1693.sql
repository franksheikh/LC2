-- GROUP BY
SELECT
    DISTINCT(date_id),
    make_name,
    COUNT(DISTINCT(lead_id)) as unique_leads,
    COUNT(DISTINCT(partner_id)) as unique_partners
FROM
    DailySales
-- Group rows that have the same values in specified columns
-- Used with aggregate functions
GROUP BY make_name, date_id;

/*
INPUT
| date_id   | make_name | lead_id | partner_id |
| --------- | --------- | ------- | ---------- |
| 2020-12-8 | toyota    | 0       | 1          |
| 2020-12-8 | toyota    | 1       | 0          |
| 2020-12-8 | toyota    | 1       | 2          |
| 2020-12-7 | toyota    | 0       | 2          |
| 2020-12-7 | toyota    | 0       | 1          |
| 2020-12-8 | honda     | 1       | 2          |
| 2020-12-8 | honda     | 2       | 1          |
| 2020-12-7 | honda     | 0       | 1          |
| 2020-12-7 | honda     | 1       | 2          |
| 2020-12-7 | honda     | 2       | 1          |

OUTPUT
| date_id    | make_name | unique_leads | unique_partners |
| ---------- | --------- | ------------ | --------------- |
| 2020-12-07 | honda     | 3            | 2               |
| 2020-12-08 | honda     | 2            | 2               |
| 2020-12-07 | toyota    | 1            | 2               |
| 2020-12-08 | toyota    | 2            | 3               |
*/