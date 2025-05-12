# Automated-Data-Query-and-Retrieval-System
Using Offline LLM, MongoDB, LangChain, LlamaIndex &amp; CSV

Overview:

This project demonstrates an automated system to query and retrieve data from a CSV file loaded into MongoDB, using open-source/offline Large Language Models (LLMs). It dynamically generates MongoDB queries based on natural language inputs.

 Project Structure
 
├── main_script.py                # Main Python script to run the entire workflow

├── sample_data.csv              # Input CSV file (product data)

├── test_case1.csv               # Output for test case 1

├── test_case2.csv               # Output for test case 2

├── test_case3.csv               # Output for test case 3

├── Queries_generated.txt        # LLM-generated MongoDB queries for each test case

└── README.md                    # Documentation

Installation & Setup:

1. Clone the Repository
git clone <your-repo-url>
cd <your-repo-folder>
2. Create and Activate a Virtual Environment (Optional but Recommended)
pip install -r requirements.txt
Or manually install:
pip install pymongo pandas langchain llama-index

Usage Instructions:

1. Run the Script
python main_script.py

2. You Will Be Prompted To:
Enter a natural language query (e.g., "Show products with rating < 4.5 and reviews > 200 by Nike or Sony.")
Choose to display results in the console or export to CSV.

Test Cases Implemented:

✅ Test Case 1

Query: Products with a rating < 4.5, > 200 reviews, by Nike or Sony

Output: test_case1.csv

✅ Test Case 2

Query: Electronics category, rating ≥ 4.5, in stock

Output: test_case2.csv

✅ Test Case 3

Query: Launched after Jan 1, 2022, Home & Kitchen or Sports, discount ≥ 10%, sorted by price

Output: test_case3.csv

Notes:

If MongoDB is not running or the CSV format is invalid, the script will raise a user-friendly error.

You can update sample_data.csv with your own data.

Queries are generated using a simple offline logic mimicking LLM behavior (custom rules / LangChain-style prompt chains can be integrated).




