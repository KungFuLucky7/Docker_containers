#!/usr/bin/env python

import sys
import subprocess
import numbers

# Run this script in this format on the command line: ./docker_containers.py [bash command] [number of containers that's less than or equal to 3]
docker_command = ""
if len(sys.argv) == 3 and int(sys.argv[1]) == 0 and int(sys.argv[2]) != 0 and int(sys.argv[2]) <= 3:
  docker_command = "while true; do echo hello world; sleep 1; done"
elif len(sys.argv) == 3 and int(sys.argv[2]) != 0 and int(sys.argv[2]) <= 3:
  print "The command to run in Docker containers is: ", str(sys.argv[1])
  docker_command = str(sys.argv[1])
elif len(sys.argv) == 3 and int(sys.argv[2]) != 0 and int(sys.argv[2]) <= 3:
  raise ValueError("You can only have up to 3 containers running simultaneously")
else:
  raise ValueError("You need to provide a bash command and the number of containers for this script! You can enter 0 as the first argument for infinite 'hellow world' programs.")

for x in range(0, int(sys.argv[2])):
  subprocess.check_call(["docker", "run", "-d", "ubuntu", "/bin/sh", "-c", docker_command])

proc = subprocess.Popen(["docker", "ps", "--format", "'{{.Names}}'"], stdout=subprocess.PIPE)
containers_names = proc.stdout.read()
    
# python switchstatement
def ps():
  """List all containers."""
  subprocess.check_call(["docker", "ps"])
  print "\n"

def stop():
  """Stop a specified container."""
  global containers_names
  print "Please select a specific container to stop:"
  index = 1
  for containers_name in containers_names.split():
    print str(index) + ") " + containers_name.strip('\'')
    index += 1
  try:
    choice = input('>>')
    if int(choice) == 0 or int(choice) > len(containers_names.split()):
      raise ValueError("Your selection is invalid!")
    # Write to stdout & stderr logs
    log_file = open("./logs/" + containers_names.split()[choice - 1].strip('\''), 'w')
    proc = subprocess.Popen(["docker", "logs", containers_names.split()[choice - 1].strip('\'')], stdout=log_file, stderr=log_file)
    subprocess.check_call(["docker", "stop", containers_names.split()[choice - 1].strip('\'')])
    print "Container " + containers_names.split()[choice - 1].strip('\'') + " has been stopped!\n"
    proc = subprocess.Popen(["docker", "ps", "--format", "'{{.Names}}'"], stdout=subprocess.PIPE)
    containers_names = proc.stdout.read()
  except (ValueError, NameError):
    print "Your selection is invalid!"

def exit():
  """Stop all containers."""
  for containers_name in containers_names.split():
    # Write to stdout & stderr logs
    log_file = open("./logs/" + containers_name.strip('\''), 'w')
    proc = subprocess.Popen(["docker", "logs", containers_name.strip('\'')], stdout=log_file, stderr=log_file)
    subprocess.check_call(["docker", "stop", containers_name.strip('\'')])
  print "The command finished executions in all Docker containers!\n"

actions = { 1 : ps,
            2 : stop,
            3 : exit
          }

is_running = True
menu = """Please select from the following menu options:
1) List all containers.
2) Stop a specified container.
3) Stop all containers."""

while (is_running):
  print menu
  try:
    option = input('>>')
    if int(option) == 0 or int(option) > 3:
      raise ValueError("Your selection is invalid!")
    actions[option]()
    if option == 3:
      is_running = False
  except (ValueError, NameError):
    print "Your selection is invalid!"

print "Good bye!"
