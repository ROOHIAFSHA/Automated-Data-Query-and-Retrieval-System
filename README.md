# Automated Data Query and Retrieval System

## Overview

This project implements an automated data query and retrieval system using Offline LLM, MongoDB, and CSV data processing. It leverages the Mistral-7B-Instruct model for natural language query generation and executes predefined test cases to generate query results, which are saved as CSV files.

## Prerequisites

* Python 3.10 or higher
* MongoDB installed and running locally
* Required Python Libraries:

  * pandas
  * pymongo
  * transformers
  * warnings

## Setup and Installation

1. **Clone the Repository:**

   ```bash
   git clone [repository-url]
   cd [repository-directory]
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Start MongoDB:**
   Ensure that MongoDB is running locally on the default port `27017`.

   ```bash
   mongod
   ```

4. **Data Preparation:**

   * Place the `sample_data.csv` file in the project directory.

## Execution

1. **Run the Script:**

   ```bash
   python main_script.py
   ```

2. **Generated Output:**

   * `test_case1.csv`: Results for products with a rating below 4.5 and more than 200 reviews, from 'Nike' or 'Sony'.
   * `test_case2.csv`: Results for products in the 'Electronics' category with a rating of 4.5 or higher and in stock.
   * `test_case3.csv`: Results for products launched after January 1, 2022, in 'Home & Kitchen' or 'Sports' categories, with a discount of 10% or more, sorted by price.

3. **Query Logs:**

   * The generated queries are logged in the `Queries_generated.txt` file.

## Troubleshooting

* Ensure MongoDB is running before executing the script.
* Verify that the model `mistralai/Mistral-7B-Instruct-v0.1` is accessible and properly loaded.

## Future Improvements

* Implement dynamic query generation using user inputs.
* Integrate more comprehensive data processing and filtering.
* Enhance logging and error handling for better traceability.





