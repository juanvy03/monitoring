#!/usr/bin/python3

import re
import sys
import subprocess

# Requisites:
# - SSH connection by KEYs
#
# Usage:
#  python3 checkIBMicpu.py <HOST> -w <WARNING> -c <CRITICAL>
#
#                             jmaillourbano@gmail.com
################

USER = "user"
HOST = str(sys.argv[1])
SSHCOMM = "ssh"
SSHLOGIN = "{0}@{1}".format(USER, HOST) #HOST
SHHCOMMAND = "system DSPSYSSTS"
WARNING = sys.argv[3]
CRITICAL = sys.argv[5]
indexLower = 21 # Fixed Indexes for OUTPUT
indexHigher = 22 # Fixed Indexes for OUTPUT

ssh = subprocess.Popen([SSHCOMM, SSHLOGIN, SHHCOMMAND],
                        shell = False, #False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)

result = ssh.stdout.readlines()

perc = str(result[2]).split(' ')

if (result == []):
    error = str(ssh.stdout.readlines())
    print("Error: {}".format(error))
else:
    if (len(perc[indexHigher]) == 0):
        percNoComma = perc[indexLower].split(',')[0]
        if(int(percNoComma) < 95):
            print("CPU OK - Usage is: {} %".format(perc[indexLower]))
            sys.exit(0)
        elif(int(percNoComma) >= WARNING):
            print("CPU WARNING - Usage is: {} %".format(perc[indexLower]))
            sys.exit(1)
        elif(int(percNoComma) > CRITICAL):
            print("CPU CRITICAL - Usage is: {} %".format(perc[indexLower]))
            sys.exit(2)
    else:
        percNoComma = perc[indexHigher].split(',')[0]
        if(int(percNoComma) < 95):
            print("CPU OK - Usage is: {} %".format(perc[indexHigher]))
            sys.exit(0)
        elif(int(percNoComma) >= WARNING):
            print("CPU WARNING - Usage is: {} %".format(perc[indexHigher]))
            sys.exit(1)
        elif(int(percNoComma) > CRITICAL):
            print("CPU CRITICAL - Usage is: {} %".format(perc[indexHigher]))
            sys.exit(2)
