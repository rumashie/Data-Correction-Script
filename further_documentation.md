The python scripts are expecting specific data. To ensure the code runs successfully ensure the data source is compatible. 

The `Data_Cleanup.py` is expecting the following columns:
- Id
- Name
- pmdm__ServiceSchedule__c
- pmdm__SessionEnd__c
- pmdm__SessionStart__c
- Program__c
- pmdm__ServiceLink__c

It is okay if the workbook you use has other columns in addition to these, the python script will ignore them. The Id and Name columns correspond to the sessions. 
Recall, these columns are the result of the workbench query. 

Data-Dump Clean-up:

The `Data_Cleanup.py` cleans and prepares the data from the workbench query for the data correction script `pythonScript.py`.
It delete unnecesary columns, re-names the columns we do need, and extracts the Service ID and Service Name from the orginal `pmdm__ServiceLink__c` column. 
Lastly, it creates the new column `Service Schedule Name`.


Workbench Query Column Names before and after Cleanup

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


The script will create a new sheet to the excel workbook named 'Cleaned-Up Data'. This sheet will be used by `pythonScript.py`. 
-----------------------------------------------------------------------------------------------------------------------------------------------------
The cleanup script should prepare the workbook to be used by pythonScript.py. 

The columns `pythonScript.py` is expecting are
-`Service ID`: unique ID identifying each Service
-`Service Name` the name of the Service
-`Service Schedule Name`: (this column is created in the datadump cleanup script)
-`Session Start`: the date the session occurred 

