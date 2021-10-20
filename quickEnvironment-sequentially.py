import subprocess

program_list = ['Anypoint.py', 'Chrome.py', 'Fork.py', 'IntelliJ.py','Postman.py', 'Slack.py']

for program in program_list:
    subprocess.call(['python', program])
    print("Finished:" + program)