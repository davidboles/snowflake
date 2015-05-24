#!/usr/bin/python -u

import sys
import re
import json

def onInit():
	global outfile
        outfile = open("/home/dboles/scratch/rsyslog/test0/rewriter.trace", "w", 1)

def onReceive(msg):
	global outfile
        print json.dumps({'hostname': 'frodo'})

        outfile.write(msg + '\n')
        outfile.flush()

def onExit():
        close(outfile)

onInit()
keepRunning = 1
while keepRunning == 1:
	msg = sys.stdin.readline()
	if msg:
		msg = msg[:len(msg)-1]
		onReceive(msg)
		sys.stdout.flush()
	else:
		keepRunning = 0
onExit()
sys.stdout.flush()
