from pathlib import Path
path= Path('10.3.py')
run = path.read_text()
run = run.rstrip()
run = run.replace('lines = conects.splitlines()for line in lines:', 'for line in conects.splitlines()')          
print(run)