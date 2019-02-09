#!/usr/bin/env python3

# Project "ical2xml"
# Copyright (C) 2019

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import re
import argparse
import os
import sys


# remove Empty Elements from list
def removeEmptyElements(line_list):
    return [x for x in line_list if x != '']


def ical2xml(icalData):
    # Detectecting new line and split into list
    # Append all elements with tab or space as first character to previous
    # element and delete the element with tab or space
    lines = icalData.replace('\r', '').replace('\n ', ' ').split('\n')

    # Remove empty elements
    lines = removeEmptyElements(lines)

    # Begin with xml version
    xml = '<?xml version="1.0"?>\n'

    # Line mathes PROPERTYNAME;ATTRIBUTES:VALUE
    for line in lines:
        result = re.findall('^([^:^;]*)(?:;([^:]*))?:(.*)$', line)
        propertyName = result[0][0]
        attributes = result[0][1].split(';')
        value = result[0][2]

        # Replace BEGIN: as a start tag
        if propertyName == 'BEGIN':
            xml += '<' + value + '>\n'
            # Replace END: as an end tag
        elif propertyName == 'END':
            xml += '</'+value+'>\n'
        else:
            # Build start and end tag in single line. Attributes in ics will be
            # attributes in the XML file
            xml += '<' + propertyName
            if attributes != ['']:
                for a in attributes:
                    att = a.split('=')
                    xml += ' ' + att[0].replace(' ', '')
                    xml += '=\'' + att[1] + '\' '
            xml += '>' + value + '</'+propertyName+'>\n'
    return xml


# Main loop
if __name__ == '__main__':

    # Initialize CLI
    parser = argparse.ArgumentParser(description='Converts iCal to XML')
    parser.add_argument("-o", "--output", help="XML output file path")

    # read from pipe
    if not sys.stdin.isatty():
        inputString = sys.stdin.read()
        args = parser.parse_args()
    else:
        parser.add_argument("input", help="iCal input-filepath or iCal string")
        args = parser.parse_args()
        inputString = args.input

    # Check if input is a path to a file and read the file
    if os.path.isfile(inputString):
        with open(inputString, 'r') as ifile:
            text_ical = ifile.read()
            xml = ical2xml(text_ical)

    # if input is not a file read as iCal string
    else:
        xml = ical2xml(inputString)

    # check for optional output file path
    if args.output:
        with open(args.output, 'w') as ofile:
            ofile.write(xml)

    # if no file path is given print xml file
    else:
        sys.stdout.write(xml)
