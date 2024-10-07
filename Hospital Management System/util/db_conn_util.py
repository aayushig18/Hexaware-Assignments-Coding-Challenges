import pyodbc

from util.db_property_util import DBPropertyUtil  # Make sure you have pyodbc installed

class DBConnUtil:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnUtil.connection is None:
            connection_string = DBPropertyUtil.get_property_string()
            DBConnUtil.connection = pyodbc.connect(connection_string)
        return DBConnUtil.connection
    

    def get_next_appointment_id():
        connection = DBConnUtil.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT MAX(appointmentId) FROM Appointments")
            max_id = cursor.fetchone()[0]
            return (max_id + 1) if max_id is not None else 1
        except Exception as e:
            print(f"An error occurred while fetching the next appointment ID: {e}")
            return 1  # Default to 1 if an error occurs
        finally:
            cursor.close()
