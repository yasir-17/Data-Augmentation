# cis6930sp24 -- Assignment2

Name: Yasir Khan

# Assignment Description (in your own words)
This assignment take incident information from norman police department and does the data augmentation.

# How to install
pipenv install

## How to run
pipenv run python assignment2.py --urls files.csv
pipenv run python -m pytest

## Functions
#### assignment2.py 
read_urls_from_csv(csv) - This function takes csv file location and extract url from this file

#### createdb.py
createdb(db_name, table_name, data) - This function takes the database name, table name and the data thats need to be populated on the database. This function also does the augmentation process by taking the element of the original table, do some processing and then make the new augmented table.

#### extract_data.py
extract_data(url) - This function takes the url of the pdf file and then extract the data using pymupdf and camelot. It iterates through each page and the extract the table content and creates list of list.

#### print_table.py
print_table(db_name, table_name) - This function takes the database name and the table name and print the table.

#### location_weather.py
get_lat_long(address) - The function takes the location and return the latitude and longitude. This function uses the api from geoapify. 

get_side_of_town(loc, center_latitude=35.220833, center_longitude=-97.443611) - This function takes the location and calculates the side of town by considering the latitude and longitude of the location and calculating the angular direction from the center.

get_weather_code(loc, date_time) - This function takes the location and date and time and return the wmo code. It uses the open-meteo api. 

## Database Development
1. Create database using function createdb()
-> Establish a connection to an SQLite database named "normanpd.db" using the sqlite3 module. Create a cursor to interact with the database. Define the name of the coulmns of the table and then execute sql statement to create table with that column name

2.Insert elements in the database 
-> Before inserting some preprocesing is done to augment the data and construct an SQL INSERT statement to insert the data into the incidents table. Execute the INSERT statement using the cursor and then commit the changes to the database

## Bugs and Assumptions
1. The code assumes that the provided incident summary URL follows a specific format, containing relevant information in a tabular structure
2. The code assumes that the incident summary URL allows for unlimited access to the data. It should not be password locked or have other access limitations.
3. The geoapify api has a limit of 3000 request per day and hence it can cause error once the limit exceeded. 
4. The geoapigy api does not return latitude and longitude for all the location and hence we dont get side of the town and weather for all location.
5. This code take some time for extracting latitude and longitude and the weather info for each entry and hence if the table is fairly big it will take some amount of time to complete running the entire code.