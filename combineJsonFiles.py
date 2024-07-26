import glob
import json

# Initialize an empty list to store combined data
combined_data = []

# Find all *_repos.json files
json_files = glob.glob('*_repos.json')

# Loop through each file and read its content
for file in json_files:
    try:
        with open(file, 'r') as f:
            content = f.read().strip()
            if content:  # Check if file is not empty
                data = json.loads(content)
                combined_data.extend(data)
    except json.JSONDecodeError:
        print(f"Skipping {file}: not a valid JSON file")

# Write the combined data to all_repos.json
with open('all_repos.json', 'w') as f:
    json.dump(combined_data, f, indent=4)