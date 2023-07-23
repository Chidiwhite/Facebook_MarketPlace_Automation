import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, WebDriverException, NoSuchWindowException
from time import sleep
import pyautogui
import csv
import configparser

class FacebookMarketAutomation(webdriver.Chrome):
    def __init__(self):
        self.service = Service('chromedriver.exe')
        super(FacebookMarketAutomation, self).__init__(service=self.service, options=chrome_options)

    def land_first_page(self):
            self.get("https://wwww.facebook.com/marketplace")
            self.implicitly_wait(10)

    def login_func(self):
        #User credentials
        try:
            Email_or_phone_number = self.find_element(By.ID, 'email')
            Email_or_phone_number.send_keys(str(username)) 
            Password = self.find_element(By.ID, 'pass') 
            Password. send_keys(password) 
            Password.send_keys(Keys.ENTER)
        except:
            pass

    def select_option(self, label_xpath, option_text):
        actions = ActionChains(self)
        label = self.find_element(By.XPATH, label_xpath)
        actions.move_to_element(label).click().perform()
        sleep(1)
        opt = self.find_element(By.XPATH, f"//span[contains(text(), '{option_text}')]")
        actions.move_to_element(opt)
        sleep(1)
        actions.click().perform()

    def send_key(self, label_xpath, key_text):
        label = self.find_element(By.XPATH, label_xpath)
        label.send_keys(f'{key_text}')
        sleep(2)

    def image_upload(self, data_):
        self.implicitly_wait(40)
        sleep(2)
        data = data_
        add_photos = self.find_element(By.XPATH, "//span[text() = 'Add Photos']")
        sleep(1)
        add_photos.click()
        pyautogui.sleep(2)
        pyautogui.typewrite('"' + os.getcwd() + data['images'] + '"')
        pyautogui.sleep(2)
        pyautogui.press("enter")
        sleep(2)

    def select_location(self, data_):
        data = data_
        location_search_input = self.find_element(By.XPATH, "//label[@aria-label='Location']")
        input_value = data['address']
        location_search_input.send_keys(f"{input_value}")
        sleep(3)
        try:
            location_list_box = self.find_element(By.XPATH, "//ul[contains(@aria-label, 'suggested searches')]")
            location_list = location_list_box.find_elements(By.TAG_NAME, "li")
            location_list[0].click()
        except:
            location_list = self.find_element(By.XPATH, "//div[@class='x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x78zum5 x1a2a7pz xh8yej3']")
            location_list.click()
        
    def submit_product(self):
        submit = self.find_element(By.XPATH, "//span[text()='Next']")
        submit.click()
        self.implicitly_wait(10)
        try:
            publish = self.find_element(By.XPATH, "//span[text()='Publish']")
            publish.click()
        except:
            print("Can't publish more products, Limit reached")

    def Items_for_sale(self, data_i):
        self.implicitly_wait(10)
        data = data_i
        
        self.refresh()
        #upload the product images
        self.image_upload(data)
        sleep(2)

        #use the project_file method to import the csv file
        

        #find title and price input
        self.send_key("//label[@aria-label='Title']", data["Name"])
        self.send_key("//label[@aria-label='Price']", data["Price"])

        #Locate and pick caterory and condition of goods you are selling
        self.select_option("//label[@aria-label='Category']", data['category'])
        sleep(2)
        self.select_option("//label[@aria-label='Condition']", data['condition'])
        sleep(4)

        # More details for Tools, Video Games, Books_films and music, Baby and children, Electronics and computers
        # Arts and crafts, Sports and outdoor, car parts, musical instruments, Miscellaneous, Garage sale, household
        # have the same features so theres no need to specify their more details feature
        try:
            self.send_key('//label[@aria-label="Brand"]', data.get('Brand'))
            self.send_key("//label[@aria-label='Colour']", data.get('color'))
            self.select_option("//label[@aria-label='Material']", data.get('material'))
        except (NoSuchElementException, KeyError):
            pass

        # Furniture
        if 'Bed_size' in data and 'Bed_type' in data:
            bed_size_xpath = "//label[@aria-label='Bed size']"
            bed_type_xpath = "//label[@aria-label='Bed type']"
            self.select_option(bed_size_xpath, data['Bed_size'])
            self.select_option(bed_type_xpath, data['Bed_type'])

        # Garden
        if 'Outdoor_Table_Type' in data and 'Shape' in data:
            outdoor_table_xpath = "//label[@aria-label='Outdoor table type']"
            shape_xpath = "//label[@aria-label='Shape']"
            self.select_option(outdoor_table_xpath, data['Outdoor_Table_Type'])
            self.select_option(shape_xpath, data['Shape'])

        # Appliances
        if 'Juicer_type' in data:
            juicer_type_xpath = "//label[@aria-label='Juicer type']"
            self.select_option(juicer_type_xpath, data['Juicer_type'])

        # Bags and luggages
        if 'Luggage_material' in data:
            luggage_material_xpath = "//label[@aria-label='Luggage material']"
            self.send_key(luggage_material_xpath, data['Luggage_material'])

        # Women and men clothing and shoe
        if 'Size' in data and 'Coat_style' in data and 'Fit' in data:
            size_xpath = "//label[@aria-label='Size']"
            coat_style_xpath = "//label[@aria-label='Coat style']"
            fit_xpath = "//label[@aria-label='Fit']"
            self.send_key(size_xpath, data['Size'])
            self.select_option(coat_style_xpath, data['Coat_style'])
            self.select_option(fit_xpath, data['Fit'])

        # Jewellery and accessories
        if 'Bracelet_style' in data and 'Gem_stone' in data:
            bracelet_style_xpath = "//label[@aria-label='Bracelet style']"
            gemstone_xpath = "//label[@aria-label='Gemstone']"
            self.send_key(bracelet_style_xpath, data['Bracelet_style'])
            self.select_option(gemstone_xpath, data['Gem_stone'])

        # Health and beauty
        if 'Hair_type' in data and 'Gender' in data:
            hair_type_xpath = "//label[@aria-label='Hair type']"
            gender_xpath = "//label[@aria-label='Gender']"
            self.select_option(hair_type_xpath, data['Hair_type'])
            self.send_key(gender_xpath, data['Gender'])

        # Pet supplies
        if 'Pet_type' in data and 'Pet_size' in data and 'Dimensions' in data:
            pet_type_xpath = "//label[@aria-label='Pet type']"
            pet_size_xpath = "//label[@aria-label='Pet size']"
            dimensions_xpath = "//label[@aria-label='Dimensions']"
            self.send_key(pet_type_xpath, data['Pet_type'])
            self.send_key(pet_size_xpath, data['Pet_size'])
            self.send_key(dimensions_xpath, data['Dimensions'])

        # Toys and games
        if 'Age_range' in data and 'Character' in data:
            age_range_xpath = "//label[@aria-label='Age range']"
            character_xpath = "//label[@aria-label='Character']"
            self.select_option(age_range_xpath, data['Age_range'])
            self.send_key(character_xpath, data['Character'])

        # Mobile phones
        if 'Compatible_mobile_phone' in data and 'Watch_band_material' in data and 'Watch_band_size' in data:
            mobile_phone_xpath = "//label[@aria-label='Compatible mobile phone']"
            watch_band_material_xpath = "//label[@aria-label='Watch band material']"
            watch_band_size_xpath = "//label[@aria-label='Watch band size']"
            self.select_option(mobile_phone_xpath, data['Compatible_mobile_phone'])
            self.send_key(watch_band_material_xpath, data['Watch_band_material'])
            self.send_key(watch_band_size_xpath, data['Watch_band_size'])

        # Bicycle
        if 'Bicycle_type' in data and 'Bicycle_wheel_size' in data:
            bicycle_type_xpath = "//label[@aria-label='Bicycle type']"
            bicycle_wheel_size_xpath = "//label[@aria-label='Bicycle wheel size']"
            self.select_option(bicycle_type_xpath, data['Bicycle_type'])
            self.send_key(bicycle_wheel_size_xpath, data['Bicycle_wheel_size'])

        # Antiques and collectibles
        if 'Decor_style' in data and 'Country_origin' in data and 'Time_period' in data:
            decor_style_xpath = "//label[@aria-label='Decor style']"
            country_origin_xpath = "//label[@aria-label='Country of origin']"
            time_period_xpath = "//label[@aria-label='Time period']"
            self.select_option(decor_style_xpath, data['Decor_style'])
            self.send_key(country_origin_xpath, data['Country_origin'])
            self.send_key(time_period_xpath, data['Time_period'])

        # Compulsory for all products more details
        self.send_key("//label[@aria-label='Description']", data['Description'])
        self.send_key("//label[@aria-label='Product tags']", data["Product_tag"])
        self.send_key("//label[@aria-label='SKU']", data["SKU"])
            
        #click availability input
        for_availability = self.find_element(By.XPATH, "//label[@aria-label='Availability']")
        for_availability.click()
        sleep(2)
        
        #products in stock
        stock_item = self.find_element(By.XPATH, "//span[text()='List as in stock']")
        single_item = self.find_element(By.XPATH, "//span[text()='List as single item']")
        if f"{data['goods_in_stock']}" == 'Yes':
            stock_item.click()
        else:
            single_item.click()

        #Pick location
        self.select_location(data)

        #Boost sales
        boost_sales = self.find_element(By.XPATH, "//span[text()=\"Boost listing after it's published\"]")
        hide_from_friends = self.find_element(By.XPATH, "//span[text()='Hide from friends']")
        if f"{data['sales_booster']}" == "Yes":
            boost_sales.click()
        else:
            pass
        sleep(3)
        if f"{data['Hide_From_Friends']}" == "No":
            hide_from_friends.click()
        else:
            pass
        
        #Submit Product
        self.submit_product()
        sleep(10)
        
            
    def Vehicle_for_sale(self, data_v):
        self.implicitly_wait(10)
        
        #use the project_file method to import the csv file
        data = data_v
        
        #pick vehicle type from options avalaible
        self.select_option("//label[@aria-label='Vehicle type']", data['vehicle_type'])
        sleep(2)
        
        #upload the product images
        self.image_upload(data)
        sleep(2)
        
        #Pick location
        self.select_location(data)
        sleep(2)
        
        #select year
        self.select_option("//label[@aria-label='Year']", data['year'])
        sleep(2)
        
        #input make and model
        self.send_key("//label[@aria-label='Make']", data['make'])
        self.send_key("//label[@aria-label='Model']", data['model'])
        
        #for mileage and fuel type
        try:
            self.send_key("//label[@aria-label='Mileage']", data['mileage'])
        except KeyError:
                print('This is a key Error, please check the correct spelling in the header of your csv file')
        except NoSuchElementException:
            print('This is a no-such-element Error, please check your csv file and put the correct data')
        
        #input price 
        self.send_key("//label[@aria-label='Price']", data['Price'])
        
        #for car/van vehicle type
        if 'body_style' in data and 'vehicle_condition' in data and 'transmission' in data and 'clean_title' in data:
            body_style_xpath = "//label[@aria-label='Body style']"
            vehicle_condition_xpath = "//label[@aria-label='Vehicle condition']"
            transmission_xpath = "//label[@aria-label='Transmission']"
            self.select_option(body_style_xpath, data['body_style'])
            self.select_option(vehicle_condition_xpath, data['vehicle_condition'])
            self.select_option(transmission_xpath, data['transmission'])
            
            if f"{data['clean_title']}" == 'yes':
                click_box = self.find_element(By.XPATH, "//label[@aria-label='This vehicle has a clean title.']")
                click_box.click()
                sleep(1)
            else:
                pass            
        else:
            pass

        try:
            self.select_option("//label[@aria-label='Fuel type']", data['fuel_type'])
        except KeyError:
                print('This is a key Error, please check the correct spelling in the header of your csv file')
        except NoSuchElementException:
            print('This is a no-such-element Error, please check your csv file and put the correct data')

        #input description
        self.send_key("//label[@aria-label='Description']", data['Description'])
        
        self.submit_product()
        sleep(10)
        
        
    def Home_for_sale(self, data_h):
        self.implicitly_wait(10)
        #use the project_file method to import the csv file
        data = data_h
        
        #upload the product images
        self.image_upload(data)
        sleep(2)

        #pick Property rental type
        self.select_option("//label[@aria-label = 'Type of property for rent']", data['rental_type'])
        sleep(2)
            
        #Number of bedrooms
        self.send_key("//label[@aria-label='Number of bedrooms']", data['number_of_bedrooms'])
        sleep(2)
        
        #Number of bathrooms
        self.send_key("//label[@aria-label='Number of bathrooms']", data['number_of_bathrooms'])
        sleep(2)
        
        #Price per month
        self.send_key("//label[@aria-label='Price per month']", data['price_per_month'])
        sleep(2)
        
        #Address of property for rent
        rental_address = self.find_element(By.XPATH, "//label[@aria-label='Address of property for rent']")
        input_value = data['address']
        rental_address.send_keys(f"{input_value}")
        sleep(3)
        try:
            location_list_box = self.find_element(By.XPATH, "//ul[contains(@aria-label, 'suggested searches')]")
            location_list = location_list_box.find_elements(By.TAG_NAME, "li")
            location_list[0].click()
        except:
            location_list = self.find_element(By.XPATH, "//div[@class='x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x78zum5 x1a2a7pz xh8yej3']")
            location_list.click()
        sleep(2)

        #Property for rent description
        self.send_key("//label[@aria-label='Property for rent description']", data['Description'])
        sleep(2)

        #Property square feet
        if 'property_sq_feet' in data:
            self.send_key("//label[@aria-label='Property square feet']", data['property_sq_feet'])

        #Choose date
        if 'date' in data:
            self.send_key("//label[@aria-label='Choose date']", data['date'])

        #Laundry type
        if 'laundry_type' in data:
            self.select_option("//label[@aria-label='Washing machine/dryer']", data['laundry_type'])
        
        #Parking type
        if 'parking_type' in data:
            self.select_option("//label[@aria-label='Parking type']", data['parking_type'])
        
        #Air conditioning
        if 'air_conditioning' in data:
            self.select_option("//label[@aria-label='Air conditioning']", data['air_conditioning'])

        
        #Heating type
        if 'heating_type' in data:
            self.select_option("//label[@aria-label='Heating type']", data['heating_type'])

        #cat-friendly
        cat_box = self.find_element(By.XPATH, "//input[@aria-label='Cat-friendly']")
        if f"{data['cat_friendly']}" == 'yes':
            cat_box.click()
            sleep(1)
        else:
            pass

        #dog friendly
        dog_box = self.find_element(By.XPATH, "//input[@aria-label='Dog-friendly']")
        if f"{data['dog_friendly']}" == 'yes':
            dog_box.click()
            sleep(1)
        else:
            pass

        #Submit Product
        self.submit_product()
        sleep(10)
        
    def run(self, data_details):
        self.land_first_page()
        self.login_func()
        create_new_listing = self.find_element(By.XPATH, '//a[@aria-label="Create new listing"]')
        create_new_listing.click()
        sleep(2)
        data = data_details
        input_value = data['listing_type']
        try:
            if input_value == 'Item':
                item = self.find_element(By.XPATH, "//span[text() ='Item for sale']")
                item.click()
                self.implicitly_wait(15)
                self.Items_for_sale(data)
                print('---------------Ads Done---------------')
                self.implicitly_wait(15)
                sleep(4)

            elif input_value == 'Vehicle':
                vehicle = self.find_element(By.XPATH, "//span[text() = 'Vehicle for sale']")
                vehicle.click()
                self.implicitly_wait(15)
                self.Vehicle_for_sale(data)
                print('---------------Ads Done---------------')
                self.implicitly_wait(15)
                sleep(4)

            elif input_value == 'Home':
                home = self.find_element(By.XPATH, "//span[contains(text(), 'sale or rent')]")
                home.click()
                sleep(1)
                self.implicitly_wait(15)
                self.Home_for_sale(data)
                print('---------------Ads Done---------------')
                self.implicitly_wait(15)
                sleep(4)
        except NoSuchElementException as e:
            print("Error: The window you are trying to interact with does not exist or cannot be found.")
            print("Details:", e)
        except WebDriverException as e:
            print("To resolve this issue, please check your network connectivity, \
                  ensure that the host is reachable, and verify that the URL is spelled correctly.")
            print("If the issue persists, try accessing the URL in a web browser outside of the \
                  WebDriver environment to verify its accessibility.")
        sleep(5)
        self.close()


#add chrome options
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-blink-features=AutomationControlleD") 
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

#adding chrome profile path
config = configparser.ConfigParser()
config.read('config.ini')
chrome_profile_name = config.get('chrome_profile', 'profile_name')
chrome_profile_directory = config.get('chrome_profile', 'profile_directory')
username = config.get('Login_details', 'username')
password = config.get('Login_details', 'password')

if chrome_profile_name and chrome_profile_directory:
    chrome_options.add_argument(f"user-data-dir={chrome_profile_name}") 
    chrome_options.add_argument(f"profile-directory={chrome_profile_directory}")
