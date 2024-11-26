# Massachusetts Department of Correction Inmate Count Analysis

This project analyzes the weekly inmate count data from Massachusetts Department of Correction for the years 2017 and 2018. The primary goal is to understand the inmate population trends across different county facilities. 

The dataset was sourced from the official Massachusetts Department of Correction website, and data cleaning and analysis were performed using Python. The project also includes interactive visualizations created using Tableau, allowing users to filter inmate counts by date and facility.

---

## Technology Stack

- **Python**: For data cleaning and preliminary analysis.
- **Pandas**: To manipulate and analyze the dataset.
- **Excel**: Original data provided in report formats.
- **Tableau**: For creating interactive visualizations of the inmate counts.

---

## Installation

To set up this project locally, follow these steps:

### Clone the Repository:
```bash
git clone https://github.com/<Your-Username>/Massachusetts-Department-of-Correction-Inmate-Analysis.git
cd Massachusetts-Department-of-Correction-Inmate-Analysis
```

### Install Required Libraries:
```bash
pip install pandas openpyxl matplotlib
```

---

## Data Preparation

The data preparation involves cleaning the downloaded weekly inmate count reports for 2017 and 2018. The cleaning process ensures consistent formatting and removes missing or invalid entries. 

### Run the Python Script:
Use the provided Python script for data cleaning and analysis:
```bash
PDF_Extracter.py
```

---

## Visualization

Once the data is cleaned, it is imported into Tableau for creating an interactive dashboard. The Tableau visualization allows users to:

- Filter inmate counts by date.
- View inmate population trends across various county facilities.
- Analyze facility-specific data over time.

### View the Tableau Dashboard:
Open the Tableau workbook file (`Inmate_Count_Analysis.twbx`) in Tableau Desktop or Tableau Public to explore the visualizations.

---

## Tools and Libraries

- **Python**: Primary language for data analysis.
- **Pandas**: For handling data cleaning and transformation.
- **PDFPlumber: To extract data from PDF reports.
- **Matplotlib**: For generating visualizations during analysis.
- **Openpyxl**: To work with Excel files.
- **Tableau**: Used for creating the interactive dashboard.

---

## Dashboard Features

The Tableau dashboard includes:

- **Date Filter**: Explore inmate counts for specific dates.
- **Facility Trends**: Analyze inmate populations across different county facilities.
- **Daily Breakdown**: Drill down into daily inmate count details for each facility.

---

## Insights

Key insights derived from the analysis include:

- **Population Trends**: Understanding seasonal or temporal changes in inmate counts.
- **Facility Utilization**: Variations in inmate populations across facilities.
- **Date-Specific Analysis**: Daily changes in inmate counts, offering insights into operational trends.

- 

---
