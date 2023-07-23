# Importing necessary modules
from Fb_Automation import FacebookMarketAutomation  # Importing the FacebookMarketAutomation class from Fb_Automation module
import csv  # Importing the CSV module to read data from CSV files
from time import sleep  # Importing the sleep function from the time module
from FastX import upload_files  # Importing the upload_files function from the FastX module

# Function to process a single CSV file
def process_csv_file(file_path):
    with open(file_path) as f:
        csv_reader = csv.DictReader(f)  # Creating a CSV reader object with DictReader to read rows as dictionaries
        for row in csv_reader:  # Iterating through each row in the CSV file
            sleep(2)  # Introducing a delay to avoid overwhelming the server
            FacebookMarketAutomation().run(row)  # Creating an instance of FacebookMarketAutomation and running the automation for the current row
            sleep(2)  # Adding another delay to give time for the automation to complete

# Function to process multiple CSV files
def process_csv_files(file_paths):
    for file_path in file_paths:  # Iterating through each file path in the list of file paths
        print(f"Processing CSV file: {file_path}")
        process_csv_file(file_path)  # Calling the process_csv_file function for each file

if __name__ == "__main__":
    data_files = upload_files()  # Calling the upload_files function to get a list of CSV files
    if data_files:  # Checking if the list of CSV files is not empty
        process_csv_files(data_files)  # Calling the process_csv_files function to process the CSV files
