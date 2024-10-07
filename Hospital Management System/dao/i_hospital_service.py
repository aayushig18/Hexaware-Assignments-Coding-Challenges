# dao/i_hospital_service.py
from abc import ABC, abstractmethod
from entity.appointment import Appointment

class IHospitalService(ABC):
    @abstractmethod
    def getAppointmentById(self, appointmentId):
        pass

    @abstractmethod
    def getAppointmentsForPatient(self, patientId):
        pass

    @abstractmethod
    def getAppointmentsForDoctor(self, doctorId):
        pass

    @abstractmethod
    def scheduleAppointment(self, appointment: Appointment):
        pass

    @abstractmethod
    def updateAppointment(self, appointment: Appointment):
        pass

    @abstractmethod
    def cancelAppointment(self, appointmentId):
        pass
