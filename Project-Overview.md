#### Introduction:
Due to Data Migration from custom tables to Salesforce's PMM environment, the data lost correct format and hierarchical structure. Specifically, the hierarchical relationship between Services and Service Sessions was corrupted. Service Sessions were mistakenly saved with unique Service Schedules, rather than associating multiple sessions of the same Service with a single Service Schedule window.  A Service Schedule window is defined by Month and Fiscal Year, meaning Sessions of the same Service that took place in the same month and year should have the same Schedule ID. 

#### Representation of the Problem in Data

The Attributes (columns) of the original table:

| **Column Name**                         | **Description**                               |
| :-------------------------------------- | --------------------------------------------- |
| Service: Program                        | Program Name                                  |
| Service: Service Name                   | Service Name                                  |
| Service: Record ID                      | *unique identifier of services*               |
| Service Schedule: Service Schedule Name | Name for service schedules                    |
| Service Schedule: ID                    | *unique identifier of service schedule*       |
| First Session Start                     | Date of First Session of the Service          |
| Location                                | Where the Service  took place                 |
| Service Schedule End Date               | Date of the Final Day of the Service Schedule |
| Language                                | Language Service was given in                 |
| Service Method                          | Method of Service                             |

The original data reveals an incorrect hierarchical relationship where sessions of the same Service are associated with unique Service Schedules. Sessions of the same service that occurred within Month and Year *should* have the same Service Schedule ID.

**Example 1:**
![example1](example1.png)
The service `150 - Telephone English Level 2 - Section B` from the `Russian UWW` Program is identified by Service Record ID `a2iUz000000efK3`. This service was provided twice on January 24, 2024, and January 31, 2024. 
Both sessions should belong to the same Service Schedule since they occurred in the same schedule window of January 2024. However, as shown in the original data, they have unique Service Schedule IDs.
In the corrected data, both sessions now have the same Service Schedule ID, indicating they are part of the same Service Schedule, January 2024.  


#### Solution 
To correct the data:
1. **Identify Rows:** Identify rows that should have the same schedule ID by *grouping* sessions of the same service occurring in the same month and year.
2. **Update Data:** Update the schedule ID and schedule name to ensure these rows have the same schedule ID and schedule name.

#### The Code
Code Implementation: We implemented the solution using Python including the library *Pandas*, a library that helps manipulate and analyze data. 
See python files in this repository.

#### Conclusion
The data correction process successfully restored the hierarchical structure between Services and Service Sessions. The Service Sessions that took place in the same month and year now share the same Service Schedule ID, reflecting the intended hierarchy. 


More Resources:
- [Salesforce PMM Documentation](https://help.salesforce.com/s/articleView?id=sfdo.PMM_Overview.htm&type=5)
- [W3Schools Pandas Overview](https://www.w3schools.com/python/pandas/pandas_intro.asp)
- [Pandas Documentation](https://pandas.pydata.org/docs/)


