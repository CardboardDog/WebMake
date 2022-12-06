import requests
import os
import urllib.request as rq
import json as JSON
import zipfile
def BuildWindows(htmlloc,outloc,outname):
    #electron url
    zippedfile = "https://github.com/electron/electron/releases/download/v21.3.3/electron-v21.3.3-win32-x64.zip"

    #make project directory
    try:
        os.mkdir(outloc+outname)
        print("created - ./project")
    except:
        print("skipped - make ./project")
        pass

    #make scaffolding directory
    try:
        os.mkdir(outloc+outname+"/scaffolding")
        print("created - ./"+outname+"scaffolding")
    except:
        print("skipped - make ./"+outname+"/scaffolding")
        pass

    #make build directory
    try:
        os.mkdir(outloc+outname+"/build")
        print("created - ./"+outname+"/build")
    except:
        print("skipped - make ./"+outname+"/build")
        pass

    #download perbuild binary
    try:
    
        rq.urlretrieve(zippedfile,outloc+outname+"/scaffolding/electron.zip")
        print("downloaded - electron.zip")
        zippath = outloc+outname+"/scaffolding/electron.zip"
    except:
        print("failed - retrieve electron.zip")
        return -1

    #load build settings
    try:
        settings = open(htmlloc+"/build.json","r")
        settings = JSON.load(settings)
        print("opened - build.json")
    except:
        print("failed - cannot open build.zip")
        return -1

    #check zip data
    if zipfile.is_zipfile(zippath) == True:
        pass
    else:
        print("failed - zip is incorrect")
        return -1

    #extract zip contents
    try:
        zipdata = zipfile.ZipFile(outloc+outname+"/scaffolding/electron.zip")
        zipdata.extractall(outloc+outname+"/build/"+outname)
        builddir = outloc+outname+"/build/"+outname
        zipdata.close()
        print("extracted - electron.zip")
    except:
        print("failed - cannot extract zip")
        return -1

    #create app folder
    try:
        os.mkdir(outloc+outname+"/build/"+outname+"/resources/app")
        print("created - ./"+outname+"/build/"+outname+"/resources/app")
    except:
        print("skiped - ./"+outname+"/build/"+outname+"/resources/app")

    #complete
    return 1