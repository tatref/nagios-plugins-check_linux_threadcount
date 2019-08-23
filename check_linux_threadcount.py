#!/usr/bin/env python
#Original version by kadirsert https://github.com/kadirsert/nagios-plugins-check_linux_threadcount
#updated by Nozlaf to include perfdata so we can make pretty graphs

import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--warn", help="Warning treshold for thread count", type=int, default=5)
parser.add_argument("-c", "--crit", help="Alert treshold for thread count", type=int, default=10)
parser.add_argument("-pn", "--pid_number", help="Identify a process by pid number", type=int)
parser.add_argument("-pf", "--pid_file", help="Identify a process by pid file")
parser.add_argument("-pr", "--pid_cmd_regex", help="Identify process(es) by using a regular expression")
args = parser.parse_args()

if (args.pid_number is None) and (args.pid_file is None) and (args.pid_cmd_regex is None):
    print "Please provide one of these arguments (--pid_number , --pid_file , --pid_cmd_regex) to identify process pids"
    sys.exit(3)

if args.pid_number is not None:
    thread_count = int(os.popen('ls /proc/' + str(args.pid_number) + '/task/ |wc -l').read())
if args.pid_file is not None:
    f = open(args.pid_file, "r")
    pid_num = f.readline().strip()
    thread_count = int(os.popen('ls /proc/' + pid_num + '/task/ |wc -l').read())
if args.pid_cmd_regex is not None:
    pid_list = os.popen('ps -ef |grep ' + args.pid_cmd_regex + ' |grep -v check_linux_threadcount |grep -v grep |awk \'{print $2}\'').read()
    thread_count = 0
    for pid_num in pid_list.strip().splitlines():
        thread_count = thread_count + int(os.popen('ls /proc/' + pid_num + '/task/ |wc -l').read())

perfdata = "threads="+ str(thread_count)+ ";" + str(args.warn) + ";" + str(args.crit) + ";;"

        
if (thread_count >= int(args.crit)):
    print "Thread count is in CRITICAL state: (" + str(thread_count)  + ") |" + str(perfdata)
    sys.exit(2)
elif (thread_count >= int(args.warn)):
    print "Thread count is in WARNING state: (" + str(thread_count)  + ") |" + str(perfdata)
    sys.exit(1)
else:
    print "Thread count is OK |" + str(perfdata)
    sys.exit(0)
