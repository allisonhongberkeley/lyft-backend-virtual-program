import os, sys
import unittest
from datetime import datetime

sys.path.append('../')

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TireTest(unittest.TestCase):
    def test_carrigan_should_not_be_serviced(self):
        sensor_array = [0.1, 0.1, 0.2, 0.3]
        carrigan = CarriganTire(sensor_array)
        self.assertFalse(carrigan.needs_service())
    
    def test_carrigan_should_be_serviced(self):
        sensor_array = [0.1, 0.95, 0.2, 0.3]
        carrigan = CarriganTire(sensor_array)
        self.assertTrue(carrigan.needs_service())
    
    def test_octoprime_should_not_be_serviced(self):
        sensor_array = [0.8, 0.1, 0.4, 0.3]
        octoprime = OctoprimeTire(sensor_array)
        self.assertFalse(octoprime.needs_service())

    def test_octoprime_should_be_serviced(self):
        sensor_array = [0.8, 0.9, 0.9, 0.7]
        octoprime = OctoprimeTire(sensor_array)
        self.assertTrue(octoprime.needs_service())

if __name__ == '__main__':
    unittest.main()