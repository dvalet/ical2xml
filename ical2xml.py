#!/usr/bin/env python3

import re
import argparse
import os

def ical2xml(icalData):
	#Detectecting new line and split into list
	lines = icalData.replace('\r','').split('\n')
	#Remove empty elements
	lines = [x for x in lines if x != '']

	#Append all elements with tab or space as first charecter to previous element and delete
	#the element with tab or space
	i=0
	for m in range(1,len(lines)):
		if lines[m-i][0]==' ' or lines[m-i][0]=='\t':
			lines[m-1-i] += lines[m-i]
			del(lines[m-i])
			i += 1
	#Begin with xml version
	xml='<?xml version="1.0"?>\n'

	#Line mathes PROPERTYNAME;ATTRIBUTES:VALUE
	for line in lines:
		erg=re.findall('^([^:^;]*)(?:;([^:]*))?:(.*)$',line)
		propertyName=erg[0][0]
		attributes=erg[0][1].split(';')
		value=erg[0][2]
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
		
