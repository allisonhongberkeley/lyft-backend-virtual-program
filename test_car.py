import sys
import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class Engine(unittest.TestCase):
    @unittest
    def capulet_engine_should_be_serviced(self):
        current_mileage = 300001
        last_service_mileage = 0
        current_mileage = 0
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    @unittest
    def willoughby_engine_should_be_serviced(self):
        current_mileage = 59999
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.needs_service())

        willoughby.current_mileage += 2
        self.assertTrue(willoughby.needs_service())
    
    @unittest
    def sternman_engine_should_be_serviced(self):
        warning_light_on = True
        sternman = SternmanEngine(warning_light_on)
        self.assertTrue(sternman.needs_service())

class Battery(unittest.TestCase):
    @unittest
    def spindler_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year-3)
        spindler = SpindlerBattery(today, last_service_date)
        self.assertTrue(spindler.needs_service())
    
    @unittest
    def nubbin_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year-3)
        nubbin = NubbinBattery(today, last_service_date)
        self.assertFalse(nubbin.needs_service()) 

        nubbin.current_date = nubbin.current_date.replace(year=today.year+2)
        self.assertTrue(nubbin.needs_service())

if __name__ == '__main__':
    unittest.main()
