from subprocess import PIPE, Popen
from os import getcwd, path, pardir


if __name__ == '__main__':
    name = 'BrightnessControl'
    root = path.abspath(path.join(getcwd(), pardir))
    main = f'{root}\\main.py'
    build = f'{root}\\build'
    icon = f'{root}\\assets\\icon.ico'

    command = f'pyinstaller --onefile --windowed --specpath {build} --workpath {build} --distpath {build} --icon={icon} --name={name} {main}'

    process = Popen(command, shell=True, stdin=PIPE, stdout=PIPE)
    out, err = process.communicate()
    print(f'{command}\n{out.decode()}')
