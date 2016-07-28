Title: A Python program to manage the execution of software within Docker containers on a single machine

Author: Terry Chun Wong

Date: 7/27/2016

Abstract
This project is a development for a Python program to manage the execution of software within Docker containers on a single machine. The script accepts a bash command and launches multiple containers to be run simultaneously and independently. The script can collect (STDOUT/STDERR) logs in real-time while the command runs and when the script ends to save them in a logs directory.

1. Requirements Analysis
   * A script written in Python that can launch multiple Docker containers to execute a certain bash command
	 * List the initiated containers
	 * Log a specified container for (STDOUT/STDERR) outputs in real-time while the command runs
	 * Stop a specified container without losing any logs
	 * Write logs and clean up the process before exiting the program
	 * Proper error handling
	 * The boot time shall be limited to 1 seconds
	 * The shutdown time shall be limited to 2 seconds

2. System Architecture
   * The Docker image that the script runs for multiple containers is ubuntu for a general linux environment
   * The number of running containers is currently limited to 3 for optimal performance
	 * The Docker containers will run the same bash command from the command-line argument list of the script simultaneously and independently to reduce conflicts between processes
	 * The script has a text-based menu UI for system/servers administration
	 * Error handling messages will be printed to the terminal
	 * There is a /logs/ directory to store all the collected (STDOUT/STDERR) logs from containers

3. Evaluation
   * Test cases to run the script with:
	   ./docker_containers.py "ls -l" 2
		 ./docker_containers.py 0 2
		 ./docker_containers.py "pwd" 2
	 * The program is tested to be fully functional and operable according to requirements
	 * The program is highly scalable and extendable

4. Conclusions and Future Work
   All the requirements goals are met and this project is deemed successful. In the future, there's scalable work to done to increase the scope and size of the project such as increasing the number of simultaneously running containers, deploy the program as a Cloud service, have different containers work on different tasks, fine-tune server performance by identifying bottleneck devices and utilization rates, and supporting Big Data technology, etc. Due to the highly scalable and extendable nature of this project, any improvements using new technologies should be adaptable for efficiency and optimal performance.


