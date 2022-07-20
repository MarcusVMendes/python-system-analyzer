from psutil import cpu_freq
from dashboard.interface import ui


def get_cpu_freq():
    get_cpu_freq = cpu_freq()
    print(get_cpu_freq)


def cpu_module():
    get_cpu_freq()
