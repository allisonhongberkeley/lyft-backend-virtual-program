import os, sys
import unittest
from datetime import datetime

p = os.path.abspath('..')
sys.path.insert(1, p)

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class BatteryTest(unittest.TestCase):
    def test_spindler_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year-3)
        spindler = SpindlerBattery(today, last_service_date)
        self.assertTrue(spindler.needs_service())
    
    def test_nubbin_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year-3)
        nubbin = NubbinBattery(today, last_service_date)
        self.assertFalse(nubbin.needs_service()) 

        nubbin.current_date = nubbin.current_date.replace(year=today.year+2)
        self.assertTrue(nubbin.needs_service())

if __name__ == '__main__':
    unittest.main()
