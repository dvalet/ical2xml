#!/usr/bin/env python3

import unittest
from ical2xml import ical2xml

class TestIcal2XmlMethods(unittest.TestCase):
	__xml_version__='<?xml version="1.0"?>\n'
	
	def test_BEGIN_END(self):
		ical="BEGIN:KEY\nEND:KEY"
		xml=self.__xml_version__ + "<KEY>\n</KEY>\n"
		self.assertEqual(ical2xml(ical), xml)

	def test_remove_backslash_r(self):
		ical="\r\n\r"
		xml=self.__xml_version__ 
		self.assertEqual(ical2xml(ical), xml)

	def test_remove_empty_lines(self):
		ical="BEGIN:KEY\n\nEND:KEY"
		xml=self.__xml_version__ + "<KEY>\n</KEY>\n"
		self.assertEqual(ical2xml(ical), xml)

	def test_key_value(self):
		ical="KEY:value\n"
		xml=self.__xml_version__ + "<KEY>value</KEY>\n"
		self.assertEqual(ical2xml(ical), xml)

	def test_second_line(self):
		ical="KEY:line1\n line2\n"
		xml=self.__xml_version__ + "<KEY>line1 line2</KEY>\n"
		self.assertEqual(ical2xml(ical), xml)

	def test_attributes(self):
		ical="KEY;ATTRIBUTE1=VALUE1;ATTRIBUTE2=VALUE2:VALUE\n"
		xml=self.__xml_version__ + "<KEY ATTRIBUTE1=\'VALUE1\'  ATTRIBUTE2=\'VALUE2\' >VALUE</KEY>\n"
		self.assertEqual(ical2xml(ical), xml)



if __name__ == '__main__':
    unittest.main()
