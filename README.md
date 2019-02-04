# ical2xml
ical2xml converter

#### Example:

| iCal          | XML           |
| ------------- |-------------|
|               | \<?xml version="1.0"?\> |
|BEGIN:VCALENDAR| \<VCALENDAR\> |
|VERSION:2.0    | \<VERSION\>2.0\</VERSION\>|           
|BEGIN:VEVENT   | \<VEVENT\>    |
|ORGANIZER;CN="Peter, Example Inc.":MAILTO:peter@example.com | \<ORGANIZER CN='"Peter, Example Inc."' \>MAILTO:peter@example.com\</ORGANIZER\>  |
|LOCATION:Somewhere | \<LOCATION\>Somewhere\</LOCATION\> |
|SUMMARY:Short summary|\<SUMMARY\>Short summary\</SUMMARY\>
|DESCRIPTION:Long description <br /> with several lines|\<DESCRIPTION\>Long description with several lines\</DESCRIPTION\>
|DTSTART:20190101T220000Z|\<DTSTART\>20190101T220000Z\</DTSTART\>
|DTEND:20190101T215900Z|\<DTEND\>20190101T215900Z\</DTEND\>
|DTSTAMP:20181201T125900Z|\<DTSTAMP\>20181201T125900Z\</DTSTAMP\>
|END:VEVENT|\</VEVENT\>
|END:VCALENDAR|\</VCALENDAR\>

