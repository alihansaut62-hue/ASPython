from pathlib import Path
path= Path('text')
run = path.read_text()
run = run.rstrip()
run = run.replace('python', 'C')          
print(run)