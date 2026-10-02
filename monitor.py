import psutil
import time
import os
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
	print("Data Sent :", round(sent,2), "MB")
	print("Data Recev :",round(recieved,2), "MB")
	if cpu>80:
		print("WARNING: High CPU Usage!")
	if memory.percent>80:
		print("WARNING: High RAM Usage!")
	if disk.percent>80:
		print("WARNING: Disk Space is getting LOW!")
	time.sleep(2) 
