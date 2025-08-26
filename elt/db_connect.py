import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

#connect to postgres database
conn = psycopg2.connect(
    host=os.getenv('HOST', 'postgres'),
    port=os.getenv('PORT', 5432),
    database=os.getenv('DATABASE', 'disaster_insurance'),
    user=os.getenv('USER', 'admin'),
    password=os.getenv('PASSWORD', 'admin')
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