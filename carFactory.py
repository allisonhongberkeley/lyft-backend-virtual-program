from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from car import Car

class carFactory:
    
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        return Car(capulet_engine, spindler_battery)
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        willougby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        return Car(willougby_engine, spindler_battery)
    
    def create_palindrome(current_date, last_service_date, warning_light_on):
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        return Car(sternman_engine, spindler_battery)
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        return Car(willoughby_engine, nubbin_battery)
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        return Car(capulet_engine, nubbin_battery)