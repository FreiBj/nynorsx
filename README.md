# NynorsX

Et verktøy for å oversette **Hovedmål** til **Sidemål** ved bruk av Apertium i en Docker-container. 
For educational purposes.

## Fra 2 til 6 i sidemål

NynorsX bruker Apertiums Bokmål-til-Nynorsk språkpakke for å oversette Microsoft Word dokumenter. Applikasjonen kjører i en isolert Docker-container i bakgrunnen på pc'en, – som overvåker en spesifisert mappe for .docx filer og sender oversatte Nynorsk-filer til en annen bestemt mappe.

- Ingen GUI. Alt skjer i bakgrunnen og er omtrent umulig å ta som juks (ved mindre jeg er eksamensvakt).

**Språkbanken:**
- [Omsetjingsminne frå Nynorsk pressekontor 2022](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-80/)
- [Omsetjingsminne frå EFTA](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-71/)
- [Translation Memories from EFTA](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-71/)

**Requirements:**
- Python3
- Docker Desktop
- Nynorsk-motstand og dagdrømmer om nasjonalromantikken

---

![NynorsX Banner](https://github.com/user-attachments/assets/6d26b029-6813-428a-b447-0146aef2300e)

---

## ⚠️ Viktige merknader
- **Bilder, Grafer, og mer:** NynorsX støtter foreløpig ikke bilder, grafer eller annet ikke-tekstinnhold i filer.
- **Filnavn:** : Unngå mellomrom og spesialtegn i filnavn for å forhindre panikk 5 min før innleveringsfristen.
- **Oversettelseshastighet:** Oversettelseshastighet avhenger av filstørrelse, komplektistet, og hardware; større filer kan ta lengre tid.
- **Docker:** Sørg for at Docker Desktop fortsetter å kjøre mens du bruker NynorsX. Docker er kjent for å tømme laptop-batterier fortere enn du klarer å bøye ordet "gutt" på nynorsk, men jeg har ikke opplevd noen problemer med en Apple Silicon MacBook Pro.
- **Slett test filer**: Det er viktig å ha en mappe uten test filer på eksamensdagen. Dog, burde alle sørge for å teste programmet på forhånd.

---

## Installasjon

Steg for steg guide for å sette opp NynorsX på MacOS:

### 1. Installer Docker Desktop
- Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
- Ensure Docker Desktop is running during the entire process.

### 2. Last ned NynorsX
- Last ned prosjektfilene: [NynorsX ZIP](https://github.com/freibj/nynorsx/archive/refs/heads/main.zip).
- Pakk ut den nedlastede filen til `Downloads` mappen din.

### 3. Lage mappene og sette opp Docker Container
Kjør følgende kommandoer i terminalen din, én om gangen:

```shell
mkdir -p /Users/$USER/Documents/eksamensFiler/ferdigTekst
```
> Lager to mapper (`eksamensFiler` and `ferdigTekst`) som programmet overvåker _by default_.

```shell
cd /Users/$USER/Downloads/nynorsX-main
```
> Går inn i NynorsX kildekode mappen du lastet ned.

```shell
sudo docker build -t apertium --no-cache .
```
> Bygger _Docker image_ for å kjøre Apertium isolert uten GUI.

### 4. Start the Docker Container
```shell
docker run --name apertiumDockerContainer -t -d -v /Users/$USER/Documents/eksamensFiler:/src apertium
```
> Starter Docker kontaineren, og mounter `eksamensFiler` mappen inn i kontaineren.

### 5. Run the Python Script
```shell
python3 folderWatcherAperitumLocal.py
```
> Starter scriptet som overvåker filer og iverksetter oversettelse av filer.

---

## Bruke NynorsX

1. **WORD -> Save As**
   - Plasser en Nynorsk-tekstfil (f.eks. (e.g., `eksamen.docx`) i `~/Documents/eksamensFiler/`.
   - **Viktig:** Bruk filnavn uten mellomrom (f.eks. (e.g., `eksamen.docx`, ikke: `my exam.docx`).

2. **Vent på oversettelse:**
   - Skriptet oppdager filen og oversetter den til Bokmål.
   - Sjekk `~/Documents/eksamensFiler/ferdigTekst/`  for resultatet (f.eks. `eksamen59430.docx`).
   - Filen du legger inn i `eksamensFiler` mappen vil bli slettet, så sørg for at det ikke er originalen.

3. **Sjekk den oversatte teksten**
   - Åpne den oversatte filen i en teksteditor eller Word for å verifisere Bokmål-oversettelsen. Du må kanskje fjerne tegnet: `*`,som vil vises når en oversettelse er usikker.

### Eksempel
1. Flytt/Lagre en `test.docx` fil i `~/Documents/eksamensFiler/` med en tekst på Bokmål:
   ```
   Jeg liker å lese bøker.
   ```
2. Vent noen sekunder.
3. Sjekk `~/Documents/eksamensFiler/ferdigTekst/` for `test.doxc`:
   ```
   Eg likar å lese bøker.
   ```

---

## Feilsøking

| Issue | Løsning |
|-------|----------|
| Docker not running | Start Docker Desktop og verifiser med docker info. |
| Python script fails | Sørg for at Python3 er installert (`python3 --version`) og at skriptet er i riktig katalog. |
| No output file | Bekreft at data-inn er i `~/Documents/eksamensFiler/` og ikke inneholder mellomrom i filnavnet. |
| Container not starting | Sjekk container-status (`docker ps -a`) og logger (`docker logs apertiumDockerContainer`).). |

Trenger du hjelp?:
- Lag en issue på [GitHub](https://github.com/freibj/nynorsx/issues).
- Sjekk ut [Apertium Wiki](https://wiki.apertium.org/).
- Be om at Ivar Aasen ikke straffer deg for dine synder.

---

## Hvordan stoppe programmet?
1. Stopp Python scriptet: Trykk `Ctrl+C` i terminalen.
2. Stopp Docker kontaineren:
   ```shell
   docker stop apertiumDockerContainer
   ```
3. (Valgfritt) Slett kontaineren:
   ```shell
   docker rm apertiumDockerContainer
   ```

---

## Bli en del av _sidemålsmotstandarane_

Ønsker du å bidra? Fork [GitHub repository](https://github.com/freibj/nynorsx), gjør endringer, og submit en pull request. Forslag til funksjoner eller feilrettinger er velkomne!

![Ivar Aasen Portrait](https://private-user-images.githubusercontent.com/39388734/378102912-2f5a6ed1-a0e1-4939-9cdb-48993221e5e0.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDczNzc0MzUsIm5iZiI6MTc0NzM3NzEzNSwicGF0aCI6Ii8zOTM4ODczNC8zNzgxMDI5MTItMmY1YTZlZDEtYTBlMS00OTM5LTljZGItNDg5OTMyMjFlNWUwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTE2VDA2MzIxNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWMzNDllNDNiZGJiYWIyNjcyNDE4YzAzZmQxOTU4ZDI3YjZkNzMyZTU2MjI3M2I5NjI5NTA3NTMwNTI3MThmZjAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.FmGDklNnHkXAGh97iQw_beXVZUYCfa9GwZPhDi2DPS4)
