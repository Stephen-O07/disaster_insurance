import requests
from dotenv import load_dotenv
import os
import psycopg2
load_dotenv()

URL = os.getenv('API_URL')

#connect to postgres database
conn = psycopg2.connect(
    host='postgres',
    port = 5432,
    database = 'disaster_insurance',
    user = 'admin',
    password = 'admin'
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS disaster (
        disasterNumber INT,
        pwNumber INT,
        incidentType TEXT,
        projectSize TEXT,
        damageCategoryDescrip TEXT,
        PRIMARY KEY (disasterNumber, pwNumber)
)
""")

conn.commit()


insert_query = """
    INSERT INTO disaster (disasterNumber, incidentType, projectSize, damageCategoryDescrip, pwNumber)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (disasterNumber, pwNumber) DO NOTHING;
"""


# connect to API and extract data
def extract_data():
    response = requests.get(URL)
    response.raise_for_status() # catch API errors
    return response.json()['PublicAssistanceFundedProjectsDetails']


insurance_data = []
def main():
    data = extract_data()

    insurance_data.extend(data)

    # Send data into posegres
    postgres_data = [(data['disasterNumber'], data['incidentType'], data['projectSize'], data['damageCategoryDescrip'], data['pwNumber'])
                     for data in insurance_data]
    
    cur.executemany(insert_query, postgres_data)
    conn.commit()
    cur.close()
    conn.close()

    print("Data loaded successfully")
    return None


   #print(insurance_data[0])
   #print(data[0])



if __name__ == '__main__':
    main()