#!/usr/bin/python2.7

#Name:  example
#VER: ALFA
#VER NR: 0.1
#LM: 01-02-2014

import time
from RPISC import servo_move
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--left", action="store_true", dest="left", help="if servo should turn left", default=False)
parser.add_option("-r", "--right", action="store_true", dest="right", help="if servo should turn right", default=False)
parser.add_option("-c", "--center", action="store_true", dest="center", help="if servo should back to central point", default=False)
parser.add_option("--manual", dest="manual", help="manual provide data for servo 2.5 - 12.5")

(options, args) = parser.parse_args()

if (options.manual and (12.5 < float(options.manual) or float(options.manual) < 2.5)):
	print "Error, please use value from 2.5 to 12.5"
	sys.exit()

if options.left:
	servo_move(12.5)
	print 'Left'

if options.center:
	servo_move(7.5)
	print 'Center'

if options.right:
	servo_move(2.5)
	print 'Right'

if options.manual:
	servo_move(float(options.manual))
	print 'move manula to:',options.manual
