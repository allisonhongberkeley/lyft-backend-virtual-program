import sys, os
import unittest
from datetime import datetime

p = os.path.abspath('..')
sys.path.insert(1, p)

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

class EngineTest(unittest.TestCase):
    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 59999
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.needs_service())

        willoughby.current_mileage += 2
        self.assertTrue(willoughby.needs_service())
    
    def test_sternman_engine_should_be_serviced(self):
        warning_light_on = True
        sternman = SternmanEngine(warning_light_on)
        self.assertTrue(sternman.needs_service())

if __name__ == '__main__':
    unittest.main()
