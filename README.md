# Facebook Marketplace Automation with Tkinter UI
Facebook Marketplace Automation is a Python script that utilizes Selenium and PyAutoGUI to automate the process of creating product listings on Facebook Marketplace. The script reads input data from a CSV file, logs in to Facebook, and creates listings for items, vehicles, or homes based on the data provided. Additionally, the script features a user-friendly Tkinter GUI, allowing users to interactively input data and manage the automation process. It uses custom Chrome options for efficient browsing and handles specific details for different listing categories. The automation streamlines the listing process, saving time and effort for users on Facebook Marketplace.

# FastX.py
This Python script utilizes Tkinter, a GUI toolkit, to create an automation tool for posting listings on Facebook Marketplace. The tool allows users to select CSV files containing product information. Upon selection, the script automatically posts the listings, saving time and effort. The application includes a dynamic welcome label with changing text color and displays the FastX logo.

# chromedriver.exe
This is for initializing the driver used in the automation code

# config.ini
This configuration file (config.ini) is used in conjunction with the Facebook Marketplace automation tool. It allows users to provide their Chrome browser profile details and login credentials securely. The chrome_profile section contains profile_name and profile_directory, which specify the Chrome profile to use. The Login_details section stores the username and password for the Facebook account. Users must fill in these values before running the automation tool

# myfile.csv
An example of how to arrange the contents of the csv file in order for the code to run effectively.

# run.py
This Python script automates posting listings on Facebook Marketplace using Selenium. It reads data from CSV files containing product information, processes the data, and posts the listings on Facebook Marketplace. The script utilizes the FacebookMarketAutomation class from the Fb_Automation module to interact with the Facebook website. The csv module is used to read data from CSV files, and the FastX module provides a function for uploading files. The script is designed to handle multiple CSV files, making it efficient for bulk listings.
