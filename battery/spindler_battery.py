from general_battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date  
    
    def needs_servce(self):
        difference = self.current_date - self.last_service_date
        years = 2
        return difference.days > (365 * years)