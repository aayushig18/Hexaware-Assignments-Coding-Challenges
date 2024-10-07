# main/main_module.py
import os
from dao.hospital_service_impl import HospitalServiceImpl
from entity.appointment import Appointment
from exception.patient_number_not_found_exception import PatientNumberNotFoundException
from util.db_conn_util import DBConnUtil
from tabulate import tabulate
from datetime import datetime

class MainModule:
    def __init__(self):
        self.service = HospitalServiceImpl()

    def menu(self):
        while True:
            menu = [
                ["1.", "Get Appointment Details by ID"],
                ["2.", "Schedule Appointment"],
                ["3.", "Update Appointment"],
                ["4.", "Cancel Appointment"],
                ["5.", "Get Appointments for Patient"],
                ["6.", "Get Appointments for Doctor"],
                ["7.", "Exit"]
            ]

        # Print the menu using tabulate
            print(tabulate(menu, headers=["Option", "Description"], tablefmt="grid"))

            choice = input("\nEnter your choice: ")
            if choice == '1':
                appointment_id = input("\nEnter appointment ID: ")
                try:
        # Convert appointment_id to an integer
                    appointment_id = int(appointment_id)
                    appointment = self.service.getAppointmentById(appointment_id)
                    if appointment is None:  # Appointment not found is handled in the method
                        print("")  # Empty print to maintain the format if needed
                except ValueError:
                    print("Invalid input. Please enter a numeric appointment ID.")
                except PatientNumberNotFoundException as e:
                    print(e)

            elif choice == '2':
                patient_id = input("Enter patient ID: ")
                doctor_id = input("Enter doctor ID: ")
                appointment_date = input("Enter appointment date (YYYY-MM-DD HH:MM): ")
                description = input("Enter appointment description: ")

    # Get the next available appointment ID
                appointment_id = DBConnUtil.get_next_appointment_id()

                if appointment_id is None:
                    print("Failed to fetch next appointment ID. Please try again.")
                else:
        # Create Appointment object
                    appointment = Appointment(
                        appointmentId=appointment_id,  # Use the generated ID
                        patientId=int(patient_id),  # Assuming patient ID is numeric
                        doctorId=doctor_id,
                        appointmentDate=appointment_date,
                        description=description
                    )

        # Schedule the appointment using the service
                if self.service.scheduleAppointment(appointment):
                    print("Appointment scheduled successfully.")
                else:
                    print("Failed to schedule appointment. Try Again\n")








            elif choice == '3':
                appointment_id = input("\nEnter appointment ID to update: ")
                try:
                    appointment_id = int(appointment_id)
                except ValueError:
                    print("Invalid input. Please enter a numeric appointment ID.")
                    continue  # Go back to the menu

                new_patient_id = input("Enter new patient ID: ")
                if not self.service.patient_exists(new_patient_id):
                    print("The specified patient ID does not exist. Please check and try again.")
                    continue
                
                new_doctor_id = input("Enter new doctor ID: ")
                new_appointment_date_str = input("Enter new appointment date (YYYY-MM-DD HH:MM): ")

    # Validate the new appointment date
                try:
                    new_appointment_date = datetime.strptime(new_appointment_date_str, '%Y-%m-%d %H:%M')
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
                    continue  # Go back to the menu

                new_description = input("Enter new appointment description: ")

    # Create an Appointment object
                appointment = Appointment(
                    appointmentId=appointment_id,
                    patientId=new_patient_id,
                    doctorId=new_doctor_id,
                    appointmentDate=new_appointment_date,
                    description=new_description
                )

                # Call the updateAppointment method
                if self.service.updateAppointment(appointment):
                    print("\n******************************************")
                    print("\tAppointment updated successfully.")
                    print("\n******************************************")
                    
                else:
                    print("Failed to update appointment.")
                    print("\n******************************************")
                    
                    
                    
                    
                    
                    
                    
                    
                    
            elif choice == '4':
                appointment_id = input("Enter appointment ID to cancel: ")
    
                if self.service.cancelAppointment(appointment_id):
                    print("Appointment canceled successfully.")
                else:
                    print("\n******************************************************")
                    print(f"\tAppointment ID {appointment_id} does not exist.\n \tfailed to cancel appointment.\n******************************************************")
            elif choice == '5':
                patient_id = input("Enter patient ID to fetch appointments: ")
                appointments = self.service.getAppointmentsForPatient(patient_id)

                if appointments:
                    print(f"\nAppointments for patient ID: {patient_id}\n")
        # Prepare data for tabular representation
                    table_data = [[appointment.appointmentId, appointment.doctorId, appointment.appointmentDate, appointment.description]
                      for appointment in appointments]
        
        # Define table headers
                    headers = ["Appointment ID", "Doctor ID", "Appointment Date", "Description"]
        
        # Print table using tabulate
                    print(tabulate(table_data, headers=headers, tablefmt="grid"))
                    print("\n")
                else:
                    print(f"\n------No appointments found for patient ID: {patient_id}------")
            elif choice == '6':
                doctor_id = input("Enter doctor ID to fetch appointments: ")

    # Verify if the doctor exists
                if not self.service.doctor_exists(doctor_id):
                    print("The doctor ID does not exist. Please check and try again.")
                    continue  # Go back to the menu

    # Fetch and display appointments for the doctor
                appointments = self.service.getAppointmentsForDoctor(doctor_id)

                if appointments:
                    print(f"\nAppointments for doctor ID: {doctor_id}\n")

        # Prepare data for tabular representation
                    table_data = [[appointment.appointmentId, appointment.patientId, appointment.appointmentDate, appointment.description]
                                  for appointment in appointments]

        # Define table headers
                    headers = ["Appointment ID", "Patient ID", "Appointment Date", "Description"]

        # Print table using tabulate
                    print(tabulate(table_data, headers=headers, tablefmt="grid"))
                    print("\n")
                else:
                    print(f"No appointments found for doctor ID: {doctor_id}")

            elif choice == '7':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main = MainModule()
    main.menu()
