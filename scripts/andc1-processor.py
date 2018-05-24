#!/usr/bin/python


import os, platform, subprocess, re, sys

# print "This is the name of the script: ", sys.argv[0]
# print "Number of arguments: ", len(sys.argv)
# print "The arguments are: " , str(sys.argv)
print 'Aurora Networx DC1 Processor v1.0'
def get_processor_name():
    if platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub( ".*model name.*:", "", line,1)
    return ""

from datetime import timedelta

with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    uptime_string = str(timedelta(seconds = uptime_seconds))

print "\nSystem Uptime: ", (uptime_string)

def check_availability (arg1):
    host = str(sys.argv[0])
    command = "ping", arg1
    return
check_availability(sys.argv[0])


print 'FQDN :', gethostbyname
print 'Disk Usage :'
print 'Kernel Version : '
print get_processor_name()
