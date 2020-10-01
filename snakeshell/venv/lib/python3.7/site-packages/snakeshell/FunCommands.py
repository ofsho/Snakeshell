import os
import sys
import mmap

platform = sys.platform

exists = True

def cmatrix():
    if platform == 'darwin' or platform == 'linux':
        if platform == 'darwin':                                        # todo : done
            os.system('brew ls cmatrix &> test.xs')
            with open('test.xs') as xs:
                if 'Error: No such keg:' in xs.read():
                    exists = False
                else:
                    exists = True
            os.system('rm test.xs')
            if exists == False:
                os.system('brew install cmatrix')
            else:
                os.system('cmatrix')
        if platform == 'linux':                                         # todo
            os.system('dpkg -s cmatrix &> test.xs')
            with open('test.xs') as xs:
                if 'error' in xs.read() or 'Error' in xs.read():
                    exists = False
                else:
                    exists = True
            os.system('rm test.xs')
            if exists == False:
                os.system('sudo apt-get install cmatrix')
            else:
                os.system('cmatrix')                                  # todo end
    else:
        print('ERR: NOT COMPATABLE')