""" appointment.py
"""
from abc import ABC, abstractmethod

class AppoitmentDecorator:
    """Decorator"""
    def __init__(self, decorated_appoitment):
        self.decorated_appoitment = decorated_appoitment
    def get_notes(self):
        """Returns the appoitment notes"""
        return self.decorated_appoitment.get_notes(self)

class Appointment:
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
