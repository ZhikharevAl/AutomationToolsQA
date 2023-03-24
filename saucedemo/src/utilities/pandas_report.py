import pandas as pd
import glob
import json

# List of files containing test results in JSON format
result_files = glob.glob("C:/Users/1/AquaProjects/AutomationToolsQA/allure-results/*.json")

# List of dictionaries with test results.
results = []
for file in result_files:
    with open(file) as f:
        result = json.load(f)
        results.append(result)

# Creating a DataFrame from a list of dictionaries.
df = pd.DataFrame(results)

# Aggregation of test results.
aggregated = df.groupby(['name', 'status']).agg({'name': 'count'}).rename(columns={'name': 'count'}).reset_index()
file_path = r'C:\Users\1\AquaProjects\AutomationToolsQA\test_report\aggregated.xml'
aggregated.to_xml(file_path)
# Displaying the report on the screen.
print(aggregated)
