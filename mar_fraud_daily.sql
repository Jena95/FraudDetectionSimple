{{ config(
    materialized='incremental',
    partition_by={'field': 'report_date','data_type':'date'}
) }}

SELECT
  DATE(ts) AS report_date,
  card,
  COUNTIF(risk_flag = 'HIGH') AS high_risk_txns,
  SUM(amount) AS daily_volume
FROM {{ ref('stg_transactions') }}
GROUP BY 1,2
HAVING high_risk_txns >= 3
