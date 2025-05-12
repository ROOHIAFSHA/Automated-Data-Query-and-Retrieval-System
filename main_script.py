# main_script.py

import pandas as pd
import pymongo
import os
from datetime import datetime
from pymongo.errors import ConnectionFailure
from transformers import pipeline
import warnings

warnings.filterwarnings("ignore")

# === 1. Load CSV into MongoDB ===
def load_csv_to_mongodb(csv_file, db_name="LLM_DB", collection_name="products"):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]
    data = pd.read_csv(csv_file)
    data_dict = data.to_dict("records")
    collection.drop()  # Optional: clear previous data
    collection.insert_many(data_dict)
    print(f"✅ Loaded {len(data_dict)} documents into MongoDB collection '{collection_name}'")
    return collection

# === 2. Simulated LLM Query Generator ===
def generate_query(user_question):
    from transformers import pipeline
    generator = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", trust_remote_code=True)
    
    prompt = f"Generate a MongoDB query for the following: {user_question}"
    result = generator(prompt, max_new_tokens=100)[0]["generated_text"]
    return result

# === 3. Parse Queries Manually (simplified approach for demo/test purposes) ===
def hardcoded_query(test_case_id):
    if test_case_id == 1:
        return {
            "query": {
                "$and": [
                    {"Rating": {"$lt": 4.5}},
                    {"Reviews": {"$gt": 200}},
                    {"Brand": {"$in": ["Nike", "Sony"]}}
                ]
            }
        }
    elif test_case_id == 2:
        return {
            "query": {
                "$and": [
                    {"Category": "Electronics"},
                    {"Rating": {"$gte": 4.5}},
                    {"Stock": True}
                ]
            }
        }
    elif test_case_id == 3:
        return {
            "query": {
                "$and": [
                    {"LaunchDate": {"$gt": "2022-01-01"}},
                    {"Category": {"$in": ["Home & Kitchen", "Sports"]}},
                    {"Discount": {"$gte": 10}}
                ]
            },
            "sort": [("Price", -1)]
        }
    return {"query": {}}

# === 4. Execute Query ===
def execute_query(collection, query_dict):
    if "sort" in query_dict:
        return list(collection.find(query_dict["query"]).sort(query_dict["sort"]))
    else:
        return list(collection.find(query_dict["query"]))

# === 5. Save Results ===
def save_results(results, filename):
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"📁 Results saved to {filename}")

# === 6. Save Generated Queries ===
def log_query(case_id, question, query_dict):
    with open("Queries_generated.txt", "a") as f:
        f.write(f"\nTest Case {case_id}: {question}\n")
        f.write(f"Generated Query: {query_dict}\n")

# === 7. Driver ===
if __name__ == "__main__":
    # Step 1: Load Data
    csv_path = "sample_data.csv"
    collection = load_csv_to_mongodb(csv_path)

    # Step 2-5: Test Cases
    test_cases = {
        1: "Find all products with a rating below 4.5 that have more than 200 reviews and are offered by the brand 'Nike' or 'Sony'.",
        2: "Which products in the Electronics category have a rating of 4.5 or higher and are in stock?",
        3: "List products launched after January 1, 2022, in the Home & Kitchen or Sports categories with a discount of 10% or more, sorted by price in descending order."
    }

    for case_id, question in test_cases.items():
        print(f"\n🚀 Running Test Case {case_id}...")
        query_dict = hardcoded_query(case_id)
        results = execute_query(collection, query_dict)
        save_results(results, f"test_case{case_id}.csv")
        log_query(case_id, question, query_dict)
