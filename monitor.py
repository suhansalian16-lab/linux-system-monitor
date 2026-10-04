import psutil
import time
import os
CPU_LIMIT=80
RAM_LIMIT=80
DISK_LIMIT=80
def get_cpu_usage():
	return psutil.cpu_percent(interval=1)
def get_ram_usage():
	memory=psutil.virtual_memory()
	return memory
def get_disk_usage():
	return psutil.disk_usage("/")
def get_network_usage():
	return psutil.net_io_counters()
def get_process():
	processes=[]
	for process in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
		try:
			processes.append(process.info)
		except (psutil.NoSuchProcess,psutil.AcessDenied):
			pass
	return processes
LOG_FILE="system.log"
old_sent=psutil.net_io_counters().bytes_sent
old_recieved=psutil.net_io_counters().bytes_recv
old_time=time.time()
while True:
	os.system("clear")
	print("======================================")
	print("     SYSTEM MONITOR       ")
	print("======================================")
	cpu=get_cpu_usage()
	memory=get_ram_usage()
	print("CPU Usage :", cpu, "%")
	ram_used=memory.used/(1024**3)
	ram_total=memory.total/(1024**3)
	print("RAM Usage :", round(ram_used,2),"/",round(ram_total,2), "GB")
	disk=get_disk_usage()
	disk_used=disk.used/(1024**3)
	disk_total=disk.total/(1024**3)
	print("Disk Usage:", round(disk_used,2), "/", round(disk_total,2), "GB")
	uptime_seconds=time.time() - psutil.boot_time()
	hours=int(uptime_seconds//3600)
	minutes=int((uptime_seconds%3600)//60)
	print("Uptime :",hours, "hours",minutes, "minutes")
	network = get_network_usage()
	sent=network.bytes_sent/(1024**2)
	recieved=network.bytes_recv/(1024**2)
	current_time=time.time()
	upload_speed=(network.bytes_sent - old_sent)/(current_time - old_time)
	download_speed=(network.bytes_recv - old_recieved)/(current_time - old_time)
	upload_speed=upload_speed/(1024**2)
	download_speed=download_speed/(1024**2)
	print("Data Sent :", round(sent,2), "MB")
	print("Data Recev :",round(recieved,2), "MB")
	print("Upload Speed :",round(upload_speed,2), "MB/s")
	print("Download Speed :",round(download_speed,2), "MB/s")
	with open(LOG_FILE, "a")as log:
		log.write(f"CPU: {cpu}% | " f"RAM: {memory.percent}% |" f"DISK: {disk.percent}% |" f"Upload: {upload_speed:.2f} MB/s |" f"Download: {download_speed:.2f} MB/s\n")
	if cpu>CPU_LIMIT:
		print("WARNING: High CPU Usage!")
	if memory.percent>RAM_LIMIT:
		print("WARNING: High RAM Usage!")
	if disk.percent>DISK_LIMIT:
		print("WARNING: Disk Space is getting LOW!")
	old_sent=network.bytes_sent
	old_received=network.bytes_recv
	old_time=current_time
	print("\nTOP PROCESSES")
	processes=get_process()
	processes.sort(key=lambda x:x['cpu_percent'], reverse=True)
	print("\nTOP CPU PROCESSES")
	for process in processes[:5]:
		print(process['name'],"CPU:",round(process['cpu_percent'],1),"%", "RAM:",round(process['memory_percent'],1),"%")
	processes.sort(key=lambda x:x['memory_percent'],reverse=True)
	print("\n TOP RAM PROCESSES")
	for process in processes[:5]:
		print(process['name'],"RAM:",round(process['memory_percent'],1),"%","CPU:",round(process['cpu_percent'],1),"%")
	time.sleep(2) 
