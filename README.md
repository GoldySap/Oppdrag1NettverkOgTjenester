# Nettverk og Tjenester - Oppdrag 1, 2IMI Uke 38 2025
## Nettverk og tilkobling
Først koblet jeg pcen og Rasberry Pien til klassens LAN nettverket med navn 2IMI - passord IMKuben1337!
Så ga jeg Rasberry Pien en statisk IP av 10.200.14.20, satt nettmask (subnet mask) til 255.0.0.0, gateway til 10.0.0.1 og DNS til 10.0.0.10
Etter det testet jeg å pinge Pien fra PCen 
<img width="862" height="371" alt="image" src="https://github.com/user-attachments/assets/f92b3026-5aea-42a7-a041-de10a5bc8495" />

## Server og tjenester
Jeg startet med å installere og verifisere at jeg har fillene som apache2.
bilde

Så oppdaterte jeg brannmuren til å tilate apache serveren
bilde

Til slutt testet jeg serveren med å prøve å få tilgang til en enkel nettside.
bilde

## Python og github
Først lagde jeg en github og klonet den til pcen min.
Så lagde jeg en python fil som skal ...
