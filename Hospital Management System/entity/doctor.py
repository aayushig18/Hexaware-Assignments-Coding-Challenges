# entity/doctor.py
class Doctor:
    def __init__(self, doctorId=None, firstName=None, lastName=None, specialization=None, contactNumber=None):
        self.__doctorId = doctorId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__specialization = specialization
        self.__contactNumber = contactNumber

    # Getters and Setters
    def get_doctorId(self):
        return self.__doctorId

    def set_doctorId(self, doctorId):
        self.__doctorId = doctorId

    def get_firstName(self):
        return self.__firstName

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def get_lastName(self):
        return self.__lastName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def get_specialization(self):
        return self.__specialization

    def set_specialization(self, specialization):
        self.__specialization = specialization

    def get_contactNumber(self):
        return self.__contactNumber

    def set_contactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def __str__(self):
        return f"Doctor(ID: {self.__doctorId}, Name: {self.__firstName} {self.__lastName}, Specialization: {self.__specialization})"
