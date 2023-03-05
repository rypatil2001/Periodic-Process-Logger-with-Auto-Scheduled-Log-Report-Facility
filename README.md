# Periodic-Process-Logger-with-Auto-Scheduled-Log-Report-Facility

### Description :
Developed an algorithm which creates a log file with the current time-stamp and stores information 
about all running processes along with their name, PID, PPID, memory usage, and thread count number of the child process.
This automation script executes periodically depending on the time specified by the user using the scheduler.
After periodic execution, Algorithm sends the log file to the specified email address.

### Scheduling in Python 
 -Schedule is in-process scheduler for periodic jobs that use the builder pattern for 
  configuration. 
  
 -Schedule lets you run Python functions (or any other callable) periodically at pre-determined 
  intervals using a simple, human-friendly syntax. 
  
 -Schedule Library is used to schedule a task at a particular time every day or a 
  particular day of a week. 
  
 -We can also set time in 24 hours format that when a task should run. 
 
 -Basically, Schedule Library matches your systems time to that of scheduled time set by 
  you. 
  
 -Once the scheduled time and system time matches the job function (command function 
  that is scheduled ) is called. 
  
  Before using schedule library we have to install it as 
  ### Installation of Schedule module 
  -   pip install schedule 
  
  
  ### Classes and methods from schedule library 
  
  schedule.Scheduler class 
  
  
  - schedule.every(interval=1) 
  Calls every on the default scheduler instance. 
  Schedule a new periodic job. 
  
  
  
  - schedule.run_pending() 
  Calls run_pending on the default scheduler instance. 
  Run all jobs that are scheduled to run. 
  
  
  
  - schedule.run _all(delay seconds=0) 
  Calls run_all on the default scheduler instance. 
  Run all jobs regardless if they are scheduled to run or not.
  
  
  - schedule.idle seconds() 
  Calls idle_seconds on the default scheduler instance. 
  
  
  - schedule.next run() 
  Calls next_run on the default scheduler instance. 
  Datetime when the next job should run. 
  
  
  - schedule.cancel jobiob()
  Calls cancel_job on the default scheduler instance. 
  Delete a scheduled job. 
