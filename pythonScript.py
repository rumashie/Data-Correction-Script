'''
 Title: pythonScript.py
 Author: Massiel Sanchez
 Date: July 2024
 Last Modified: 12 August 2024 by Massiel Sanchez
 
 Purpose: This python script automates data correction by restoring the hierarchical relationship 
 between Service Sessions and Service Schedules in the Salesforce PMM environment, ensuring sessions in the same month 
 and year share the same Service Schedule ID.
 
 Notes:
 
* Excel Workbook should be in the same folder of this python file. For more instructions on set-up, visit the project's Github README file. 
 
This python script was made specifically for Services and Service Schedule Data. It interacts directly with the following Columns: 
 - Service: Record ID
 - First Session Start
 - Service Schedule: Service Schedule Name
 - Service: Service Name
 '''

# Import Libraries
import pandas as pd
from openpyxl import load_workbook
import os


# Get the directory of the current python file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the folder containing the workbook as the same directory as the script
folder_path = script_dir

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

'''
Data Correction Project Begins:
'''

# Import Workbook: 
book = load_workbook(workbook_path)

# Convert Sheet with Original Data into pandas DataFrame
original_dataFrame = pd.read_excel(workbook_path, sheet_name=0)

'''
Group original data based on the Month and Year the service occured using the Date in column 'First Session Start'
using pandas to_period() function

'''

# Convert Dates into type datetime
original_dataFrame['First Session Start'] = pd.to_datetime(original_dataFrame['First Session Start'], format='%m/%d/%Y %I:%M %p')

# Creating new Column named Period to 'extract' the Month and Year from 'First Session Start' of each row
original_dataFrame['period'] = original_dataFrame['First Session Start'].dt.to_period('M')

# Adjust Period for Fiscal Year Calendar 

# This function updates the necessary periods
def update_period(period):
    if period.month > 6:
        # Create and return a new period with different year, since periods are immutable 
        return pd.Period(year = period.year + 1, month = period.month, freq='M')
    # else no need to change period
    return period 

# Apply the update_period function to period column
original_dataFrame['period'] = original_dataFrame['period'].apply(update_period)


'''
Group Original Data based on 'period' column and Service ID
iterating through each group, update the needed columns
'''

grouped_data = original_dataFrame.groupby(['period', 'Service: Record ID'])

# Helper Function 1: used to perform the Data update, finds row in original DataFrame and updates content
def update_data(df, group, schedule_id, schedule_name):
    df.loc[group.index, 'Service Schedule: ID'] = schedule_id
    df.loc[group.index, 'Service Schedule: Service Schedule Name'] = schedule_name

# Helper Function 2: used to format the updated Schedule Name in "FY [YEAR] [MONTH] [Service Name]"
def get_schedule_name(period, service_name):
    dt = period.to_timestamp()
    year_last_two_digits = dt.year % 100
    month_name = dt.strftime('%B')
    # Concatenate
    result = f"FY {year_last_two_digits} {month_name} {service_name}"
    return result

'''
MAIN CODE: 
1. Iterate through grouped data
2. Find service session that happened first based on date
3. Retrieve information from this row
4. Call Helper Functions to update the information for remaining rows in the group
'''    
for name, group in grouped_data: 
    first_row_index = group['First Session Start'].idxmin()
    first_row = group.loc[first_row_index]
    first_row_scheduleID = first_row['Service Schedule: ID']
    group_period = first_row['period']
    new_service_schedule_name = get_schedule_name(group_period, first_row['Service: Service Name'])
    update_data(original_dataFrame, group, first_row_scheduleID,new_service_schedule_name)

# Drop the 'period' column before writing to the new sheet
corrected_dataFrame = original_dataFrame.drop(columns=['period'])

with pd.ExcelWriter(workbook_path, engine='openpyxl', mode='a') as writer:
    corrected_dataFrame.to_excel(writer, sheet_name="Corrected", index=False)    
    
print("All Done. Check Workbook for new sheet with corrected data :)")