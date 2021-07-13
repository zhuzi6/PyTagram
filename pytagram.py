import instaloader
from instaloader import Post


class PyTagram:

    def __init__(self):
        self.downloadProcces = True
        self.pyTagram = instaloader.Instaloader()
    
    #login 
    def logIn(self):

        print("--- LOGIN ---")
        
        userNickname = str(input("username : "))
        userPassword = str(input("password :"))

        self.pyTagram.login(userNickname, userPassword)

    #procces menu
    def proccesMenu(self):
        print("--- PyTagram ---")
        print("Downlaod Profile Pictures : 1")
        print("Download Saved Posts :      2")
        print("Download Post :             3")
        print("Exit :                      0")

        userInput = int(input("Procces : "))

        if userInput == 0:
            exit(0)

        if userInput == 1:
            self.downloadProfilePicture()

        if userInput == 2:
            self.downloadSavedPosts()
        
        if userInput == 3:
            self.downloadPost()

    #download the profile pictures
    def downloadProfilePicture(self):
        
        targetNickName = str(input("nickname : ")) 
        
        print("[DOWNLOAD] - Started")

        try:
            self.downloadProcces = self.pyTagram.download_profile(targetNickName, profile_pic_only=True)

        except Exception as DownlaodError:
            print("[DOWNLOAD] - Failed")

        else:
            print("[DOWNLAOAD] - Succesfull")

    def downloadSavedPosts(self):
        try:
            self.downloadProcces = self.pyTagram.download_saved_posts()
        
        except Exception as DownlaodError:
            print("[DOWNLOAD] - Failed")

        else:
            print("[DOWNLAOAD] - Succesfull")

    def downloadPost(self):

        targetUserNickName = str(input("nickname : "))
        targetPostShortCode = str(input("shortcode : "))

        try:
            self.downloadProcces = self.pyTagram.download_post(targetPostShortCode, targetUserNickName)

        except instaloader.PrivateProfileNotFollowedException or instaloader.ProfileNotExistsException as DownloadException:
            print(f"[DOWNLOAD] - Failed | Target profile not found or not following")

         
#main
#||-------------------------------------------------||
_pyTagram = PyTagram()
_pyTagram.logIn()
while True:
    _pyTagram.proccesMenu()

