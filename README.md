# Nettverk og Tjenester - Oppdrag 1, 2IMI Uke 38 2025
## Nettverk og tilkobling
Først koblet jeg Rasberry Pien til nettverket: __Kuben.it__ - passord: `IMKuben1337!`

Så konfigurerte jeg wifi settings til Rasberry Pien: 
* Statisk IP: 10.200.14.20
* Nettmask (subnet mask): 255.0.0.0
* Gateway: 10.0.0.1
* DNS: 10.0.0.10

<img width="50%" height="50%" alt="Screenshot From 2025-09-16 10-38-12" src="https://github.com/user-attachments/assets/d2a1268c-8296-42a3-bea1-15bbcb3a8016" />

Så brukte jeg `ip a` kommandoen i terminalen for å skjekke Rasberry Pien sin IP

<img width="50%" height="50%" alt="Screenshot From 2025-09-17 11-49-28" src="https://github.com/user-attachments/assets/f8d90908-10ec-40be-b208-94650265caab" />


Etter det testet jeg å pinge Rasberry Pien, med `ping 10.200.14.20` kommandoen, fra PCen får å verifisere tilkoblingen og feilsøke om jeg skrev noe feil.

<img width="50%" height="50%" alt="image" src="https://github.com/user-attachments/assets/f92b3026-5aea-42a7-a041-de10a5bc8495" />

## Server og tjenester
Jeg startet med å updatere filene mine og installere apache2/verifisere at jeg har apache2.
Kommandoer:
```
sudo apt update
sudo apt install apache2
sudo ufw app list
```

<img width="50%" height="50%" alt="Screenshot From 2025-09-17 09-08-20" src="https://github.com/user-attachments/assets/5502a4a3-b33a-4da2-acad-170b60933d86" />


Så oppdaterte jeg brannmuren til å tilate apache serveren.
Kommandoer:
```
sudo ufw allow Apache
```

<img width="50%" height="50%" alt="image" src="https://github.com/user-attachments/assets/7e41328b-dce9-4fbc-96c8-5666a7d1b4e0" />


Til slutt la jeg til min egen netside som apache skal kjøre og testet apache serveren med å få tilgang til nettsiden, med å skrive IPen 10.200.14.20 og få min nettside.
Kommandoer for å starte apache serveren:
```
sudo systemctl status apache2
sudo systemctl enable apache2
```
Kommandoer for å legge til nettsiden i apache, Username endres til maskin brukernavnet og nettside endres til nettside mappen, I mitt tillfelde er Username: alexsi og min nettsidemappe: TheTerminal_WebVersion_NoButtons_02:
```
cd .. #til du er ute av user og home directorien.
sudo mv ~/nettside/* /var/www/html/
cd /var/www/html
ls #til å sjekke om overføringen funket
sudo rm -r ~/nettside
```

<img width="1036" height="68" alt="image" src="https://github.com/user-attachments/assets/f68ed281-b005-4978-83ca-ddc3d66b68a8" />


<img width="50%" height="50%" alt="image" src="https://github.com/user-attachments/assets/a58d36c3-e4eb-4b83-9c3d-c15219a559f5" />

---
### Samba
Etter å få resultatet valgte jeg å laste ned samba.

<img width="50%" height="50%" alt="Screenshot From 2025-09-17 09-24-11" src="https://github.com/user-attachments/assets/9ad02424-cdb3-413a-ad38-78fc8ffdde8b" />


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
Så lagde jeg en python fil som skal vise system detaljer, som type system, version, cpu detaljer, uptime, etc.

Dette krevde at jeg lastet ned psutil på Rasberry Pien og Pcen 

<img width="50%" height="50%" alt="image" src="https://github.com/user-attachments/assets/05357697-1ce9-4abe-a0fc-a915806621bd" />

<img width="50%" height="50%" alt="Screenshot From 2025-09-17 10-58-14" src="https://github.com/user-attachments/assets/e02691d0-947d-49b0-a039-1f224d2ccd21" />

Så klonet jeg reposetorien til Rasberry Pien og testet at python filenfunket.

<img width="50%" height="50%" alt="Screenshot From 2025-09-17 11-12-01" src="https://github.com/user-attachments/assets/bc3e300c-afff-4585-aaf5-c87a0c627407" />


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
