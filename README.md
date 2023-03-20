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
  
 
  - schedule.every(interval=1) 
  Calls every on the default scheduler instance. 
  Schedule a new periodic job. 
  
  
  
  - schedule.run_pending() 
  Calls run_pending on the default scheduler instance. 
  Run all jobs that are scheduled to run. 
  
  
  
  - schedule.run _all(delay seconds=0) 
  Calls run_all on the default scheduler instance. 
  Run all jobs regardless if they are scheduled to run or not.
  
  

  
  
# Brief Summary
### This script is used to create a log of all running processes and send it to a specific email address. It runs as a scheduled task and can be set to run every specified number of minutes using command-line arguments.

The main() function is the entry point of the script. It checks the number of command-line arguments and prints usage information if necessary. It also initializes the scheduled task using the schedule library.

The ProcessLog() function creates a log file of all running processes and saves it in a specified directory. It uses the psutil library to get information about the running processes. The log file is created with a unique timestamp so that multiple log files can be created without overwriting each other. If an internet connection is available, the log file is sent as an attachment to a specified email address using the smtplib library.

The is_connected() function checks if an internet connection is available by trying to connect to www.google.com. If the connection is successful, it returns True, otherwise it returns False.

The MailSender() function sends an email with the log file attached using the smtplib library. It takes the log file name and timestamp as arguments and uses them to construct the email message. The sender email, receiver email, and password are hardcoded in the function, so they need to be changed to match the actual email addresses and password used.

#### Overall, this script provides a useful way to monitor running processes on a computer and receive updates via email. It could be useful for system administrators or anyone who needs to keep track of the processes running on their computer.
  
 ## For Testing We have Set the Frequency to 1 Minute (Log File Logger will run every 1 Minute)
 ## Application Accepts inputs through COMMAND LINE ARGUMENTS IN TERMINAL
  
 # Usage (Terminal): 
![ComandLineArguments](https://user-images.githubusercontent.com/123350287/226370155-e1cfe886-aecb-43c0-b961-fc16a2bebb8e.JPG)


# Running Process

![created](https://user-images.githubusercontent.com/123350287/226372531-135d966f-047d-499b-ad0c-512ae2f85a5d.JPG)

# Running Processes at frequency of 1 Minute along with the timeStamp in Filename
![Terminalop](https://user-images.githubusercontent.com/123350287/226375752-baa09655-09aa-4941-b93c-8819230f5592.JPG)


# LogFile Saved in specified Bucket (Directory)
![Directory1](https://user-images.githubusercontent.com/123350287/226375907-f0ae11cc-226b-43cd-8d10-f3657dfb6715.JPG)

# Log Files created every Minute Inside Log_File_Bucket Directory
![Bucketlogs](https://user-images.githubusercontent.com/123350287/226377355-751598d2-059f-4314-9cd7-070821ee4301.JPG)

# Inside Log File 

![LogFIleInside](https://user-images.githubusercontent.com/123350287/226378474-9a2d4668-707e-475e-bc0a-c111aa0e0b39.JPG)

# Mails

![MailsIn](https://user-images.githubusercontent.com/123350287/226378963-e66bfc9c-23f4-4fe1-8059-8b0b2bed8c25.JPG)


# Inside Mail

![inside Mail](https://user-images.githubusercontent.com/123350287/226380149-41ba9614-27a4-48ae-b2ba-9ed1856458aa.JPG)

#                                                              -Raj Patil
