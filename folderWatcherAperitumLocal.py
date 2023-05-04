import os, time, requests, glob, random
def deleteFiles():
    files = glob.glob('/Users/frei/Documents/watchedFolder/*')
    for f in files:
        os.remove(f)

WATCHED_FOLDER = '/Users/frei/Documents/watchedFolder/'
EXPORTED_FOLDER = '/Users/frei/Documents/'

def watch_folder():
    while True:
        time.sleep(10)
        for file_name in os.listdir(WATCHED_FOLDER):
            file_path = os.path.join(WATCHED_FOLDER, file_name)
            time.sleep(5)
            if os.path.isfile(file_path) and (file_path.endswith('.docx')):
                integer = str(random.randint(1,5**25))
                os.system(f"apertium -f docx nob-nno_e {WATCHED_FOLDER+file_name} {EXPORTED_FOLDER+'Nynorsk'+integer+'.docx'}")
                print(f"File: {file_name} found")
                deleteFiles()


if __name__ == '__main__':
    deleteFiles()
    watch_folder()
