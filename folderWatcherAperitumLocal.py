import os, time, requests, glob, random
def deleteFiles():
    files = glob.glob('/Users/frei/Documents/watchedFolder/*.*')
    for f in files:
        os.remove(f)

WATCHED_FOLDER = '/Users/frei/Documents/watchedFolder/'
EXPORTED_FOLDER = '/Users/frei/Document/watchedFolder/exported/'

# Disse er irrelevante for andre enn utviklerene til dette programmet.
dockerWatchedFolder = '/src/'
dockerExportedFolder = '/src/exported/'

# Finner Brukernavnet til programmets bruker
env_userName = os.environ['USER']

def watch_folder():
    while True:
        time.sleep(1) # 10 seconds
        for file_name in os.listdir(WATCHED_FOLDER):
            file_path = os.path.join(WATCHED_FOLDER, file_name)
            time.sleep(1) # 5 seconds
            if os.path.isfile(file_path) and (file_path.endswith('.docx')):
                randomInteger = str(random.randint(1,5**25))
                try:
                    os.system(f"docker exec apertiumDockerContainer apertium -f docx nob-nno_e {dockerWatchedFolder+file_name} {dockerExportedFolder+'Nynorsk'+randomInteger+'.docx'}")
                except:
                    print("An error occured with writing file") # An error occured

                print(f"File: {file_name} found")
                deleteFiles()


if __name__ == '__main__':
    deleteFiles()
    watch_folder()
