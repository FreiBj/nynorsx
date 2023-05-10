import os, time, requests, glob, random
def deleteFiles():
    files = glob.glob('/Users/frei/Documents/watchedFolder/*')
    for f in files:
        os.remove(f)

WATCHED_FOLDER = '/Users/frei/Documents/watchedFolder/'
EXPORTED_FOLDER = '/Users/frei/Documents/'

env_userName = os.environ['USER']

def watch_folder():
    while True:
        time.sleep(1) # 10 seconds
        for file_name in os.listdir(WATCHED_FOLDER):
            file_path = os.path.join(WATCHED_FOLDER, file_name)
            time.sleep(1) # 5 seconds
            if os.path.isfile(file_path) and (file_path.endswith('.docx')):
                integer = str(random.randint(1,5**25))
                print(f"docker run -v /Users/{env_userName}/Documents/apertiumDockerVolume/ apertium -f docx nob-nno_e {WATCHED_FOLDER+file_name} {EXPORTED_FOLDER+'Nynorsk'+integer+'.docx'}")
                try:
                    os.system(f"docker run -v /Users/{env_userName}/Documents/watchedFolder:/Users/{env_userName}/Documents/watchedFolder apertium -f docx nob-nno_e {WATCHED_FOLDER+file_name} {EXPORTED_FOLDER+'Nynorsk'+integer+'.docx'}")
                except:
                    print("An error occured with writing file") # An error occured

                print(f"File: {file_name} found")
                deleteFiles()


if __name__ == '__main__':
    deleteFiles()
    watch_folder()
