# Crypto Analytics ETL Pipeline & REST API

This repository implements an automated ETL (Extract, Transform, Load) pipeline in Python integrated with a lightweight REST API built using **FastAPI**.

## 📌 Features
- **Extract**: Fetches real-time market data from the external CoinGecko REST API using `requests`.
- **Transform**: Cleans, filters, and computes financial metrics (e.g., volume-to-market-cap ratios) using **Pandas**.
- **Load / Expose**: Serves transformed data through a clean REST API endpoint with auto-generated OpenAPI / Swagger documentation.

## 🛠️ How to Run Locally

1. **Clone repository**:
   ```bash
   git clone [https://github.com/AskhanLqve/python-etl-rest-api.git](https://github.com/AskhanLqve/python-etl-rest-api.git)
   cd python-etl-rest-api