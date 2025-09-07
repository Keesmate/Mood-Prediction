import pandas as pd

# Load your dataset
df = pd.read_csv("dataset_mood_smartphone.csv")

# Combine date and time columns
date_str = df.iloc[:, 2]  # e.g. "15/03/2014"
time_str = df.iloc[:, 3]  # e.g. "23:39:27"

# Parse using the known format
df['datetime'] = pd.to_datetime(date_str + ' ' + time_str, format="%d/%m/%Y %H:%M:%S", errors='coerce')

# Output earliest and latest timestamps
print("Earliest timestamp in dataset:", df['datetime'].min())
print("Latest timestamp in dataset:", df['datetime'].max())
