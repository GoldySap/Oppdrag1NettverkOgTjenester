# Nettverk og Tjenester - Oppdrag 1, 2IMI Uke 38 2025
## Nettverk og tilkobling
Først koblet jeg pcen og Rasberry Pien til klassens LAN nettverket med navn 2IMI - passord IMKuben1337!
Så satt jeg Rasberry Pien: 
* Statisk IP av 10.200.14.20
* Nettmask (subnet mask) til 255.0.0.0
* Gateway til 10.0.0.1
* DNS til 10.0.0.10

Etter det testet jeg å pinge Pien fra PCen

<img width="50%" height="50%" alt="image" src="https://github.com/user-attachments/assets/f92b3026-5aea-42a7-a041-de10a5bc8495" />

## Server og tjenester
Jeg startet med å updatere filene mine og installere apace2/verifisere at jeg har apache2.
bilde

Så oppdaterte jeg brannmuren til å tilate apache serveren.
bilde

Til slutt la jeg til min egen netside som apache skal kjøre og testet apache serveren med å få tilgang til nettsiden, med å skrive IPen 10.200.14.20 og få min nettside.
<img width="50%" height="50%" alt="image" src="https://github.com/user-attachments/assets/a58d36c3-e4eb-4b83-9c3d-c15219a559f5" />

Etter å få resultatet valgte jeg å laste ned samba.

Får at folderen skal deles må jeg legge til: 
```
[sambashare]
  comment = Samba on Ubuntu
  path = /home/alexsi/sambashare
  read only = no
  browsable = yes
```
I konfigurations filen, lagre, og restarte samba med `Sudo service smdb restart` Eller `Sudo systemctl smbd restart` kommandoene.

<img width="50%" height="50%" alt="Screenshot From 2025-09-17 09-46-19" src="https://github.com/user-attachments/assets/b60e659f-9e25-4422-89f2-526ae2fd022b" />

Til slutt la jeg til en test fil og fikk sambashare folderen til å dele.

<img width="50%" height="50%" alt="image" src="https://github.com/user-attachments/assets/17a9dac7-5394-435f-b951-b9edf6056b3d" />


## Python og github
Først lagde jeg en github og klonet den til pcen min.
Så lagde jeg en python fil som skal hvise system detaljer, som type system, version, cpu detaljer, uptime, etc. Så klonet jeg reposetorien til Rasberry Pien og testet at python filenfunket.

Koden:
```Python
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

disk_usage = psutil.disk_usage('/') # Replace '/' with the desired path for other drives
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
```
