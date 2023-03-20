import os
import time
import psutil
import socket
import smtplib                       # SIMPLE MAIL TRANSFER PROTOCOL
import schedule
import datetime
from datetime import datetime
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


# This function returns True if Internet is connected
def is_connected():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False



def MailSender(filename, time,mail_reciever):
    try:
        mail_sender = 'jypatil1601@gmail.com'

        mail_pass = 'obwsdjjnxwffmsxi'
        msg = MIMEMultipart()
        msg['From'] = mail_sender
        msg['To'] = mail_reciever
        # Message Body
        body = """
        Hello % s, Welcome. 
        Please find attached document which contains 
        Log of Running process. 
        Log file is created at: %s
        This is an auto Generated Mail
        
        
        Thanks & Regards,
        Raj Patil
        """%(mail_reciever, time)
        Subject = """
        Process log generated at : %s
        """%(time)
        msg['Subject'] = Subject
        msg.attach(MIMEText(body, 'plain'))
        attachment = open(filename, "rb")
        p =MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(mail_sender,mail_pass)
        text = msg.as_string()
        s.sendmail(mail_sender, mail_reciever, text)
        s.quit()

        print("Log file successfully sent through Mail at :",mail_reciever)
    except Exception as E:
        print("Unable to send mail.", E)

# Log FiLe Creation
def ProcessLog(log_dir = "Log_File_Bucket",MailR = argv[2]):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    # log file creation
    seperator = "-" * 80

    timestr = datetime.now().strftime("%d_%m_%Y - %H-%M-%S")
    log_path = os.path.join(log_dir,"ProcessLog_" + timestr + ".log")  # os.path.join() method in Python join one or more path components intelligently
    f = open(log_path, 'w')  # CREATES NEW FILE THEN OPENS IT TO WRITE

    f.write(seperator + "\n")
    f.write("Raj Infosystems process Logger       : " + time.ctime() + "\n")
    f.write(seperator + "\n")

    for proc in psutil.process_iter():

        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms / (
                        1024 * 1024)  # vms = memory alocated for process to run [virtual memory size in bytes]
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)


    print("Log file is successfully generated at location ",(log_path))
    connected = is_connected()

    if connected:
        timestr = datetime.now().strftime("%d_%m_%Y - %H;%M;%S")
        #startTime = timestr
        MailSender(log_path, timestr,MailR)
        #endTime = time.time()
        #print('Took %s seconds to send mail' % (endTime - startTime))
    else:
        print("There is no internet connection")

def main():
    print("-"*100)
    print("Application name: " +argv[0])
    print("Current Time is  :", datetime.now())


    if (len(argv) != 3):
        print("Error: Invalid number of arguments")
        print("USAGE : python File_Name  Interval_in_minutes  Reciever_mail_id")
        print("-" * 100)
        print(" EG : python Filename 1")
        print("-" * 100)
        print("      Every 1 MINUTE  ")
        print("      Script will create a Log file of all running processes after ")
        print("      and send it to the Mentioned Email address ")
        exit()
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used log record of running processes and send it to Specific Email address")
        print("")
        exit()
    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage ApplicationName AbsolutePath_of_Directory")
        print("")
        exit()


    print("------------------Raj Automations---------------------------------")
    print("------------------Process started successfully--------------------")
    print("------------------Check Log_File_Bucket---------------------------")

# Scheduling the Task
    try:
        Minutes = int(argv[1])

        print("------------------Script will Run every",Minutes,"Minutes-----------------")
        schedule.every(Minutes).minutes.do(ProcessLog)

        while True:
          schedule.run_pending()
          time.sleep(1)

    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception as E:
        print("Error Invalid input",E)

if __name__ == "__main__":
    main()
