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

def Curl(url):                                                      # todo : done
    cmd = "curl "
    cmd += url
    os.system(cmd)

def Wget(url):
    cmd = "wget "
    cmd += url
    os.system(cmd)



def InstallManager(name):
    # darwin
    if platforms == 'Darwin':
        # npm
        if name == 'npm':                                                           # todo : done
            if path.exists('/usr/local/bin/npm') == True:
                os.system('brew upgrade nodejs')
            else:
                if prefrence == True:
                    if pkgpref == 'port':
                        cmd = "port install nodejs"
                        cmd += version
                        os.system(cmd)
                    elif pkgpref == 'brew' or pkgpref == 'homebrew':
                        os.system('brew install nodejs')
                else:
                    os.system('brew install nodejs')
        elif name == 'brew' or name == 'homebrew':                                          # todo done
            if path.exists('/usr/local/bin/brew') == True:
                os.system('echo \'Homebrew is already installed!\'')
            else:
                os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"')

    # windows
    elif platforms == 'Windows':
        # npm
        if name == 'npm':                                                          # todo : test
            if prefrence == True:
                if pkgpref == 'scoop':
                    os.system('scoop install nodejs')
                elif pkgpref == 'choco' or pkgpref == 'chocolatey':
                    os.system('cinst nodejs.install')
            else:
                os.system('cinst nodejs.install')

    # linux
    elif platforms == 'Linux':
        if distroName == 'Ubuntu':                                                          # todo : test
            # npm
            if name == 'npm':
                os.system('curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -')
                os.system('sudo apt-get install -y nodejs')
            if name == 'brew' or name == 'homebrew':                                          # todo : test
                os.system('sudo apt-get install build-essential curl file git')
        elif distroName == 'Debian':                                                          # todo : test
            if name == 'npm':
                os.system('curl -sL https://deb.nodesource.com/setup_14.x | bash -')
                os.system('apt-get install -y nodejs')
            if name == 'brew' or name == 'homebrew':                                          # todo : test
                os.system('sudo apt-get install build-essential curl file git')
        elif distroName == 'Fedora':                                                          # todo : test
            if name == 'npm':
                os.system('curl -sL https://rpm.nodesource.com/setup_14.x | bash -')
            if name == 'brew' or name == 'homebrew':                                          # todo : test
                os.system('sudo yum groupinstall \'Development Tools\'')
                os.system('sudo yum install curl file git')
                os.system('sudo yum install libxcrypt-compat # needed by Fedora 30 and up')
        elif distroName == 'OpenSUSE':                                                        # todo : test
            if name == 'npm':
                os.system('zypper install nodejs4')
        elif distroName == 'Arch':
            if name == 'npm':
                os.system('pacman -S nodejs npm')
        else:
            print('distro not supported')

    # freebsd
    elif platforms == 'FreeBSD':
        if name == 'npm':                                                                    # todo : test
            os.system('pkg install node')

    # other
    else:
        print('Your OS is not supported with this library')