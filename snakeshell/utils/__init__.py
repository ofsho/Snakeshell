from snakeshell.utils import FunCommands
import os
import sys

platform = sys.platform

exists = True

def nvms(filename):
    if platform == "darwin" or platform == "linux":          # todo check on linux
        cmd = "touch "
        cmd += filename
        os.system(cmd)
    elif platform == "windows":
        cmd = "echo $null > "
        cmd += filename
        os.system(cmd)

def newfile(filename):
    if platform == "darwin" or platform == "linux":          # todo check on linux
        cmd = "touch "
        cmd += filename
        os.system(cmd)
    elif platform == "windows":
        cmd = "echo $null > "
        cmd += filename
        os.system(cmd)

def touch(filename):
    if platform == "darwin" or platform == "linux":          # todo check on linux
        cmd = "touch "
        cmd += filename
        os.system(cmd)
    elif platform == "windows":
        cmd = "echo $null > "
        cmd += filename
        os.system(cmd)

def systemInfo():
    if platform == "linux":                                     # todo check
        os.system('uname -r')
    elif platform == "darwin":                                  # todo : done
        os.system("sw_vers")
    elif platform == "windows":                                 # todo check
        os.system("systeminfo")

def openApp(app):
    if platform == "darwin":                                    # todo : done
        os.system('cd /Applications')
        cmd = "open "
        cmd += app
        os.system(cmd)
    else:
        print()                                                # todo: now!

def PypiExists(packagename):
    