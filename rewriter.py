#!/usr/bin/python -u

import sys
import re
import json

def create_element(element_data):
    type = element_data['type']
    if type == 'ladybug':
        return { 'type' : type,
                 'name' : element_data['name'],
                 'spots' : int(element_data['spots']) }
    elif type == 'ant':
        return { 'type' : type,
                 'name' : element_data['name'],
                 'age' : int(element_data['age']),
                 'role' : element_data['role'] }


def transform_log_entry(entry):
    pentry = json.loads(entry)

    new_entry = { 'time' : '', 'elements' : [], 'msg' : '', 'host' : '' }

    last_index = 0
    element_data = { }
    elements = [ ]

    for key, val in sorted(pentry['$!'].items()):
        if key.startswith('el.'):
            v = key[3:].partition('.')
            index = int(v[0])
            slot = v[2]
            if (index == last_index):
                element_data[slot] = val
            else:
                if 'type' in element_data:
                    elements.append(create_element(element_data))
                else:
                    print("No type given for element " + str(index))
                element_data = { }
                element_data[slot] = val
                last_index = index
    if len(element_data) > 0 and 'type' in element_data:
        elements.append(create_element(element_data))

    new_entry['time'] = pentry['timegenerated']
    new_entry['msg'] = pentry['$!']['msg']
    new_entry['host'] = pentry['$!']['host']
    new_entry['elements'] = elements

    return new_entry


def onInit():
	global outfile
        outfile = open("/home/dboles/scratch/rsyslog/test0/rewriter.trace", "w", 1)

def onReceive(msg):
	global outfile
        xe = transform_log_entry(msg)
        print json.dumps({'msg' : xe})

        outfile.write(msg + '\n\n')
        outfile.write(json.dumps(xe, sort_keys=True, indent=4) + '\n')
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
