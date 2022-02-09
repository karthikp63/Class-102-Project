import cv2 
import dropbox 
import time 
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        result = False
    return image_name
    videoCaptureObject.realease()
    cv2.destroyAllWindows()

take_snapshot()

def upload_file(image_name)
    access_token = 'sl.AvahrjhkrgaAEhAGHmvnbeuruiaygrjhmbjnv.srghjn_uirgkhvmbrwkutig0io4gfyhrb4he2ngbiuya4bi7wyt9g'
    file = image_name
    file_from = file
    file_to = "/folder" + (image_name)
    
    with open(file_from, 'rb') as g:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite())
    
def main():
    while (True):
        if ((time.time() - start_time) >= 3):
            name = take_snapshot()
            upload_file(name)

main(   )