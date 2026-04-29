""" appointment.py
"""
from abc import ABC, abstractmethod

class AppoitmentInterface(ABC):
    """This is the interface that will link our decorators to our concrete class"""
    @abstractmethod
    def attend_appointment(self):
        """This is the method that we want to decorate"""
        pass
    @abstractmethod
    def get_notes(self):
        """This is used to get our notes"""
        pass

class AppoitmentDecorator(AppoitmentInterface):
    """Decorator"""
    def __init__(self, decorated_appoitment):
        self.decorated_appoitment = decorated_appoitment

    def attend_appointment(self):
        """This function is whats called unitl we reach our concrete class"""
        self.decorated_appoitment.attend_appointment()

    def get_notes(self):
        """Returns the appoitment notes"""
        return self.decorated_appoitment.get_notes()

class VaccinationDecorator(AppoitmentDecorator):
    """Decorator"""
    def attend_appointment(self):
        self.decorated_appoitment.attend_appointment()
        print("Enter vaccination notes: ")

        note = input()
        self.decorated_appoitment.get_notes().append(f"Vaccination = {note}") # append notes onto notes list

class SurgeryDecorator(AppoitmentDecorator):
    """Decorator"""
    def attend_appointment(self):
        self.decorated_appoitment.attend_appointment()
        print("Enter Surgey notes: ")

        note = input()
        self.decorated_appoitment.get_notes().append(f"Surgery = {note}") # append notes onto notes list

class Appointment(AppoitmentInterface):
    """
    Stores the appointment details. Allows notes to be entered when the appointment is attended.
    """

    def __init__(self, pet, time):
        """
        Appointment constructor
        
        :param pet (Pet): the pet the appointment is for
        :param time (str): A string containing the date/time of the appointment
        """
        self.pet = pet
        pet.add_appointment(self)
        self.time = time

        # notes will be added when the appointment is attended
        self.notes = []

    def attend_appointment(self):
        """
        Asks the user to enter the pet's weight and health notes.        
        :param self
        """

        print("Enter pet weight: ")
        note = input()
        self.notes.append(f"weight= {note}")

        print("Enter health notes: ")
        note = input()        
        self.notes.append(note)

    #---
    # getters

    def get_pet(self):
        """
        Getter for pet
        param: self 
        """
        return self.pet

    def get_notes(self):
        """
        Getter for notes
        param: self
        """
        return self.notes

# EOF
#----
