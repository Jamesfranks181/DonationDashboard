# Donor Segmentation and Dashboard Analysis

This project involves segmenting donor data using Python, visualizing insights through a Tableau dashboard, and analyzing donation behavior. The data comes from a CRM system and includes donor details, donation amounts, and campaign information.

## Project Overview

The project is divided into two main parts:
1. **Data Cleaning and Segmentation (Python)**: Python was used to clean the donor data and segment donors based on donation behavior.
2. **Interactive Dashboard (Tableau)**: The cleaned data was visualized in Tableau, providing insights into donor distribution, total donations, and campaign performance.

## Project Files

- **Donor_Segmentation.py**: This Python script performs the following tasks:
    - Cleans and processes donor and donation data from CSV files.
    - Segments donors based on donation frequency and amount.
    - Outputs the cleaned data for use in Tableau.

- **Donations_Data.csv**: This CSV file contains the cleaned donor data with the following fields:
    - `Donor_ID`: Unique identifier for each donor.
    - `Donation_Amount`: The amount donated by the donor.
    - `Campaign_Name`: The name of the campaign associated with the donation.
    - `Date_Created`: Date the donor record was created.
    - `Cluster`: Donor segmentation based on clustering (e.g., high-value, low-value, etc.).

- **Tableau_Dashboard.twbx**: The Tableau workbook containing the following visualizations:
    - **Donor Distribution by State**: A map showing donation totals by geographic location.
    - **Donor Segmentation**: Bar charts visualizing d
