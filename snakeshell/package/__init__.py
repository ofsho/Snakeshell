from snakeshell.package import Package

import os
from os import path
import platform
import distro

platforms = platform.system()
distroName = ''

if platforms == "Linux":
    distroName = distro.name()

prefrence = False
pkgpref = ""
pkgprefL = ""
version = ''

def PackagePrefrence(pref, over):
    global prefrence
    global pkgpref
    global pkgprefL
    pkgpref = pref
    pkgprefL = over
    prefrence = True

def PkgVersion(versions):
    global version                                                                  # todo : done
    version = versions

def ZypperInstall(package):
    if distroName == 'OpenSUSE':                                                    # todo test
        cmd = 'zypper install'
        cmd += package
        os.system(cmd)
    else:
        print('Zypper does not exist for your os')

def YumInstall(package):
    if distroName == 'Fedora':
        cmd = 'sudo yum install '
        cmd += package
        os.system(cmd)
    else:
        print('Yum is not available in your os')

def PipInstall(package):
    log = False                                                                         # todo : done
    if '!list' in package:
        package = package.replace('!list', '')
        os.system('pip list')
    if '!log' in package:
        package = package.replace('!log', '')
        log = True
    cmd = "pip install "
    cmd += package
    if log == True:
        cmd += ' --log '
        cmd += package
    os.system(cmd)

def NpmInstall(package):
    if '!config' in package:                                                        # todo test
        package = package.replace('!config ', '')
        cmd = 'npm config '
        cmd += package
    elif '!cache' in package:                                                       # todo : done
        package = package.replace('!cache ', '')
        if 'add' in package:
            package = package.replace('add ', '')
            cmd = 'npm cache add '
            cmd += package
        elif 'clean' in package:
            cmd = 'npm cache clean '
        else:
            cmd = 'npm cache verify'
    elif '!doctor' in package:                                                      # todo test
        package = package.replace('!doctor', '')
        cmd = 'npm doctor '
        cmd += package
    elif '!explore' in package:                                                     # todo : done
        package = package.replace('!explore', '')
        cmd = 'npm explore '
        cmd += package
    elif '!init' in package:                                                        # todo test
        cmd = 'npm init'
    elif '!ping' in package:                                                        # todo : done
        cmd = 'npm ping'
    elif '!list' in package:                                                        # todo : done
        cmd = 'npm list'
    elif '!start' in package:                                                       # todo test
        cmd = 'npm start'
    elif '!star' in package:                                                        # todo test
        os.system('npm whoami &> test.xs')
        with open('test.xs') as xs:
            if 'npm ERR! code ENEEDAUTH' in xs.read():
                os.system('npm login')
                package = package.replace('!star ', '')
                cmd = 'npm star '
                cmd += package
            else:
                package = package.replace('!star ', '')
                cmd = 'npm star '
                cmd += package
        os.system('rm test.xs')
    elif '!stars' in package:                                                       # todo FIX
        os.system('npm whoami &> test.xs')
        with open('test.xs') as xs:
            if 'npm ERR! code ENEEDAUTH' in xs.read():
                os.system('npm login')
                cmd = 'npm stars '
                cmd += package
            else:
                cmd = 'npm stars'
        os.system('rm test.xs')
    elif '!unstar' in package:                                                      # todo test
        os.system('npm whoami &> test.xs')
        with open('test.xs') as xs:
            if 'npm ERR! code ENEEDAUTH' in xs.read():
                os.system('npm login')
                package = package.replace('!unstar ', '')
                cmd = 'npm unstar '
                cmd += package
            else:
                package = package.replace('!unstar ', '')
                cmd = 'npm unstar '
                cmd += package
        os.system('rm test.xs')
    else:                                                                           # todo : done
        cmd = 'npm ls '
        cmd += package
        cmd += ' &> test.xs'
        os.system(cmd)
        with open('test.xs') as xs:
            if '(empty)' in xs.read():
                cmd = "npm install "
                cmd += package
                os.system(cmd)
                cmd = "npm link "
                cmd += package
            else:
                cmd = "npm update "
                cmd += package
    os.system(cmd)
    if '!root' in package:
        cmd2 = 'npm root'
        os.system(cmd2)

def PacmanInstall(package):
    if distroName == 'Arch':                                                         # todo test
        cmd = 'pacman install '
        cmd += package
        os.system(cmd)
    else:
        print('Pacman does not exist for your os')

def BrewInstall(package):
    if platforms == 'Darwin' or platforms == 'Linux':                               # todo : done
        if '!doctor' in package:
            package = package.replace('!doctor ', '')
            cmd = 'brew doctor '
            cmd += package
            os.system(cmd)
        else:
            cmd = 'brew ls '
            cmd += package
            cmd += ' &> test.xs'
            os.system(cmd)
            with open('test.xs') as xs:
                if 'Error: No such keg:' in xs.read():
                    cmd = "brew install "
                    cmd += package
                    os.system(cmd)
                    cmd = "brew link "
                    cmd += package
                    os.system(cmd)
                else:
                    print('PACKAGE EXISTS')
                    cmd = 'brew upgrade '
                    cmd += package
                    os.system(cmd)
            os.system('rm test.xs')
    else:
        print('Homebrew does not exist for your os')

def AptInstall(package):
    if distroName == 'Debian' or distroName == 'Ubuntu':                    # todo test
        cmd = "sudo apt install "
        cmd += package
        os.system(cmd)
    else:
        print('Apt does not exist for your os')

def AptGetInstall(package):
    if distroName == 'Debian' or distroName == 'Ubuntu':                    # todo test
        cmd = "sudo apt-get install "
        cmd += package
        os.system(cmd)
    else:
        print('AptGet does not exist for your os')

def PortInstall(package):
    if platforms == 'Darwin':                                               # todo : done
        cmd = "port install "
        cmd += package
        os.system(cmd)
    else:
        print('MacPorts does not exist for your os')

def CondaInstall(package):
    cmd = "conda install "                                              # todo : done
    cmd += package
    os.system(cmd)

def PkgInstall(package):
    if platforms == 'FreeBSD':                                           # todo test
        cmd = 'pkg install '
        cmd += package
        os.system(cmd)
    else:
        print('Pkg does not exist for your os')

def YarnInstall(package):
    cmd = "yarn add "                                                   # todo : done
    cmd += package
    os.system(cmd)
    cmd = "yarn link "
    cmd += package
    os.system(cmd)

def NugetInstall(package):
    cmd = "dotnet add package "                                         # todo : done
    cmd += package
    os.system(cmd)

def ChocolateyInstall(package):
    if platforms == 'Windows':                                      # todo test
        if 'cinst' in package:
            command = package.replace("cinst ", "")
            cmd = "cinst "
            cmd += command
            os.system(cmd)
        else:
            cmd = "choco install "
            cmd += package
            os.system(cmd)
    else:
        print('Chocolatey does not exist for your os')

def LuaRocksInstall(package):
    cmd = "luarocks install "                                           # todo : done
    cmd += package
    os.system(cmd)

def GemsInstall(package):
    cmd = "gem install "                                                # todo : done
    cmd += package
    os.system(cmd)

def Scoop(package):
    if platforms == 'Windows':                                      # todo test
        cmd = "scoop install "
        cmd += package
        os.system(cmd)
    else:
        print('Scoop does not exist for your os')

def PipInitPackage(name, author, version, license, author_email, url, download_url):
    cmd = "nvms Setup.py"