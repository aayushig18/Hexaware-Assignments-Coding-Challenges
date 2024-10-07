class Appointment:
    def __init__(self, appointmentId, patientId, doctorId, appointmentDate, description):
        self.appointmentId = appointmentId
        self.patientId = patientId
        self.doctorId = doctorId
        self.appointmentDate = appointmentDate
        self.description = description

    def get_patientId(self):
        return self.patientId

    def get_doctorId(self):
        return self.doctorId

    def get_appointmentDate(self):
        return self.appointmentDate

    def get_description(self):
        return self.description

    def __str__(self):
        return (f"Appointment ID: {self.appointmentId}, "
                f"Patient ID: {self.patientId}, "
                f"Doctor ID: {self.doctorId}, "
                f"Date: {self.appointmentDate}, "
                f"Description: {self.description}")
