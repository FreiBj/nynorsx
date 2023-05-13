# nynorsx

Nynorsk...

Aperitum i Docker med Nynorsk til Bokmål language pack.

https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-80/

---

## Requirements

-   Python versjon 3 (Python3)
-   Docker Desktop
-   Nynorsk motstand

# Installasjon

## 1 Installer Docker Desktop for Windows eller MacOS

https://www.docker.com/products/docker-desktop/
[https://docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).

Installer og start, Docker Dekstop applikasjonen må kjøre hele tiden dette programmet skal brukes.

## 2 I /dittnavn/Documents/

### Lag en mappe som heter 'eksamensFiler' og inni der lag en mappe som heter 'ferdigTekst'.

VELDIG VIKTIG MED STORE OG SMÅ BOKSTAVER og _IKKE PUNKTUM_. Kopier navnene så du er sikker på at det blir riktig.

#### Skal se sånn her ut

├── KariNormann/
│ ├── Documents/
│ │ ├── eksamensFiler/
│ │ │ ├── ferdigTekst/
│ │ │ │
│ │ │ │
│ │ │ │
│ │  
│ ├── Movies/
│ ├── Images/
│ ├── Applications/
│ ├── Music/

## 3 Kjør følgende kommando med admin rettigheter

### MacOS i terminal.app

`sudo docker build -t apertium --no-cache .`

### Windows - FUNKER IKKE ENDA

Åpne terminal som administrator i den nedlastede mappen
`docker build -t apertium --no-cache .`

# 4 Start Docker containeren

`docker run --name apertiumDockerContainer -t -v /Users/frei/Documents/watchedFolder:/src apertium`

## 5 Kjør python programmet med Python3

### Like this

`python3 folderWatcherAperitumLocal.py`

---

### - 🐻‍❄️ Isbjørnen
