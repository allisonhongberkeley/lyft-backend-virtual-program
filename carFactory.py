from engine import create_engine
from car import Car
from battery import create_battery
from createCar import createCar

class carFactory:
    
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = create_engine.create_capulet_engine(current_mileage, last_service_mileage)
        spindler_battery = create_battery.create_spindler_battery(current_date, last_service_date)
        return createCar(capulet_engine, spindler_battery)
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        willougby_engine = create_engine.create_willoughby_engine(current_mileage, last_service_mileage)
        spindler_battery = create_battery.create_spindler_battery(current_date, last_service_date)
        return Car(willougby_engine, spindler_battery)
    
    def create_palindrome(current_date, last_service_date, warning_light_on):
        sternman_engine = create_engine.create_sternman_engine(warning_light_on)
        spindler_battery = create_battery.create_spindler_battery(current_date, last_service_date)
        return Car(sternman_engine, spindler_battery)
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = create_engine.create_willoughby_engine(current_mileage, last_service_mileage)
        nubbin_battery = create_battery.create_nubbin_battery(current_date, last_service_date)
        return Car(willoughby_engine, nubbin_battery)
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = create_engine.create_capulet_engine(current_mileage, last_service_mileage)
        nubbin_battery = create_battery.create_nubbin_battery(current_date, last_service_date)
        return Car(capulet_engine, nubbin_battery)