from nubbin_battery import NubbinBattery
from spindler_battery import SpindlerBattery

class CreateBattery:
    def create_spindler_battery(current_date, last_service_date):
        return SpindlerBattery(current_date, last_service_date)
    
    def create_nubbin_battery(current_date, last_service_date):
        return NubbinBattery(current_date, last_service_date)
    
    