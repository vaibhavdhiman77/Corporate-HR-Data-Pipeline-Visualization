# Corporate-HR-Data-Pipeline-Visualization

## 📌 Project Overview
In many organizations, Human Resources departments struggle with manual data management, leading to inefficiencies and a lack of clear workforce visibility. This project is an end-to-end Data Analytics solution designed to streamline HR workflows. It transitions raw employee data into a secure database, provides a functional application for data management, and concludes with an interactive business intelligence dashboard for strategic decision-making.

## 🎯 Business Problem & Solution
* **The Challenge:** HR teams spend excessive hours manually tracking employee records, making it difficult to analyze salary distributions, departmental headcount, and workforce demographics.
* **The Solution:** Developed a robust Python-to-SQL data pipeline to securely manage 500+ employee records. Built a Command Line Interface (CLI) application for seamless CRUD operations, and engineered an automated data extraction process that feeds into a Power BI dashboard to visualize key HR metrics. 

## 🛠️ Tech Stack & Tools
* **Programming Language:** Python
* **Database Management:** SQLite
* **Data Manipulation:** Python `csv` module
* **Data Visualization & BI:** Microsoft Power BI
* **Version Control:** Git & GitHub

## ⚙️ Project Workflow & Features
1. **Data Ingestion:** Automated the extraction of raw text data (`.txt`) and successfully loaded 500 records into a structured SQLite database (`EMS_Database.db`).
2. **Backend Application (CRUD):** Engineered a Python-based CLI application (`main.py`) allowing users to:
   * **Create:** Add new employee records safely with Primary Key constraints.
   * **Read:** View the top 10 records or search for specific employees via ID.
   * **Update:** Modify existing employee salaries and departmental assignments.
   * **Delete:** Remove outdated employee records.
3. **Data Extraction:** Developed a script (`export_data.py`) to query the updated SQLite database and generate a clean, formatted CSV file for downstream analysis.
4. **Interactive Dashboard:** Imported the clean dataset into Power BI to create actionable visualizations.

## 📊 Dashboard Insights
The Power BI dashboard provides immediate answers to critical HR questions:
* **Total Salary Cost by Department (Donut Chart):** Highlights budget allocation across various departments.
* **Headcount by Department (Clustered Bar Chart):** Visualizes the distribution of the workforce.
* **Average Employee Age (Card Visual):** Displays the demographic average of the company to assist in targeted HR policy planning.

## 📸 Project Screenshots
*(Note: Replace the placeholder links below with your actual screenshot URLs once uploaded to GitHub)*

![Power BI Dashboard](dashboard_1.png)
![Python CLI Interface](Link_to_your_terminal_screenshot.png)

## 🚀 How to Run the Project
1. Clone this repository: `git clone https://github.com/YourUsername/HR-Data-Analytics-End-to-End.git`
2. Ensure Python is installed on your system.
3. Run `setup_db.py` to initialize the database and load the raw data.
4. Run `main.py` to interact with the Employee Management System.
5. Run `export_data.py` to generate the updated CSV file.
6. Open the `.pbix` file in Power BI Desktop to view the dashboard.
