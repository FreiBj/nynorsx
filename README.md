# nynorsx

Nynorsk eksamen...

Aperitum i Docker med Nynorsk til Bokmål language pack.

→ https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-80/
→ https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-71/
→ https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-71/

**Requirements:**
- Python versjon 3 (Python3)
- Docker Desktop
- Nynorsk motstand
---
![NynorsX](https://github.com/user-attachments/assets/6d26b029-6813-428a-b447-0146aef2300e)

## Installasjon

1. #### Installer _Docker Desktop_
   Installer og start, Docker Dekstop applikasjonen **må kjøre hele tiden** dette programmet skal brukes.
   https://www.docker.com/products/docker-desktop/
<br/>

2. #### Last ned filene og unzip i "Downloads"
    [Klikk her for å laste ned](https://github.com/freibj/nynorsx/archive/refs/heads/main.zip)
<br/>

3. #### Kjør følgende i Terminal, en av gangen.
   ```shell
   mkdir -r /Users/$User/Documents/eksamensFiler/ferdigTekst
   ```
   > Oppretter 2 mapper som programmet overvåker.
   <br/>
   
   ```shell
   cd /Users/$USER/Downloads/nynorsX-main
   ```
   > Navigerer inn i _NynorskX_ kildekoden.
   <br/>
   
   ```shell
   sudo docker build -t apertium --no-cache .
   ```
   > Bygger applikasjonen lokalt.
   <br/>

4. #### Start Docker Containeren
   ```shell
   docker run --name apertiumDockerContainer -t -d -v /Users/$USER/Documents/watchedFolder:/src apertium
   ```
<br/>

5. #### Kjør python programmet med Python3
    ```shell
    python3 folderWatcherAperitumLocal.py
    ```
<br/>

## Hvordan oversetter jeg?

Lagre filen din i `eksamensFiler/` mappen, IKKE bruk mellomrom i filnavnet grunnet at programmet da vil crashe og du vil bli mer stressa enn når du fikk vite at du  ble trukket opp til denne skiten. Vent noen sekunder til programmet spytter ut den oversatte filen i `ferdigTekst/` mappen.

### VIKTIG!
- Apertium takler IKKE **grafer og bilder** når den genererer Word dokumenter, så sørg for at det kun er tekst i filen du kjører gjennom programmet.
