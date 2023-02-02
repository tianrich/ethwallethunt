import os

scripts = [
    'eth.py',
    'generate.py',
    'lines.py',
    'hunt2.py'
]

for script in scripts:
    os.system(f'python {script}')
