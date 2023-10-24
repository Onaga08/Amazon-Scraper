import os
import pandas as pd

csv_directory = "output files"
all_dataframes = []
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(csv_directory, filename)
        df = pd.read_csv(filepath)
        all_dataframes.append(df)

combined_dataframe = pd.concat(all_dataframes, ignore_index=True)
output_filepath = os.path.join(csv_directory, "combined_data.csv")
combined_dataframe.to_csv(output_filepath, index=False, encoding='utf-8')
print(f"Combined data written to: {output_filepath}")

