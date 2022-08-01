from abc import abstractmethod


from abc import ABC, abstractmethod
from car import Car

class createCar:
    @abstractmethod
    def create_car(engine, battery):
        return Car(engine, battery)