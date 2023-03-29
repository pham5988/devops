from fabric.api import *

def greeting(msg):
  print ('Good {}'.format(msg))

# show info local machine

def system_info():
  print ("Disk space")
  local ("df -h")

  print ("RAM")
  local ("free -m")

  print ("Uptime")
  local ("uptime")

# remote to another machines

def remote_exec():
  print ("Get system info")
  run ("hostname")
  run ("df -h")
  run ("free -m")
  run ("uptime")
