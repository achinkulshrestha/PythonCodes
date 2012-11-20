"""usage: PROGRAM <subnet address> <...>
A Multithreaded Active IP Finder (Looking for movie shares)
Example:
  Find all active IP's in the subnet
  $ PROGRAM 192.168.1.*

Copyright (C) 2007 Achin Kulshrestha, mail: achinkul@gmail.com
"""
from threading import Thread
import subprocess
from Queue import Queue

no_of_threads = 5

def get_store_ips():
    addr = raw_input("Enter the IP address in form of <192.168.1.*>: ")
    ips= []
    if(addr):
        netmask_host = addr.split('*')
    if(len(netmask_host) > 0):
        for i in range(255):
            ips.append(netmask_host[0] + str(i))
    return ips

def start_pinging(thread_no,queue):
    while True:
        ip = queue.get()
        print "Thread %s: Pinging %s\n" % (thread_no, ip)
        ret = subprocess.call("ping -n 1 %s" % ip, shell=True)

        if ret == 0:
            print "%s: is alive\n" % ip
        else:
            print "%s: didn't respond\n" % ip

def main():
    ips = get_store_ips()
    queue = Queue()
    for ip in ips:
        queue.put(ip)

    for thread_no in range(no_of_threads):
        threadie = Thread(target=start_pinging, args=(thread_no, queue))
        threadie.setDaemon(True)
        threadie.start()
    queue.join()

    print "Scan Complete... (:"
    
if __name__=="__main__":
    main()
