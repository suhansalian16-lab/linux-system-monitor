import psutil
import time
import os
old_sent=psutil.net_io_counters().bytes_sent
old_recieved=psutil.net_io_counters().bytes_recv
old_time=time.time()
while True:
	os.system("clear")
	print("======================================")
	print("     SYSTEM MONITOR       ")
	print("======================================")
	cpu=psutil.cpu_percent()
	memory=psutil.virtual_memory()
	print("CPU Usage :", cpu, "%")
	ram_used=memory.used/(1024**3)
	ram_total=memory.total/(1024**3)
	print("RAM Usage :", round(ram_used,2),"/",round(ram_total,2), "GB")
	disk=psutil.disk_usage("/")
	disk_used=disk.used/(1024**3)
	disk_total=disk.total/(1024**3)
	print("Disk Usage:", round(disk_used,2), "/", round(disk_total,2), "GB")
	uptime_seconds=time.time() - psutil.boot_time()
	hours=int(uptime_seconds//3600)
	minutes=int((uptime_seconds%3600)//60)
	print("Uptime :",hours, "hours",minutes, "minutes")
	network = psutil.net_io_counters()
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
	if cpu>80:
		print("WARNING: High CPU Usage!")
	if memory.percent>80:
		print("WARNING: High RAM Usage!")
	if disk.percent>80:
		print("WARNING: Disk Space is getting LOW!")
	old_sent=network.bytes_sent
	old_received=network.bytes_recv
	old_time=current_time
	print("\nTOP PROCESSES")
	processes=[]
	for process in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
		try:
			processes.append(process.info)
		except (psutil.NoSuchProcess,psutil.AcessDenied):
			pass
	processes.sort(key=lambda x:x['cpu_percent'], reverse=True)
	for process in processes[:5]:
		print(process['name'],"CPU:",round(process['cpu_percent'],1),"%", "RAM:",round(process['memory_percent'],1),"%")
	time.sleep(2) 
