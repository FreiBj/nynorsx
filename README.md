# nynorsx

Nynorsk eksamen...

Aperitum i Docker med Nynorsk til Bokmål language pack.

→ https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-80/

**Requirements:**
- Python versjon 3 (Python3)
- Docker Desktop
- Nynorsk motstand
---
## Installasjon

1. **Installer Docker Desktop**
   Installer og start, Docker Dekstop applikasjonen **må kjøre hele tiden** dette programmet skal brukes.
    https://www.docker.com/products/docker-desktop/
3. **I /dittNavn/Documents/**

    Lag en mappe som heter *eksamensFiler* og inni der lag en mappe som heter *ferdigTekst*
     > VELDIG VIKTIG MED STORE OG SMÅ BOKSTAVER og _IKKE PUNKTUM_. Kopier navnene så du er sikker på at det blir riktig.

    Det skal se lik ut:
    ```markdown
    ├── KariNormann
    │   ├── Documents
    │   └── eksamensFiler
    │       └── ferdigTekst
    ├── Movies
    ├── Images
    ├── Applications
    └── Music
    ```

4. **Kjør følgende kommandoer med admin rettigheter**

    Åpne Terminal som administrator i den nedlastede mappen og kjør følgende:

    ```shell
    sudo docker build -t apertium --no-cache .
    ```
    > Windows - FUNKER IKKE ENDA

5. **Start Docker containeren**

    ```shell
    docker run --name apertiumDockerContainer -t -v /Users/frei/Documents/eksamensFiler:/src apertium
    ```

6. **Kjør python programmet med Python3**

    ```shell
    python3 folderWatcherAperitumLocal.py
    ```

