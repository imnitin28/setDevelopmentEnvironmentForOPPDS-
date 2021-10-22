from threading import Thread
import subprocess

t1 = Thread(target=subprocess.run, args=(["python", "Chrome.py"],))
t2 = Thread(target=subprocess.run, args=(["python", "Fork.py"],))
t3 = Thread(target=subprocess.run, args=(["python", "IntelliJ.py"],))
t4 = Thread(target=subprocess.run, args=(["python", "Slack.py"],))
t5 = Thread(target=subprocess.run, args=(["python", "Postman.py"],))
t6 = Thread(target=subprocess.run, args=(["python", "Anypoint.py"],))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
