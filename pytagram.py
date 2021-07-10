import instaloader
from instaloader import Post


class PyTagram:
    def __init__(self):
        self.pyTagram = instaloader.Instaloader()
        #self.logIn()
    
    #login 
    def logIn(self):

        print("--- LOGIN ---")
        print("Dont forget disable the 2FA!!")

        userNickname = str(input("username : "))
        userPassword = str(input("password :"))

        self.pyTagram.login(userNickname, userPassword)

    #procces menu
    def proccesMenu(self):
        print("--- PyTagram ---")
        print("Downlaod Profile Pictures : 1")
        print("Exit : 0")

        userInput = int(input("Procces : "))

        if userInput == 0:
            exit(0)

        if userInput == 1:
            self.downloadProfilePicture()

    #download the profile pictures
    def downloadProfilePicture(self):
        targetNickName = str(input("nickname : ")) 
        
        print("[DOWNLOAD] - Started")

        try:
            downloadProcces = self.pyTagram.download_profile(targetNickName, profile_pic_only=True)

        except Exception as DownlaodError:
            print("[DOWNLOAD] - Failed")

        else:
            print("[DOWNLAOAD] - Succesfull")

    

#main
#||-------------------------------------------------||
_pyTagram = PyTagram()
while True:
    _pyTagram.proccesMenu()


#TO DO 
# Append Downloading Posts and Stories 
# Append 