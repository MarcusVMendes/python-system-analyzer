from dashboard.interface import ui
from time import sleep

while True:
    try:
        ui.display()
        sleep(1)
    except KeyboardInterrupt:
        break
