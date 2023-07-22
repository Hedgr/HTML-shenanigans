import neocities


true = True
false = False

mainKey = "11e8eaefafb7b3bf8cf5e2b967a481fe"
subKey = "7a7fea559ddb77954b585e5390512b9f"

nc = neocities.NeoCities(api_key=subKey)

mainProjectPath = "C:\\Users\\hedgr\\Downloads\\neocities main site\\"
altProjectPath = "C:\\Users\\hedgr\\Downloads\\neocities alt site\\"

def uploadTo(path, file):
    print("uploadTo()")
    nc.upload((path+file, file))

def uploadToMain(file):
    # function takes one file and uploads it from C:\Users\hedgr\Downloads\neocities main site\[file].[extension]
    print("uploadToMain()")
    uploadTo(mainProjectPath,file)

def uploadToAlt(file):
    print("uploadToAlt()")
    uploadTo(altProjectPath, file)

def mainUpdate(*toUpload):
    print("mainUpdate()")
    uploadToMain("index.html")
    uploadToMain("style.css")
    if len(toUpload) != 0:
        for i in range(len(toUpload)):
            uploadToMain(toUpload[i])

def altUpdate(*toUpload):
    print("altUpdate()")
    uploadToAlt("index.html")
    uploadToAlt("style.css")
    if len(toUpload) != 0:
        for i in range(len(toUpload)):
            uploadToAlt(toUpload[i])



altUpdate()
