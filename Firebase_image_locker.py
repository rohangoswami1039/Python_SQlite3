import pyrebase
import os
import sys 
from PIL import Image
firebaseConfig = {
    "Your Firebase config "
}
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
storage=firebase.storage()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

email=input(str("Enter your Email: ")))
password=input(str("Enter your Password: ")))
images=[]
compressed_images=[]


#image compresion and uplod functions
def compressed_images_name():
    for i in os.listdir("."):
        file_ext=os.path.splitext(i)[1]
        if file_ext=='.jpg' or file_ext=='.jpeg' or file_ext==".JPG" or file_ext==".JPEG":
            file_name=os.path.splitext(i)[0]
            global compressed_images
            compressed_images.append("Compressed_"+file_name+".JPG")
    return compressed_images


def image_name():
    for i in os.listdir("."):
        file_ext=os.path.splitext(i)[1]
        if file_ext=='.jpg' or file_ext=='.jpeg' or file_ext==".JPG" or file_ext==".JPEG":
            global images
            images.append(i)
    return images


def CLI_Image():
    def compressMe(file, verbose = False): 
                filepath = os.path.join(os.getcwd(),file) 
                picture = Image.open(filepath) 
                picture.save("Compressed_"+file,"JPEG",optimize = True,quality = 35) 
                return
    verbose = False 
    if (len(sys.argv)>1): 
        if (sys.argv[1].lower()=="-v"): 
            verbose = True
    cwd = os.getcwd() 
    formats = ('.jpg', '.jpeg') 
    for file in os.listdir(cwd): 
         if os.path.splitext(file)[1].lower() in formats: 
            print('compressing', file) 
            compressMe(file, verbose)
    
    print()
    print("Compression Done")
    print()



#firebase all setup and functions 


def login(email,password):
    #login 
    try:
        auth.sign_in_with_email_and_password(email,password)
        print("Login Sucess ")
        print("Do you want to upload compressed Images y/n ? ")
        print()
        ch=input("Enter your choice: ")
        if ch=='y'or ch=='Y':
            for i in image_name():
                global storage 
                print(i)
                folder=input("Enter the file name: ")
                try:
                    storage.child(i).put(folder)
                    print("Images Uploded...")
                except:
                    print("Can not upload the images.....Please try later ")
        elif ch=='n' or ch=='N':
            for i in compressed_images_name():
                
                folder=input("Enter the folder name: ")
                storage.child(folder).put(i)
                print("Images Uploded...")
        else :
            print("Wrong Choice....")
    except:
         print("Invalid user or password")

icon=""" 
\u001b[33m========================<><><><><><><><><><><><><><><><><><><><><><><><>========================
                                    \u001b[34m ONLINE LOCKER CLI 
\u001b[33m========================<><><><><><><><><><><><><><><><><><><><><><><><>========================
"""

#main menu
while True :
    print(icon)
    print()
    
    print("\u001b[32m 1. Login \u001b[37m")
    ch=int(input("Enter your choice: "))
    if ch==1 :
        os.system('cls')
        login(email,password)
    else :
        break
