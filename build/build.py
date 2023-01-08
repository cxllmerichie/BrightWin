import subprocess


name = 'BrightnessControl'
root = 'C:\\Projects\\Python\\BrightnessControl-Desktop-'
main = f'{root}\\main.py'
build = f'{root}\\build'
icon = f'{root}\\src\\assets\\icon.ico'

command = f'pyinstaller --onefile --windowed --specpath {build} --workpath {build} --distpath {build} --icon={icon} --name={name} {main}'

process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, err = process.communicate()
print(f'{command}\n{out.decode()}')
