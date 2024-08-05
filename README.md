### Data Correction Script

**Instructions to run:**

Assuming you have Git and Python installed, these instructions should work on *Windows Command Prompt*.

1. **Clone the Repository:**
   - Navigate to the directory where you want to keep the project.
   - Clone this repository to your local machine using the command:
     ```
     git clone https://github.com/rumashie/Data-Correction-Script
     ```
   Confirm that a new folder named `Data-Correction-Script` has been created in your chosen directory.

2. **Add the Workbook:**
   - Inside the `Data-Correction-Script` folder, add the workbook containing the data you want to correct. The code expects just one workbook.

3. **Set Up a Python Virtual Environment (venv):**
   - **Create the virtual environment with the following command:**
     ```
     python -m venv venv
     ```
   - **Activate the virtual environment:**
     ```
     venv\Scripts\activate
     ```
   - **Install the dependencies:**
     Ensure you have a `requirements.txt` file in the project directory and run:
     ```
     pip install -r requirements.txt
     ```

4. **Run the Code:**
   - With the virtual environment activated, run the script using:
     ```
     python pythonScript.py
     ```
   - **Deactivate the virtual environment** with the command:
     ```
     deactivate
     ```

#### To Run the Script Again with a New Workbook:
1. **Delete and Replace Workbook:**
   - Delete the existing workbook from the project folder.
   - Add the new workbook file to the same location.

2. **Execute the Script:**
   - Activate the virtual environment again with:
     ```
     venv\Scripts\activate
     ```
   - Run the script using:
     ```
     python pythonScript.py
     ```
