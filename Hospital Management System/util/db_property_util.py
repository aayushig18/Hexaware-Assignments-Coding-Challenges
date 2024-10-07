
# util/db_property_util.py
class DBPropertyUtil:
    @staticmethod
    def get_property_string():
        # Define your connection details here
        hostname = "LAPTOP-N5SA57O6\MSSQLSERVER01"  # Ensure this is correct
        database = "HospitalManagementSystem"
        
        # Construct the connection string
        connection_string = f"DRIVER={{SQL Server}};" \
                            f"SERVER={hostname};" \
                            f"DATABASE={database};" \
                            
        return connection_string
