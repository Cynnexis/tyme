# -*- coding: utf-8 -*-
import unittest
from datetime import time

from tyme_tools.tools import str2time, tyme


class TymeTest(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls) -> None:
		cls.expr_time = {
			"12h - 8h": time(hour=4),
			"(16:- 13h)": time(hour=3),
			"(12h - 8h) + (16:- 13h)": time(hour=7),
			"(12h24 - 8h22) + (16:- 13h)": time(hour=7, minute=2),
			"(12h24 - 8h22) + (16:45- 13h)": time(hour=7, minute=47),
		}
		cls.str_time_valid = {
			"10h": time(hour=10),
			"12h12": time(hour=12, minute=12),
			"12 h12": time(hour=12, minute=12),
			"12h 12": time(hour=12, minute=12),
			"12  h     12": time(hour=12, minute=12),
			"1h25": time(hour=1, minute=25),
			"01h25": time(hour=1, minute=25),
			"10:00": time(hour=10),
			"10:": time(hour=10),
			"12:12": time(hour=12, minute=12),
			"1:25": time(hour=1, minute=25),
			"01:25": time(hour=1, minute=25),
		}
		cls.str_time_invalid = [
			"2595h4569",
			"h24",
			"1",
			"10",
			"2256",
			"1.587",
		]
	
	def test_tyme(self):
		# Test valid inputs
		for (content, actual_time) in self.str_time_valid.items():
			result: time = str2time(content)
			print(f'tyme("{content}") = {result} (actual = {actual_time})')
			self.assertEqual(result, actual_time)
		
		for (expr, actual_time) in self.expr_time.items():
			result: time = tyme(expr)
			print(f'tyme("{expr}") = {result} (actual = {actual_time})')
			self.assertEqual(result, actual_time)
	
	def test_str2time(self):
		# Test valid inputs
		for (content, actual_time) in self.str_time_valid.items():
			result: time = str2time(content)
			print(f'str2time("{content}") = {result} (actual = {actual_time})')
			self.assertEqual(result, actual_time)
		
		# Test invalid inputs
		for invalid_input in self.str_time_invalid:
			self.assertIsNone(str2time(invalid_input))
