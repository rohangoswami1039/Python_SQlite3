import pyrebase
firebaseConfig = {
    "apiKey": "AIzaSyDaeBhz84GujaFOnFwl5A3KGjzzITJZhIQ",
    "authDomain": "onlinelocker2-43a3b.firebaseapp.com",
    "databaseURL": "https://onlinelocker2-43a3b.firebaseio.com",
    "projectId": "onlinelocker2-43a3b",
    "storageBucket": "onlinelocker2-43a3b.appspot.com",
    "messagingSenderId": "1051418910693",
    "appId": "1:1051418910693:web:c188aa09b507de51a8d90c"}
firebase=pyrebase.initialize_app(firebaseConfig)
storage=firebase.storage()
fileupload=input("Enter the file name: ")

#file=input("Enter the file name on cloud: ")
image='images/'
#storage.child(image,file).put(fileupload)
storage.child(fileupload).download("","doload.jpg")
print("File uploaded")
