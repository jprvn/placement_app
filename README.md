HEAD
# Placement Eligibility Streamlit Application

## Overview
This project is designed to build a data-driven Streamlit application for managing student placements. It includes:
- **Database Creation:** Four related tables (Students, Programming, Soft Skills, Placements) using SQLite.
- **Synthetic Data Generation:** Using Faker to generate realistic student data.
- **Streamlit App:** An interactive dashboard for filtering and analyzing placement eligibility.

## Project Steps

1. **Database Setup:**
   - Created `database_setup.py` to define and create tables in SQLite.
   - Tables: Students, Programming, SoftSkills, Placements.

2. **Synthetic Data Generation:**
   - Next step: Use the Faker library to generate synthetic data for each table.

3. **Streamlit Application:**
   - Will be built to allow user inputs for filtering data.

4. **SQL Queries & Insights:**
   - A set of SQL queries will be developed to extract meaningful insights.

## Setup Instructions

- **Clone the Repository:**
  ```bash
  git clone https://github.com/jprvn/placement_app.git
  
## Synthetic Data Generation

The `data_generator.py` script uses the Faker library to generate synthetic student data. It:
- Generates realistic student details.
- Inserts 100 records into the Students table of the SQLite database.
- Similar scripts (or extended functions) can be used to generate data for the Programming, Soft Skills, and Placements tables.

# placement_app
b45d612 (Initial commit)