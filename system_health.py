import psutil
import logging
import argparse

# Setting up logging config file
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# For Parsing command-line arguments
parser = argparse.ArgumentParser(description='System health monitoring script.')
parser.add_argument('--cpu-threshold', type=int, default=75, help='CPU usage percentage threshold')
parser.add_argument('--memory-threshold', type=int, default=80, help='Memory usage percentage threshold')
parser.add_argument('--disk-threshold', type=int, default=90, help='Disk usage percentage threshold')
args = parser.parse_args()

CPU_THRESHOLD = args.cpu_threshold
MEMORY_THRESHOLD = args.memory_threshold
DISK_THRESHOLD = args.disk_threshold

#Funciton for checking cpu usage
def check_cpu_usage():
    
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
        print(f"Alert: High CPU usage detected: {cpu_usage}%")
    else:
        logging.info(f"CPU usage: {cpu_usage}%")
#Function for checking memory usage
def check_memory_usage():
    
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage detected: {memory_usage}%")
        print(f"Alert: High memory usage detected: {memory_usage}%")
    else:
        logging.info(f"Memory usage: {memory_usage}%")

#Function for checking disk usage and space 
def check_disk_space():
    disk = psutil.disk_usage('/')
    total_space = disk.total / (1024**3)  
    used_space = disk.used / (1024**3)    
    free_space = disk.free / (1024**3)    
    total_percentage = disk.percent
    
    logging.info(f"Total disk space: {total_space:.2f} GB")
    logging.info(f"Used disk space: {used_space:.2f} GB")
    logging.info(f"Free disk space: {free_space:.2f} GB")
    logging.info(f"Disk usage percentage: {total_percentage}%")
    
    if total_percentage > DISK_THRESHOLD:
        logging.warning(f"High disk usage detected: {total_percentage}%")
        print(f"Alert: High disk usage detected: {total_percentage}%")
    else:
        logging.info(f"Disk usage percentage: {total_percentage}%")

def check_running_processes():
    process_count = len(psutil.pids())
    logging.info(f"Number of running processes: {process_count}")

def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()  # Updated function
    check_running_processes()

if __name__ == "__main__":
    main()