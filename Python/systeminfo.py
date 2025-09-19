import platform 
import psutil

print(f"System: {platform.system()}")
print(f"Release: {platform.release()}")
print(f"Version: {platform.version()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")
print(f"Python Version: {platform.python_version()}")

print(f"CPU count (logical): {psutil.cpu_count()}")
print(f"CPU count (physical): {psutil.cpu_count(logical=False)}")
print(f"CPU usage (per core): {psutil.cpu_percent(interval=1, percpu=True)}")
print(f"Overall CPU usage: {psutil.cpu_percent(interval=1)}")

mem = psutil.virtual_memory()
print(f"Total memory: {mem.total / (1024**3):.2f} GB")
print(f"Used memory: {mem.used / (1024**3):.2f} GB")
print(f"Available memory: {mem.available / (1024**3):.2f} GB")
print(f"Memory usage percentage: {mem.percent}%")

swap_mem = psutil.swap_memory()
print(f"Total swap memory: {swap_mem.total / (1024**3):.2f} GB")
print(f"Used swap memory: {swap_mem.used / (1024**3):.2f} GB")
print(f"Swap memory usage percentage: {swap_mem.percent}%")

disk_usage = psutil.disk_usage('/')
print(f"Total disk space: {disk_usage.total / (1024**3):.2f} GB")
print(f"Used disk space: {disk_usage.used / (1024**3):.2f} GB")
print(f"Free disk space: {disk_usage.free / (1024**3):.2f} GB")
print(f"Disk usage percentage: {disk_usage.percent}%")

print("Disk partitions:")
for partition in psutil.disk_partitions():
    print(f"  Device: {partition.device}, Mountpoint: {partition.mountpoint}, Filesystem: {partition.fstype}")

net_io = psutil.net_io_counters()
print(f"Bytes sent: {net_io.bytes_sent / (1024**2):.2f} MB")
print(f"Bytes received: {net_io.bytes_recv / (1024**2):.2f} MB")

from datetime import datetime
boot_time_timestamp = psutil.boot_time()
boot_time_datetime = datetime.fromtimestamp(boot_time_timestamp)
print(f"System boot time: {boot_time_datetime}")