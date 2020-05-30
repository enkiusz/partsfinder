#!/usr/bin/env python3
import unittest

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from partsfinder.datamodel import Value, Parameter
import pint

class PartsfinderTest(unittest.TestCase):
    def setUp(self):
        self.ureg = pint.UnitRegistry()
        self.unit_amps = self.ureg.parse_expression("A")
        self.unit_volts = self.ureg.parse_expression("V")

    def test_value_compare(self):
        v1 = Value(raw="123", id=None, ureg=self.ureg)
        v2 = Value(raw="456", id=None, ureg=self.ureg)
        self.assertLess(v1, v2)

    def test_value_unit_compare(self):
        v1 = Value(raw="12 A", unit=self.unit_amps, id=None, ureg=self.ureg)
        v2 = "60A"
        self.assertLess(v1, v2)

    def test_value_unit_mismatch(self):
        v1 = Value(raw="60 A", id=None, ureg=self.ureg)
        try:
            v1.unit = self.unit_volts
        except Exception as e:
            if type(e) == ValueError:
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        
    def test_parameter_value_check_nounit(self):
        p = Parameter(id=None, name='Test Parameter', unit=None)
        self.assertTrue(p.validate_value_text('2000 A'))

    def test_parameter_value_check_unit(self):
        p = Parameter(id=None, name='Test Parameter')
        self.assertTrue(p.validate_value_text('2000 A'))

if __name__ == '__main__':
    unittest.main()

