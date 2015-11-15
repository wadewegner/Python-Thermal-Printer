from __future__ import print_function
import urllib, time, json, urllib2, re
from Adafruit_Thermal import *
from xml.dom.minidom import parseString

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

text = urllib2.urlopen('http://rpprinter.azurewebsites.net/api/unread').read()

messages = json.loads(text)

for message in messages:
	printer.print('\"' + message["Text"] + '\" from ' + message["FromEmail"] + '.')
	printer.feed(3)

#printer.print("testing 123")

#printer.feed(3)

#print("complete")