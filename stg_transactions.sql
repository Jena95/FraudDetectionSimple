{{ config(materialized='view') }}

SELECT
  CAST(txn_id AS STRING) AS txn_id,
  card,
  amount,
  ts,
  merchant,
  location,
  IF(amount > 5000, 'HIGH', 'NORMAL') AS risk_flag
FROM {{ source('demo_raw', 'transactions') }}
