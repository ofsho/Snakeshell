import os
import platform
import distro

def GccCompile(file, fileout):
    cmd = 'gcc -o '
    cmd += file
    cmd += ' '
    cmd += fileout
    os.system(cmd)

def Gcc(command):
    cmd = 'gcc '
    cmd += command
    os.system(cmd)

def ClangCompile(file, fileout):
    cmd = 'clang '
    cmd += fileout
    cmd += file
    os.system(cmd)

def ClangConfig(command):
    cmd = 'clang '
    cmd += command
    os.system(cmd)

def ClangPlusPlusCompile(file, fileout):
    cmd = 'clang++ '
    cmd += fileout
    cmd += file
    os.system(cmd)

def ClangPlusPlusConfig(command):
    cmd = 'clang++ '
    cmd += command
    os.system(cmd)

def GPlusPlusCompile(file, fileout):
    cmd = 'g++ -o'
    cmd += file
    cmd += fileout
    os.system(cmd)

def GPlusPlus(command):
    cmd = 'g++ '
    cmd += command
    os.system(cmd)

def Ghc(file):
    cmd = 'ghc '
    cmd += file
    os.system(cmd)

def GhcConfig(command):
    cmd = 'ghc '
    cmd += command
    os.system(cmd)

def GoCompile(file):
    cmd = 'go tool compile '
    cmd += file
    os.system(cmd)

def GoCompileConfig(command):
    cmd = 'go tool compile '
    cmd += command
    os.system(cmd)

def GfortranConfig(command):
    cmd = 'gfortran '
    cmd += command
    os.system(cmd)

def Gfortran(file, fileout):
    cmd = 'gfortran -o '
    cmd += file
    cmd += ' '
    cmd += fileout
    os.system(cmd)

def mcs(file):
    cmd = 'mcs '
    cmd += file
    os.system(cmd)