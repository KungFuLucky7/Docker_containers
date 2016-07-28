# docker_containers
A Python program to manage the execution of software within Docker containers on a single machine. The script accepts a bash command and launches multiple containers to be run simultaneously and independently. The script can collect (STDOUT/STDERR) logs in real-time while the command runs and when the script ends to save them in a logs directory.

### Installation & Requirements:
* Python
* Docker
* Git/GitHub

### Command-line Man Page:
Run this script in this format on the command line:
./docker_containers.py [bash command] [number of containers that's less than or equal to 3]

Test cases to run the script with:
	   ./docker_containers.py "ls -l" 2
		 ./docker_containers.py 0 2
		 ./docker_containers.py "pwd" 2

Notes:
1. You need to provide a bash command and the number of containers for this script!
2. You can only have up to 3 containers running simultaneously
3. You can enter 0 as the first argument for infinite 'hello world' programs. ->  "while true; do echo hello world; sleep 1; done"
4. The Docker image you are running is ubuntu for these containers
5. The STDOUT/STDERR log files can be found in the /logs/ directory

### GitHub Repository Link:
https://github.com/KungFuLucky7/docker_containers