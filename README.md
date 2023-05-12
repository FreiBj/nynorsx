# nynorsx

Nynorsk...

Aperitum i Docker med Nynorsk til Bokmål language pack.

---

# 1.0 - Installer Docker Desktop for Windows eller MacOS

https://www.docker.com/products/docker-desktop/

# 2 Lag en mappe som heter 'watchedFolder' og inni der lag en mappe som heter 'exported'.

VELDIG VIKTIG MED STORE OG SMÅ BOKSTAVER. Kopier navnene så du er sikker på at det blir riktig.

# 3 - Kjør følgende kommando med admin rettigheter

## MacOS

`sudo docker build -t apertium --no-cache .`

## Windows

Åpne terminal som administrator i den nedlastede mappen
`docker build -t apertium --no-cache .`

# 4 Start Docker containeren

`docker run --name apertiumDockerContainer -t -v /Users/frei/Documents/watchedFolder:/src apertium`

# 5 Kjør python programmet

## Med Python3

`python3 folderWatcherAperitumLocal.py`
