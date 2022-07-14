import subprocess
cmd="python gui.py"
cmd2="python instrukcja.py"
p=subprocess.Popen(cmd,shell=True)
out,err=p.communicate()
print(err)
print(out)
