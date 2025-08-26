from dotenv import load_dotenv
from elt.db_connect import conn, cur, insert_query
from elt.extract import extract_data

load_dotenv()
 
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