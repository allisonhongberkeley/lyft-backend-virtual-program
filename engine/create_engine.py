from willoughby_engine import WilloughbyEngine
from capulet_engine import CapuletEngine
from sternman_engine import SternmanEngine

class CreateEngine:
    def create_capulet_engine(current_mileage, last_service_mileage):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        return capulet_engine 
    
    def create_willougby_engine(current_mileage, last_service_mileage):
        willougby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return willougby_engine
    
    def create_sternman_engine(warning_light_on):
        sternman_engine = SternmanEngine(warning_light_on)
        return sternman_engine
    