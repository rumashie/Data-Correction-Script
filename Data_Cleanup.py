import os
import re
import pandas as pd
from openpyxl import load_workbook

# Get the current working directory
folder_path = os.getcwd()

# List all Excel files in the folder
files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Check if there is exactly one Excel file
if len(files) != 1:
    raise FileNotFoundError("There should be exactly one Excel file in the folder.")

# Get the path to the single workbook
workbook_name = files[0]
workbook_path = os.path.join(folder_path, workbook_name)
print(f"Program is using workbook: {workbook_name}") 
print("Program Running...")

# Import Workbook: 
book = load_workbook(workbook_path)

# Convert Sheet with Original Data into pandas DataFrame
dump_df = pd.read_excel(workbook_path, sheet_name=0)

# Rename Columns 
# Delete unnecessary columns
# Create schedule name column
dump_df = dump_df[['Id', 'Name', 'pmdm__ServiceSchedule__c', 'pmdm__SessionEnd__c', 'pmdm__SessionStart__c', 'Program__c', 'pmdm__ServiceLink__c']]

dump_df.rename(columns= {'Id': 'Session ID', 'Name':'Session Name', 'pmdm__ServiceSchedule__c':'Service Schedule ID', 'pmdm__SessionEnd__c':'Session End', 'pmdm__SessionStart__c':'Session Start','Program__c':'Program', 'pmdm__ServiceLink__c':'Service Link'}, inplace=True)
dump_df['Service Schedule Name'] = None

dump_df['Service Link'] = dump_df['Service Link'].astype(str)

def extract_service_details(link):
    match = re.search(r'href="/([^"]+)"[^>]*>([^<]+)<', link)
    if match:
        service_id = match.group(1)
        service_name = match.group(2)
        return pd.Series([service_id, service_name])
    return pd.Series([None, None])  # Return None if it's not a string or if no match is found

# Apply the function to the 'Service Link' column
dump_df[['Service ID', 'Service Name']] = dump_df['Service Link'].apply(extract_service_details)

# Reorder columns 
new_order = ['Program', 'Service Name', 'Service ID', 'Service Schedule ID', 'Service Schedule Name', 'Session Start', 'Session End', 'Session ID', 'Session Name']
dump_df = dump_df[new_order]

# Write the DataFrame to a new sheet in the existing workbook
with pd.ExcelWriter(workbook_path, engine='openpyxl', mode='a') as writer:
    dump_df.to_excel(writer, sheet_name='Cleaned-Up Data', index=False)

print("The Workbench Data Dump has been prepared for the Python Data Correction Script. The cleaned up data has been written in the new sheet 'Cleaned-Up Data")
print("You can now run command `python pythonScript.py to run correcting script")
