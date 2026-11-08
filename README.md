# Secret Diary: Week 5 Encryptie

Link naar de repo: https://github.com/Taha-1088007/Week-5-Encryptie

## 1.Hoe werkt de applicatie?

De applicatie is een command-line dagboek in Python. Elk bericht wordt met Fernet versleuteld voordat het wordt opgeslagen in diary.enc. Tijdens het lezen wordt deze weer ontsleuteld. Zonder het juiste wachtwoord wordt het dagboek niet gelezen.  

Bij de opstarten van de applicatie vraagt de applicatie voor een wachtwoord. Het wachtwoord wordt ingevoerd met getpass, dus je ziet het wachtwoord niet. Bij de eerste keer, als er nog geen diary.enc is, dan type je het wachtwoord twee keer, zodat een typfout het dagboek niet op slot zet.
Als de wachtwoord fout is dan krijg je een foutmelding te zien en sluit het af.

<br>

**Opties in het menu**
1. Schrijf een bericht (Het dagboek wordt ontsleuteld. Een leeg bericht wordt niet opgeslagen.)
2. Lees het dagboek (Het dagboek wordt ontsleuteld en getoond. Is het dagboek nog leeg, dan staat er "is empty".)
3. Zoek in het dagboek (Hierin kun je een zoekwoord in typen en de applicatie toont alle regels waarin het voorkomt.)
4. wachtwoord wijzigen (Hier wijzig je het wachtwoord, dit doe je twee keer. Het dagboek wordt ontsleuteld met het oude wachtwoord en opnieuw versleuteld met het nieuwe.)
5. Verlaten (De applicatie sluit af)

<br>

**Wat er gebeurt bij het opslaan?** 

Het dagboek wordt als één tekst versleuteld en opgeslagen in diary.enc. Dit is wat er gebeurt: 
1. Er wordt een nieuwe salt van 16 bytes gemaakt met os.urandom
2. Uit mijn wachtwoord en de salt wordt met PBKDF2 een sleutel gemaakt.
3. Fernet versleutelt de tekst met de sleutel

<br>

**Foutafhandeling** <br>

De applicatie vangt: 
- Een leeg wachtwoord
- twee wachtwoorden die niet overeenkomen
- Een verkeerd wachtwoord
- Een leeg bericht
- Een leeg zoekwoord
- Een ongeldige menu

<br>

**Installeren en starten (in de terminal)**

```1. python3 -m venv .venv```

```2. source .venv/bin/activate```

```3. pip install -r requirements.txt```

```4. python3 diary.py```

<br>

**Opbouw van de code:** 

| Bestand | Taak | 
| --- | ---|
| encryption.py | Cryptografie: sleutel maken, versleutelen, ontsleutelen | 
| storage.py | Het versleutelde bestand lezen en opslaan | 
| diary.py | Het menu en de functies(schrijven,lezen, zoeken, wachtwoord wijzigen)

<br>

## 2. Onderzoek: Symmetrisch en asymmetrisch 

**Symmetrisch:**
Dezelfde sleutel wordt gebruikt voor versleutelen en ontsleutelen. Dit is snel, maar moet geheim blijven. 

**Asymmetrisch:** 
Gebruikt een publieke of een private sleutel om te ontsleutelen, maar maakt het makkelijker om sleutels veilig uit te wisselen. Het is ook trager

**Mijn keuze:**
Ik kies voor Symmetrische encryptie, omdat ik alleen het dagboek lees. Er is geen sleutelwisseling met anderen nodig.

<br>

## 3. Algoritme en rechtvaardiging
Ik gebruik Fernet uit de library (Python) Cryptography. Fernet gebruikt AES-128 voor encryptie en HMAC-SHA256 om te controleren of gegevens zijn aangepast.

Waarom deze keuze? 
- Fernet controleert of de gegevens zijn aangepast.
- Het is lastig om er fouten mee te maken.
- AES wordt ook wereldwijd gebruikt.

<br>

## 4. Sleutelbeheer
Voor het sleutelbeheer maak ik gebruik van PBKDF2 met 600.000 Iterations en ook een salt van 16 bytes. De salt bewaar ik samen met de versleutelde bestand. Het zorgt ervoor dat een wachtwoord niet steeds dezelfde sleutel geeft.

Het wachtwoord wordt nergens opgeslagen. Als ik het wachtwoord vergeet dan zijn de berichten van de dagboek voorgoed kwijt, want er is geen reserveknop. Verder zorgt het ervoor dat diary.enc niet in Github komt te staan door het in de gitignore te zetten.

<br>

## 5. Reflectie 
Kerckhoffs's Principle zegt dat een systeem veilig moet zijn, ook als iedereen weet hoe de software werkt, behalve de sleutel. Bij mijn applicatie is dat ook zo. De code is openbaar, het enige is dat mijn wachtwoord niet wordt gedeeld met anderen. 
Ik vind dit wel een goede manier, omdat het programma niet wordt beschermd door de code geheim te houden, want dat werkt niet vaak. Het is slimmer om sterke standaarden te gebruiken. 

Dit principe heeft wel een nadeel, alles hangt af van de sleutel. In mijn geval is dat het wachtwoord, en het is minder sterk dan een willekeurige sleutel. Als iemand diary.enc bestand in hand krijgt, dan kan diegene net zo lang mogelijk wachtwoord proberen tot het goed is. 
<br>

## 6. Bronnen

- Fernet (symmetric encryption) — Cryptography 51.0.0-dev1 documentation. (z.d.). https://cryptography.io/en/latest/fernet/

- Wikipedia-bijdragers. (2024, 20 juli). Principe van Kerckhoffs - Wikipedia. https://nl.wikipedia.org/wiki/Principe_van_Kerckhoffs

- Password Storage - OWASP Cheat Sheet Series. (z.d.). https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html

- GeeksforGeeks. (2026, 18 augustus). Symmetric vs Asymmetric Key Encryption. GeeksforGeeks. https://www.geeksforgeeks.org/computer-networks/difference-between-symmetric-and-asymmetric-key-encryption/

- Turtle Code. (2025, 13 november). Python Encryption Tutorial: How to Encrypt & Decrypt Data with cryptography Fernet [Video]. Youtube. https://www.youtube.com/watch?v=es_5TMQc-Bk

- getpass — Portable password input. (z.d.-b). Python Documentation. https://docs.python.org/3.13/library/getpass.html
  
- os — Miscellaneous operating system interfaces. (z.d.). Python Documentation. https://docs.python.org/3.13/library/os.html
