#!/usr/bin/python3
import os

userlist = ["alpha","beta","gamma"]

print ('')
print ('')

for user in userlist:
	exitcode = os.system("id {}".format(user))
	if exitcode != 0:
		print ('User not exist. Adding user {}'.format(user))
		print ('###########################################################')
		print ('')
		os.system("useradd {}".format(user))
	else:
		print ('User already exits!!!')
		print ('-----------------------------------------------------------')
		print ('')


# Condition to check if group exits or not. add if not exits
exitcode = os.system("grep science /etc/group")
if exitcode != 0:
	print ('Group not exist. Adding group')
	print ('###########################################################')
	print ('')
	os.system("groupadd science")
else:
	print ('Group already exits!!!')
	print ('-----------------------------------------------------------')
	print ('')

# add all users into group
for user in userlist:
	print ('Adding Users!!!')
	print ('***********************************************************')
	print ('')
	os.system("usermod -G science {}".format(user))

# Adding directory
print ('Adding directory!!!')
print ('***********************************************************')
print ('')

if os.path.isdir("/opt/science_dir"):
	print ('directory is existed, skipping it')
else:
	os.mkdir('/opt/science_dir')

# Adding permission
os.system("chown :science /opt/science_dir")
os.system("chmod 770 /opt/science_dir")
