#!/usr/bin/env python3
import unittest

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from partsfinder.datamodel import Value
import pint

class PartsfinderTest(unittest.TestCase):
    def setUp(self):
        self.ureg = pint.UnitRegistry()

    def test_value_compare(self):
        v1 = Value(raw="123", id=None, ureg=self.ureg)
        v2 = Value(raw="456", id=None, ureg=self.ureg)
        self.assertLess(v1, v2)

    def test_value_unit_compare(self):
        unit_amps = self.ureg.parse_expression("A")
        v1 = Value(raw="12 A", unit=unit_amps, id=None, ureg=self.ureg)
        v2 = "60A"
        self.assertLess(v1, v2)

    def test_value_unit_mismatch(self):
        unit_volts = self.ureg.parse_expression("V")
        v1 = Value(raw="60 A", id=None, ureg=self.ureg)
        try:
            v1.unit = unit_volts
        except Exception as e:
            if type(e) == ValueError:
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        
if __name__ == '__main__':
    unittest.main()

