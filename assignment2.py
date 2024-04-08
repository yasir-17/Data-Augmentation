import os
import subprocess
import csv
import sqlite3
from retry_requests import retry
import openmeteo_requests
import requests_cache
from src.print_table import print_table
from src.extract_data import extract_data
from src.createdb import createdb
import time

def read_urls_from_csv(csv_file):
    urls = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            urls.extend(row)
    return urls

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", nargs='+', help="CSV files containing URLs.")
    args = parser.parse_args()

    if args.urls:
        all_data = []  # List to collect all the data
        for csv_file in args.urls:
            urls = read_urls_from_csv(csv_file)
            incident_data = []
            for url in urls:
                data = extract_data(url)
                data = data[1:]
                #print(data)
                incident_data += data
                all_data.append(incident_data)  # Collect the returned data

        db_name = "resources/normanpd.db"
        table_name = "incident_table"

        createdb(db_name, table_name, incident_data)
        
        print_table(db_name, table_name)
        
    else:
        print("Please provide CSV files containing URLs.")
