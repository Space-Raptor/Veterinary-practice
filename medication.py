""" medication.py
contains the medication class 
"""
from abc import ABC, abstractmethod

class Subject(ABC):
    """
    Subject interface enforces observer design pattern
    """
    @abstractmethod
    def attach(self, observer):
        """
        param: self
        param observer: The observer you want to subsribe to the sucject
        """
        pass

    @abstractmethod
    def detach(self, observer):
        """
        param: self
        param observer: The observer you want to detach from the subject
        """
        pass

    @abstractmethod
    def notify(self):
        """
        This will update each observer that is subscribed to the subject
        param: self 
        """
        pass



class Medication(Subject):
    """
    Meication class contains a name for the medication and the amount it has in stock
    """
    def __init__(self, name, amount_in_stock):
        """
        Medication __init__
        
        :param self
        :param name (string): the name of the medication
        :param amount_in_stock: how much of this medication is in stock
        """
        self.name = name
        self.amount_in_stock = amount_in_stock
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def restock(self, amount):
        """        
        :param self
        :param amount (int): The amount to increase the stock by
        """
        self.amount_in_stock += amount
        self.notify() # Update observers when stock changes

    def reduce_stock(self, amount):
        """
        param: self
        param: amount: the number to reduce the stock by
        """
        self.amount_in_stock -= amount
        self.notify() # Update observers when stock changes




    def has_enough_stock(self, dosage):        
        """ Checks if there is enough stock for the given dosage.   
        :param self
        :param dosage (int): The dosage to be checked.
        :returns True or False
        """
        return self.amount_in_stock >= dosage
