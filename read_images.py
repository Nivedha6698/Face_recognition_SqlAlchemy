import mysql.connector
from mysql.connector import Error

try:
    connection = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=DESKTOP-CIRT352;"
        "Database=Face_recognition;"
        "Trusted_Connection=yes;"
    )
    )

    cursor = connection.cursor()

    with open('example.jpg', 'rb') as file:
        image = file.read()

    # Define the data to be inserted into the table
    data = (
    1, 'John', 'face_encoding_data', 'http://example.com/john.jpg', '2022-03-23', True, 30, 'Male', 'Engineer', image)

    # SQL query to insert data into the table
    sql_query = "INSERT INTO face_recognition (id, name, face_encoding, image_url, date_of_registration, status, age, gender, occupation, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # Execute the query and commit the changes to the database
    cursor.execute(sql_query, data)
    connection.commit()

    print("Data inserted successfully!")

except Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
