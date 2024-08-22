# Data Requirements for Python Scripts

The Python scripts expect specific data formats. To ensure smooth execution, please make sure your data source matches these requirements.

## `Data_Cleanup.py` Requirements

The `Data_Cleanup.py` script requires the following columns in your data:

- Id
- Name
- pmdm__ServiceSchedule__c
- pmdm__SessionEnd__c
- pmdm__SessionStart__c
- Program__c
- pmdm__ServiceLink__c

It’s fine if your workbook has additional columns; the script will ignore them. The `Id` and `Name` columns should correspond to the sessions. These columns come from the workbench query.

**The `Data_Cleanup.py` script performs the following tasks:**

1. **Cleans the Data:** Removes unnecessary columns.
2. **Renames Columns:** Updates the names of the columns we need.
3. **Extracts Information:** Pulls the Service ID and Service Name from the `pmdm__ServiceLink__c` column.
4. **Creates New Column:** Adds a new column named `Service Schedule Name`.

## Workbench Query Column Names Before and After Cleanup

**Column Changes**

| **Original Columns**                      | **Updated Columns After Cleanup**              |
|-------------------------------------------|------------------------------------------------|
| Id                                        | Program                                        |
| Name                                      | Service Name                                   |
| pmdm__ServiceSchedule__c                  | Service ID                                     |
| pmdm__SessionEnd__c                       | Service Schedule ID                            |
| pmdm__SessionStart__c                     | Service Schedule Name                          |
| Program__c                                | Session Start                                  |
| pmdm__ServiceLink__c                      | Session End                                    |
|                                           | Session ID                                     |
|                                           | Session Name                                   |

After the cleanup, the script will create a new sheet in the Excel workbook called 'Cleaned-Up Data'. This sheet will be used by the `pythonScript.py`.

---

## `pythonScript.py` Requirements

To work correctly, `pythonScript.py` needs the following columns:

- **Service ID:** Unique ID for each Service
- **Service Name:** The name of the Service
- **Service Schedule Name:** Created by the `Data_Cleanup.py` script
- **Session Start:** The date when the session occurred
