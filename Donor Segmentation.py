import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Step 1: Load the data from the Excel file
file_path = r"C:\Users\mfran\PycharmProjects\Virtuous\Large_VirtuousCRM_Sample.xlsx"

# Load the Excel file
xls = pd.ExcelFile(file_path)

# Load relevant sheets
contacts_df = pd.read_excel(xls, 'Contacts')
donations_df = pd.read_excel(xls, 'Donations')

# Step 2: Merge the Contacts and Donations dataframes on 'Contact_ID'
merged_df = pd.merge(donations_df, contacts_df, on='Contact_ID', how='inner')

# Step 3: Feature Engineering
# Create features such as total donations and frequency of donations
donor_summary = merged_df.groupby('Contact_ID').agg({
    'Donation_Amount': 'sum',  # Total donations
    'Donation_Date': 'count',  # Frequency of donations (number of donations)
    'City': 'first',           # City information
    'State': 'first'           # State information
}).reset_index()

# Rename columns for clarity
donor_summary.columns = ['Contact_ID', 'Total Donations', 'Frequency', 'City', 'State']

# Step 4: K-Means Clustering
# Standardize the data (only numerical features)
clustering_data = donor_summary[['Total Donations', 'Frequency']]
scaler = StandardScaler()
clustering_data_scaled = scaler.fit_transform(clustering_data)

# Apply K-Means clustering (choose the number of clusters, e.g., 3)
kmeans = KMeans(n_clusters=3, random_state=42)
donor_summary['Cluster'] = kmeans.fit_predict(clustering_data_scaled)

# Print out the cluster distribution to verify
print(donor_summary['Cluster'].value_counts())

# Step 5: Save the clustered data to a CSV file for Tableau
output_file_path = r"C:\Users\mfran\PycharmProjects\Virtuous\donor_segmentation_results.csv"
donor_summary.to_csv(output_file_path, index=False)

# Optional: Check the first few rows of the output file
print(donor_summary.head())

