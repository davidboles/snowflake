# snowflake

## Purpose

This repository serves to the files used to explore a challenge with using rsyslog to process structured log data.

## Contents

### Generating the Log Messages

The application ultest generates the structured log messages. It is created from the file pair ultest.c and Makefile. It is assumed that libumberlog is installed on the system where ultest is built.

### Rsyslog configuration

The file build.conf serves as a small-scale rsyslog.conf file. I install that file as /etc/rsyslog.conf and run rsyslogd as "/usr/sbin/rsyslogd -dn > logfile"

### Plugin for mmexternal

The python script rewriter.py is the executable invoked by the mmexternal plugin. It is adapted directly from posted credit card number example. The comments were deleted solely for brevity.

### Desired result

The file result.json contains an example desired output from processing the log message originated by ultest. in the general case, the members of the "elements" array can be arbitrary JSON data derived from the flat structured log data generated via ul_syslog().

