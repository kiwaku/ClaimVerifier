import pandas as pd

# Path to your CSV file
csv_file_path = 'annotation_data_english_only.csv'
# Path to the output JSON file
json_file_path = 'Annotation/doccano_import.json'

# Load the CSV file
df = pd.read_csv(csv_file_path)

# Optionally, if your CSV contains multiple columns and you want to include only the text for annotation,
# you can select the specific column. For example, if your text is in the 'Sentence' column:
# df = df[['Sentence']]

# Convert the DataFrame to a JSON file, with each line as a JSON object
df.to_json(json_file_path, orient='records', lines=True)

print(f"File converted and saved as {json_file_path}")
