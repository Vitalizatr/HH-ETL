# HH.ru ETL Pipeline
# 📌 Project Overview

This project is a simple ETL pipeline for extracting job vacancies from HH.ru, transforming the data, and saving the result to a CSV file for further analysis.

The goal of the project is to demonstrate:

clean ETL logic

clear separation of responsibilities

basic Data Engineering best practices

# 🏗 Project Structure

├── src/

│   ├── extract.py     # Extracts data from HH.ru API

│   └── load.py        # Saves processed data to CSV

├── data.csv           # Example output file

└── README.md

🔄 ETL Flow
## 1. Extract

Fetches job vacancies from the HH.ru public API

Supports pagination

Returns raw vacancy data in structured format

## 2. Transform

Selects required fields

Normalizes salary and date fields

Removes incomplete or invalid records

## 3. Load

Saves the processed data into a CSV file (data.csv) or In DataBase(SQL)

Ready for analytics, dashboards, or further processing

# 🛠 Technologies Used

Python 3.10+

requests — API communication

pandas — data transformation

csv — data export

sqlAlchimia - sql export

# ▶️ How to Run

Install dependencies:

pip install pandas requests


# Run the ETL pipeline:

python src/extract.py
python src/load.py


After execution, the output file will be available as:

data.csv
