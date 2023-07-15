import os
import glob
import qrcode
import time
from tqdm import tqdm
import fitz
from firebase_admin import credentials, initialize_app, storage

##################################################################

def get_filepaths(directory):


    file_paths = []  

    
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  





###################################################################

cred = credentials.Certificate("rec/yur_auth_json_file")
initialize_app(cred, {'storageBucket': 'base-c5b39.appspot.com'})

def upload_on_cloud(file,auth=1):
    
    # auth -- authentacation
    
    # auth 0 -> make it private
    # auth 1 -> make it private default

    fileName = file
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    blob.make_public()
      

    return blob.public_url


##########################################################################

def text2qr(txt):
        
        qr = qrcode.make(txt)
        txt = txt.replace(".","$")
        txt = txt.replace("/","$")
        qr.save(f"qr/{txt}.png")
        return f"qr/{txt}.png"

        
##########################################################################

print("""
                                  _                    
   __ _  ___ _ __   ___ _ __ __ _| |_ ___    __ _ _ __ 
  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \  / _` | '__|
 | (_| |  __/ | | |  __/ | | (_| | ||  __/ | (_| | |   
  \__, |\___|_| |_|\___|_|  \__,_|\__\___|  \__, |_|   
  |___/                                        |_|
  """)

h = ("""
welcome!!

this tool will help you to store any kind of document in cloud storage..

follow these steps..
1 -> place file(s) in pdf folder
2 -> select mode
     0 -> for manual mode
     1 -> for automatic mode
3 -> generated pdf will get stored in result/pdf
4 -> and you will fing QR in qr folder..
     
     """)

print("""press r to run
press h for help.
press e to exit
""")


while True:
    opt = input("Enter option $> ")
    print()
    try:

        if opt == "h":
            print(h)
            
        if opt == "e":
            break

        if opt == "r":
            print("press 1 for manual mode and 0 for automatic mode.")
            

            mode = int(input("Enter mode $> "))
            print()
            
            if mode == 1:
                print("file should be present inside pdf folder.")
                f_name = input("enter file name :: ")
                
                #processing...
                
                link = upload_on_cloud(f"pdf/{f_name}")
                text2qr(link)
                print("suc!!")
                
            else:
                
                f_list = get_filepaths("pdf")
                print("no of files :: ",len(f_list))

                

                with tqdm(total= len(f_list), desc="processing ", bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:
                    
                    for i in f_list:
                        src_pdf_filename = i
                        dst_pdf_filename = f"result/{i}"
                        

                        img_rect = fitz.Rect(0, 0, 60, 60)
                        document = fitz.open(src_pdf_filename)

                        page = document[0]
                                                
                        link = upload_on_cloud(i)
                        img = text2qr(link)
                        page.insert_image(img_rect, filename=img)
                        document.save(dst_pdf_filename)
                        document.close()
                        pbar.update(1)
          

    except:
        print("""
opps!! somthing went wrong...
check internet connection/input... 
""")

                
                
            
            

























    
