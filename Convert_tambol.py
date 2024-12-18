import timeit
import re
import os

start_time = timeit.default_timer()

def read_sql_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract only the data within the parentheses
    pattern = r"\((\d+), '([^']+)', (\d+), '([^']+)', (\d+), '([^']+)'\)"
    matches = re.findall(pattern, content)
    

    # Convert matches to the desired format
    result = []
    for match in matches:
        row = (
            int(match[0]),  # First number
            match[1]       # First string
        )
        result.append(row)
    return result

# Specify the file to process
file_path = os.path.abspath("D:/work/Sorting-Algorithm/tambol.sql")
print(f"Processing file: {file_path}")

# Read data from the file
data = read_sql_file(file_path)

# Exit if no data was processed
if not data:
    print("No data processed. Exiting.")
    exit()

# Display sample data
print(f"Processed data from {file_path}:")
for row in data[:5]:  # Display the first 5 rows as a sample
    print(" ".join(map(str, row)))
print("\n")

# Write the data to a new file
output_file = 'D:/work/Sorting-Algorithm/Convert/tambol.txt'
os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Create directories if needed
with open(output_file, 'w', encoding='utf-8') as write_province:
    for row in data:
        write_province.write(" ".join(map(str, row)) + "\n")

# Calculate processing time
Timespent = timeit.default_timer() - start_time
print(f"{Timespent} seconds")
