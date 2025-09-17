# Nettverk og Tjenester - Oppdrag 1, 2IMI Uke 38 2025
## Nettverk og tilkobling
Først koblet jeg pcen og Rasberry Pien til klassens LAN nettverket med navn 2IMI - passord IMKuben1337!
Så ga jeg Rasberry Pien en statisk IP av 10.200.14.20, satt nettmask (subnet mask) til 255.0.0.0, gateway til 10.0.0.1 og DNS til 10.0.0.10
Etter det testet jeg å pinge Pien fra PCen 
<img width="862" height="371" alt="image" src="https://github.com/user-attachments/assets/f92b3026-5aea-42a7-a041-de10a5bc8495" />

## Server og tjenester
Jeg startet med å updatere filene mine og installere apace2/verifisere at jeg har apache2.
bilde

Så oppdaterte jeg brannmuren til å tilate apache serveren.
bilde

Til slutt la jeg til min egen netside som apache skal kjøre og testet apache serveren med å få tilgang til nettsiden, med å skrive IPen 10.200.14.20 og få min nettside.
<img width="1909" height="1058" alt="image" src="https://github.com/user-attachments/assets/a58d36c3-e4eb-4b83-9c3d-c15219a559f5" />

Etter å få resultatet valgte jeg å laste ned samba.

Får at folderen skal deles må jeg legge til: 

I konfigen
<img width="1844" height="484" alt="Screenshot From 2025-09-17 09-46-19" src="https://github.com/user-attachments/assets/b60e659f-9e25-4422-89f2-526ae2fd022b" />

Til slutt la jeg til en test fil og fikk sambashare folderen til å dele.
<img width="1154" height="861" alt="image" src="https://github.com/user-attachments/assets/17a9dac7-5394-435f-b951-b9edf6056b3d" />


## Python og github
Først lagde jeg en github og klonet den til pcen min.
Så lagde jeg en python fil som skal ...
Klonet den til Rasberry Pien og testet at den funket:
