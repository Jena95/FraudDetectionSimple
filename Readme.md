# Fraud Analytics with dbt & BigQuery

## Overview
This project simulates a transaction feed and demonstrates a simple **fraud detection pipeline** using **dbt** and **BigQuery**.  

- Raw transaction data is loaded from CSV into BigQuery (`demo_raw.transactions`).
- Staging layer (`stg_transactions`) cleans data and flags high-risk transactions.
- Mart layer (`mart_fraud_daily`) aggregates daily high-risk transactions for reporting.

## Setup

### 1. Load Raw Data
```bash
bq mk --dataset demo_raw --location=US
bq load --autodetect --source_format=CSV demo_raw.transactions gs://pubdata/transactions.csv

```
### 2. Install dbt
```bash
pip install dbt-bigquery
```
### 3. Initializze Project
```bash
dbt init demo1
cd demo1
```
### 4. Configure profiles.yml
```bash
demo1:
  outputs:
    dev:
      type: bigquery
      method: service-account
      project: YOUR_PROJECT_ID
      dataset: demoDBT
      keyfile: /path/to/your/service_account.json
      location: US
      threads: 2
      priority: interactive
  target: dev
```

### 5. Add the SQL files in Model and makes sure the service account has DataReader access in source and dataEditor in target table.

### 6. Run DBT
```bash
dbt debug
dbt run
dbt test
```

demo_raw.transactions (raw CSV)
          │
          ▼
stg_transactions (dbt view)
          │
          ▼
mart_fraud_daily (incremental table)
