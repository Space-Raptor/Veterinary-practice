"""Pet.py
Contains the Pet class 
"""
from prescription import Prescription

class Pet:
    """
    pet contians a name, owner, speicies and 3 lists appoitments,vaccinations and perscriptions.
    """
    def __init__(self, name, owner, species):
        self.name = name
        self.owner = owner
        self.species = species

        self.appointments = []
        self.vaccinations = []
        self.prescriptions = []

    def create_prescription(self, medication, dosage):
        """
        param: self
        param: medication: the medication you want to create a perscription for
        param: dosage: the dose of the medication
        """
        prescription = Prescription(self, medication, dosage)
        self.prescriptions.append( prescription )
        return prescription

    def add_vaccination(self, vaccination):
        """
        param: self
        param: vaccination: the vaccine to add to the vaccinations list
        """
        self.vaccinations.append(vaccination)

    def add_appointment(self, appointment):
        """
        param: self
        param: appoitment: the appoitment to add to the appoitments list
        """
        self.appointments.append(appointment)
