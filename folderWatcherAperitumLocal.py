import os, time, glob, random

# Finner Brukernavnet til programmets bruker
env_userName = os.environ['USER']

# HOST COMPUTER PATHS
WATCHED_FOLDER = f"/Users/{env_userName}/Documents/eksamensFiler/"
EXPORTED_FOLDER = f'/Users/{env_userName}/Document/eksamensFiler/ferdigTekst/'

# Sletter alle filer i mappen "eksamensFiler", men sletter ikke mappene. For å unngå masse forskjellige tekster som ligger igjen fra forrige gang.
def deleteFiles():
    files = glob.glob(f"/Users/{env_userName}/Documents/eksamensFiler/*.*")
    for f in files:
        os.remove(f)

# Disse er irrelevante for andre enn utviklerene til dette programmet. Eller vågale nynorsk-motstandere!
dockerWatchedFolder = '/src/'
dockerExportedFolder = '/src/ferdigTekst/'

def watch_folder():
    while True:
        time.sleep(1) # 10 seconds
        for file_name in os.listdir(WATCHED_FOLDER):
            file_path = os.path.join(WATCHED_FOLDER, file_name)
            time.sleep(1) # 5 seconds
            if os.path.isfile(file_path) and (file_path.endswith('.docx')):
                randomInteger = str(random.randint(1,5**25))
                try:
                    os.system(f"docker exec apertiumDockerContainer apertium -f docx nob-nno {dockerWatchedFolder+file_name} {dockerExportedFolder+'Nynorsk-eksamen.docx'}")
                except:
                    print("An error occured with writing file") # An error occured

                print(f"success")
                deleteFiles()


if __name__ == '__main__':
    deleteFiles()
    watch_folder()
