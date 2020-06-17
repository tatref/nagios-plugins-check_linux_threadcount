# Description:
This Nagios Plugin calculates count of threads for one or more Linux process(es). One can give pid number or pid file path to identify the unique process. pid_cmd_regex is useful when monitoring sum of thread counts for multiple processes.

# Usage:

`<python_interpreter_path> check_linux_threadcount.py {-w,--warn} <warning_treshold> {-c,--crit} <critical_treshold> {--pid_number,--pid_file,--pid_cmd_regex} <pid_argument>`

# Examples:
Monitoring the process with pid number 1757:
  
`/usr/bin/python check_linux_threadcount.py -w 1500 -c 2000 --pid_number 1757`
  
Monitoring the process by using pid file using python3:
  
`/usr/bin/python3 check_linux_threadcount.py --warn 2000 --crit 2200 --pid_file /var/run/autofs.pid`
  
Getting sum of the thread counts for multiple jboss instances using Python version 2.7:
  
`/usr/bin/python2.7 check_linux_threadcount.py -w 1500 -c 2000 --pid_cmd_regex ".*org.jboss.Main.*"`
