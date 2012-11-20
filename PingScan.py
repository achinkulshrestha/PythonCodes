"""usage: PROGRAM <subnet address> <...>
Active IP Finder (Looking for movie shares)
Example:
  Find all active IP's in the subnet
  $ PROGRAM 192.168.1.*

Copyright (C) 2007 Achin Kulshrestha, mail: achinkul@gmail.com
"""

import subprocess

addr = raw_input("Enter the IP address in form of <192.168.1.*>: ")

if(addr):
    netmask_host = addr.split('*')
if(len(netmask_host) > 0):
    print "Starting Ping Scan...\n\n"
    for i in range(255):
        ip = netmask_host[0] + str(i)

        ret = subprocess.call("ping -n 1 %s" % ip, shell=True)

        if ret == 0:
            print "%s: is alive\n" % ip
        else:
            print "%s: didn't respond\n" % ip




