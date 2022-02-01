import subprocess
import sys
modules = ['discord', 'plotly', 'numpy', 'sympy', 'requests']

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if input('Do you want to install the required pip modules? Y/N: \n').upper() == 'Y':
    for module in modules:
      install(module)
