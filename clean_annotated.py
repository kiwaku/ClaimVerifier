import pandas as pd

# Load the CSV file
file_path = 'exported.csv'
data = pd.read_csv(file_path)

# Delete the 'Comments' column if it exists
if 'comments' in data.columns:
    data.drop('Comments', axis=1, inplace=True)

# Assuming the column for Y/N values is named 'Fact (Y/N)'
# Remove rows where the 'Fact (Y/N)' column doesn't have a 'Y' or 'N' value
data_cleaned = data[data['label'].isin(['Y', 'N'])]

# Save the cleaned data to a new CSV file
cleaned_file_path = 'exported_cleaned.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)