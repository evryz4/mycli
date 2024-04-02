import os, platform

command = 'pip install pyuac pypiwin32 clearterminal'
os.system(command=command)

from pyuac import main_requires_admin
from clearterminal import system

clipath = os.path.join(os.path.dirname(__file__), 'mycli')
if system == 'Windows':
    sys32path = os.path.join(os.environ['SystemRoot'], 'SysNative' if 
    platform.architecture()[0] == '32bit' else 'System32', 'mycli.bat')

    command = f'python3 {clipath}'

    @main_requires_admin
    def create_file():
        with open(sys32path, 'w') as file:
            file.write(command)

    create_file()
else:
    os.system(f'echo \'alias mycli="python3 {clipath}"\' >> ~/.bashrc')

print('You need to just enter "mycli" in cmd/terminal to open MyCLI')