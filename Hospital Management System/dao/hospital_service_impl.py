from dao.i_hospital_service import IHospitalService
from entity.appointment import Appointment
from exception.patient_number_not_found_exception import PatientNumberNotFoundException
from util.db_conn_util import DBConnUtil
from tabulate import tabulate
from datetime import datetime

class HospitalServiceImpl(IHospitalService):
    
    def getAppointmentById(self, appointmentId):
        connection = DBConnUtil.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Appointments WHERE appointmentId = ?", (appointmentId,))
            appointment_data = cursor.fetchone()
            if appointment_data:
            # Create a list of appointment details for tabulate
                appointment_details = [
                    ["Appointment ID", appointment_data[0]],
                    ["Patient ID", appointment_data[1]],
                    ["Doctor ID", appointment_data[2]],
                    ["Appointment Date", appointment_data[3]],
                    ["Description", appointment_data[4]],
                ]
                print("\n********* Appointment Details *********")
                print(tabulate(appointment_details, tablefmt="grid"))
                print("***************************************\n")
            else:
                print("\n***** Appointment not found!!!!! *****\n")
                return None
        except Exception as e:
            print(f"An error occurred while fetching appointment: {e}")
            return None
        finally:
            cursor.close()

    def getAppointmentsForPatient(self, patientId):
        connection = DBConnUtil.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Appointments WHERE patientId = ?", (patientId,))
            appointments = []
            for row in cursor.fetchall():
                appointments.append(Appointment(
                    appointmentId=row[0],
                    patientId=row[1],
                    doctorId=row[2],
                    appointmentDate=row[3],
                    description=row[4]
                ))
            return appointments
        except Exception as e:
            print(f"An error occurred while fetching appointments for patient: {e}")
            return []
        finally:
            cursor.close()


    def getAppointmentsForDoctor(self, doctorId):
        connection = DBConnUtil.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Appointments WHERE doctorId = ?", (doctorId,))
            appointments = []
            for row in cursor.fetchall():
                appointments.append(Appointment(
                    appointmentId=row[0],
                    patientId=row[1],
                    doctorId=row[2],
                    appointmentDate=row[3],
                    description=row[4]
                ))
            return appointments
        except Exception as e:
            print(f"An error occurred while fetching appointments for doctor: {e}")
            return []
        finally:
            cursor.close()
    
    def doctor_exists(self, doctor_id):
        connection = DBConnUtil.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM Doctors WHERE doctorId = ?", (doctor_id,))
            count = cursor.fetchone()[0]
            return count > 0  # Return True if doctor exists
        except Exception as e:
            print(f"An error occurred while checking doctor existence: {e}")
            return False
        finally:
            cursor.close()
    
    
    def scheduleAppointment(self, appointment: Appointment):
        connection = DBConnUtil.get_connection()
        cursor = connection.cursor()

        try:
        # Check if the patient ID exists
            cursor.execute("SELECT COUNT(*) FROM Patients WHERE patientId = ?", (appointment.get_patientId(),))
            patient_exists = cursor.fetchone()[0]
            if not patient_exists:
                print("\n*************************************************")
                print(f" Patient ID {appointment.get_patientId()} does not exist.")
                print("\n*************************************************")
                return False

        # Check if the doctor ID exists
            cursor.execute("SELECT COUNT(*) FROM Doctors WHERE doctorId = ?", (appointment.get_doctorId(),))
            doctor_exists = cursor.fetchone()[0]
            if not doctor_exists:
                print("\n*************************************************")
                print(f"Error: Doctor ID {appointment.get_doctorId()} does not exist.")
                print("\n*************************************************")
                return False

        # If both IDs exist, proceed with scheduling the appointment
            cursor.execute(
                "INSERT INTO Appointments (appointmentId, patientId, doctorId, appointmentDate, description) VALUES (?, ?, ?, ?, ?)",
                (appointment.appointmentId, appointment.get_patientId(), appointment.get_doctorId(), appointment.get_appointmentDate(), appointment.get_description())
            )
            connection.commit()
            print("\n*************************************")
            print("Appointment scheduled successfully!")
            print("\n*************************************")
            return True

        except Exception as e:
            print(f"An error occurred while scheduling appointment: {e}")
            return False

        finally:
            cursor.close()



    def cancelAppointment(self, appointmentId):
        connection = DBConnUtil.get_connection()
        cursor = connection.cursor()
    
        try:
        # First, check if the appointment ID exists
            cursor.execute("SELECT COUNT(*) FROM Appointments WHERE appointmentId = ?", (appointmentId,))
            appointment_exists = cursor.fetchone()[0]
        
            if appointment_exists == 0:
                print(f"Appointment ID {appointmentId} does not exist.")
                return False
        
        # If the appointment exists, proceed to delete it
            cursor.execute("DELETE FROM Appointments WHERE appointmentId = ?", (appointmentId,))
            connection.commit()
            return True
    
        except Exception as e:
            print(f"An error occurred while canceling appointment: {e}")
            return False
    
        finally:
            cursor.close()
            
            
            
    def patient_exists(self, patientId):
        connection = DBConnUtil.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM Patients WHERE patientId = ?", (patientId,))
            count = cursor.fetchone()[0]
            return count > 0  # Return True if patient exists
        except Exception as e:
            print(f"An error occurred while checking patient existence: {e}")
            return False
        finally:
            cursor.close()
            
    def updateAppointment(self, appointment: Appointment):
        connection = DBConnUtil.get_connection()
        cursor = connection.cursor()
        try:
        # Check if the appointment ID exists
            cursor.execute("SELECT COUNT(*) FROM Appointments WHERE appointmentId = ?", (appointment.appointmentId,))
            count = cursor.fetchone()[0]
        
            if count == 0:
                print("\n*****************************************")
                print("Appointment ID does not exist.")
                return False
        
        # Proceed with the update if the ID exists
            cursor.execute(
                "UPDATE Appointments SET patientId = ?, doctorId = ?, appointmentDate = ?, description = ? WHERE appointmentId = ?",
                (appointment.get_patientId(), appointment.get_doctorId(), appointment.get_appointmentDate(), appointment.get_description(), appointment.appointmentId)
            )
            connection.commit()
            return True
        except Exception as e:
            print(f"An error occurred while updating appointment: {e}")
            return False
        finally:
            cursor.close()


