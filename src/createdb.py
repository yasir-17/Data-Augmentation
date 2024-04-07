import sqlite3
from collections import Counter
from datetime import datetime
from src.location_weather import get_weather_code
from src.location_weather import get_side_of_town



# Create a sqlite database and a table
def createdb(db_name, table_name, data):
    # create connection to the database and create a cursor
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    # Drop the existing table if it already exists
    cur.execute("DROP TABLE IF EXISTS {};".format(table_name))

    # Create the table with the new columns
    create_table_query = """
        CREATE TABLE {} (
            incident_time TEXT,
            incident_number TEXT,
            incident_location TEXT,
            nature TEXT,
            incident_ori TEXT,
            day_of_week INTEGER,
            time_of_day INTEGER,
            weather INTEGER,
            location_rank INTEGER,
            side_of_town TEXT,
            incident_rank INTEGER,
            nature_string TEXT,
            emsstat INTEGER
        );
    """.format(table_name)
    cur.execute(create_table_query)
    
    # Initialize the geocoder

    
    # Count the frequency of locations and assign ranks based on the frequency
    location_counts = Counter(row[2] for row in data)
    location_ranks = {loc: rank for rank, locs in enumerate(sorted(location_counts.items(), key=lambda x: x[1], reverse=True), start=1) for loc in locs}

    # Count the frequency of incident and assign ranks based on the frequency
    incidet_count = Counter(row[3] for row in data)
    incident_ranks = {incident: rank for rank, incidents in enumerate(sorted(incidet_count.items(), key=lambda x: x[1], reverse=True), start=1) for incident in incidents}

    # Insert data into the table
    for i, row in enumerate(data, start=1):
        
        if len(row) > 5:
            row[4] = row[5]
            row.pop()
        
        # Initialize EMSSTAT to False
        emsstat = 0
        
        # Check if Incident ORI was EMSSTAT
        if row[4] == "EMSSTAT":
            emsstat = 1

        # Check the subsequent two records for EMSSTAT at the same time and location
        for j in range(1, 3):
            if i + j < len(data):
                next_row = data[i + j]
                if (row[0] == next_row[0] and row[2] == next_row[2] and next_row[4] == "EMSSTAT"):
                    emsstat = 1
                    break
        
        # Extract day of the week from incident_time

        incident_time = datetime.strptime(row[0], "%m/%d/%Y %H:%M")
        time_of_day = incident_time.hour 
        day_of_week = (incident_time.isoweekday() % 7) + 1
        
        
        # Extract rank for the location
        location_rank = location_ranks[row[2]]
        
        # Extract rank for the incident
        incident_rank = incident_ranks[row[3]]
        
        # Extract Nature
        nature = row[3]
        
        loc = row[2]
        date_time = row[0]
        
        wmo  = get_weather_code(loc, date_time)
        side_of_town = get_side_of_town(loc)

        # Add placeholders for the new columns
        row.extend([day_of_week, time_of_day, wmo, location_rank, incident_rank, nature, side_of_town, emsstat])

        insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?' for _ in row])})"
        cur.execute(insert_query, row)
        #time.sleep(30)
        if (i == 10) :
            break

    print("Database created successfully")

    # Commit changes
    con.commit()
    con.close()