#!/usr/bin/env python3

import re
import argparse
import os

#remove Empty Elements from list
def removeEmptyElements(line_list):
    return [x for x in line_list if x != '']

def ical2xml(icalData):
    #Detectecting new line and split into list
    #Append all elements with tab or space as first character to previous element and delete
    #the element with tab or space
    lines = icalData.replace('\r','').replace('\n ',' ').split('\n')

    #Remove empty elements
    lines = removeEmptyElements(lines)

    #Begin with xml version
    xml='<?xml version="1.0"?>\n'

    #Line mathes PROPERTYNAME;ATTRIBUTES:VALUE
    for line in lines:
        result=re.findall('^([^:^;]*)(?:;([^:]*))?:(.*)$',line)
        propertyName=result[0][0]
        attributes=result[0][1].split(';')
        value=result[0][2]

        #Replace BEGIN: as a start tag
        if propertyName == 'BEGIN':
            xml += '<'+value+'>\n'
            #Replace END: as an end tag 
        elif propertyName == 'END':
            xml += '</'+value+'>\n'
        else:
        #Build start and end tag in single line. Attributes in ics will be attributes in the XML file
            xml += '<'+propertyName
            if attributes != ['']:
                for a in attributes:
                    att=a.split('=')
                    xml += ' ' + att[0].replace(' ','') +'=\'' + att[1] + '\' '
            xml += '>' + value + '</'+propertyName+'>\n'
    return xml

# Main loop
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts iCal to XML')
    parser.add_argument("-o", "--output", help="XML output file path")
    parser.add_argument("input", help="iCal input - filepath or iCal string")
    args = parser.parse_args()

    if os.path.isfile(args.input):
        with open(args.input,'r') as ifile:
            text_ical=ifile.read()
            xml=ical2xml(text_ical)
    else:
        xml=ical2xml(args.input)

    if args.output:
        with open(args.output,'w') as ofile:
            ofile.write(xml)
    else:
        print(xml,end='')

