import os

#Your e-mail address. You will be mailed a report whenever an experiment finishes.
MAILTO='you@your.domain.com'


HOMEDIR = os.getenv("HOME")

#Process directory: Where should information on active processes be stored? There is limited support for multiple hosts if
#you point this to somewhere on a shared mount (e.g. NFS) between hosts.
PROCDIR = HOMEDIR + '/wrexp/proc'

#Log directory: Where should logs be stored?
EXPLOGDIR = HOMEDIR + '/wrexp/logs/'

#How often to poll the status of the experiment? (in seconds)
POLLINTERVAL = 30

#How often do you want the resources logs to be updated with information on CPU and memory usage?
RESINTERVAL = 600 #every 10 minutes


#How often do you want to receive mails with a periodic report on running experiments?
MAILINTERVAL = 6 * 3600 #every 6 hours

#Version Audit. A list of commands to issue for the version log. These are version querying commands intended
#to log some information on the state of the system prior to running an experiment.
# Example:
#VERSION_AUDIT = ['uname -a', 'gcc -v','svn info /path/to/a/svn/project']
VERSION_AUDIT = ['uname -a']

#REMOVE THIS NEXT LINE WHEN DONE CONFIGURING!!!!!!!!!
#raise Exception("PLEASE CONFIGURE wrexpconf.py first!") 
