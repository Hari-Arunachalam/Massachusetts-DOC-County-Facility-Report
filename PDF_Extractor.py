import pdfplumber
import pandas as pd
import os
import re
from datetime import datetime

# Folder containing the PDF files
folder_path = "/Users/hariarunachalam/Documents/Folders/Job Hunt/Interview project/DOC_datasets/Website_pdf/2018"

# List to hold individual DataFrames
dataframes = []

# Flag to indicate if headers have been assigned
headers_assigned = False
column_names = []

# Iterate over files in the specified folder
for filename in os.listdir(folder_path):
    # Process all files that end with .pdf
    if filename.lower().endswith('.pdf'):
        # Attempt to extract date from filename
        date = None
        date_str = None

        # Try to find a date in the filename using regex (looking for 8 consecutive digits)
        date_match = re.search(r'(\d{8})', filename)
        if date_match:
            date_str = date_match.group(1)
            # Try parsing the date in MMDDYYYY format
            try:
                date = datetime.strptime(date_str, '%m%d%Y').date()
            except ValueError:
                # Try parsing in YYYYMMDD format
                try:
                    date = datetime.strptime(date_str, '%Y%m%d').date()
                except ValueError:
                    # Could not parse date
                    print(f"Could not parse date from filename {filename}")
                    date = None
        else:
            print(f"No date found in filename {filename}")

        # Full path to the PDF file
        pdf_path = os.path.join(folder_path, filename)

        # Initialize a variable to hold the last table
        last_table = None

        # Open the PDF file
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    # Extract tables from the current page
                    tables = page.extract_tables()
                    if tables:
                        # Update the last table found
                        last_table = tables[-1]
        except Exception as e:
            print(f"Error reading PDF file {filename}: {e}")
            continue  # Skip this file if it cannot be read

        # Convert the last table to a DataFrame if it exists
        if last_table:
            # If headers are not assigned yet, process the header
            if not headers_assigned:
                # Assume the first row is the header
                df = pd.DataFrame(last_table[1:], columns=last_table[0])
                # Save column names for reuse
                column_names = last_table[0]
                headers_assigned = True
            else:
                # For subsequent tables, skip the header row
                df = pd.DataFrame(last_table[1:], columns=column_names)
            # Add date column to DataFrame
            df['Date'] = date
            # Append DataFrame to list
            dataframes.append(df)
            print(f"Extracted data from {filename}")
        else:
            print(f"No tables found in the PDF: {filename}")
    else:
        print(f"File does not end with .pdf and will be skipped: {filename}")

# After processing all files, combine the DataFrames
if dataframes:
    # Concatenate all DataFrames into one
    final_df = pd.concat(dataframes, ignore_index=True)

    # Save the final DataFrame to a CSV file
    final_csv_path = os.path.join(folder_path, "Combined_Data.csv")
    final_df.to_csv(final_csv_path, index=False)

    print(f"All data successfully combined and saved to {final_csv_path}")
else:
    print("No data extracted from any PDF files.")
