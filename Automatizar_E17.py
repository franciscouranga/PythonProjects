from time import sleep
from subprocess import call
import datetime

hora_de_ejecucion = ["17:11", "17:22", "17:45"]

while True:
    hora_actual = datetime.datetime.now().strftime("%H:%M")
    if hora_actual in hora_de_ejecucion:
        call(['python', 'E17_parsinghttps.py'])
        sleep(1200)
    else:
        sleep(30)