import subprocess

def getIP(hostName):
  pingCmd = "ping -c 1 " + hostName + " | grep \"" + hostName + "\" | awk 'NR==1{sub(/\(/, \"\",$3); sub(/\)/, \"\",$3); printf \"%s\", $3}'"
  ip = subprocess.Popen(pingCmd, stdout=subprocess.PIPE, stderr=None, shell=True).communicate()[0].decode("utf-8")
  return ip
