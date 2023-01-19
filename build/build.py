from subprocess import PIPE, Popen
from os import getcwd, path, pardir
from shutil import rmtree as rmdir
from os import remove as rmfile
from zipfile import ZipFile

if __name__ == '__main__':
    VERSION = '2.1'
    NAME = 'BrightnessControl'
    ROOT = path.abspath(path.join(getcwd(), pardir))
    MAIN = f'{ROOT}\\main.py'
    BUILD = f'{ROOT}\\build'
    ICON = f'{ROOT}\\assets\\icon.ico'

    command = f'pyinstaller --onefile --windowed --specpath {BUILD} --workpath {BUILD} --distpath {BUILD} --icon={ICON} --name={NAME} {MAIN}'

    process = Popen(command, shell=True, stdin=PIPE, stdout=PIPE)
    out, err = process.communicate()
    print(f'{command}\n{out.decode()}')

    rmdir(f'{BUILD}\\{NAME}')
    rmfile(f'{BUILD}\\{NAME}.spec')

    release = ZipFile(f'{ROOT}\\Releases\\{NAME}-v{VERSION}.zip', 'w')
    release.write(f'{NAME}.exe')
    release.write(f'{ROOT}\\assets')
    release.close()

    rmfile(f'{BUILD}\\{NAME}.exe')
