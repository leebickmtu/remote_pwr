#! /usr/bin/env python

import sys
import functions

if ( len(sys.argv) == 3 and sys.argv[1] == 'pulse' and sys.argv[2] == 'pwr' ):
	functions.pulse('pwr')
elif ( len(sys.argv) == 3 and sys.argv[1] == 'pulse' and sys.argv[2] == 'rst' ):
	functions.pulse('rst')
elif ( len(sys.argv) == 3 and sys.argv[1] == 'hold' and sys.argv[2] == 'pwr' ):
	functions.hold('pwr')
elif ( len(sys.argv) == 2 and sys.argv[1] == 'state' ):
	functions.pwr_state()
else:
	print('\nInvalid arguments\n')
	sys.exit(1)

