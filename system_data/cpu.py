from dashboard.interface import ui
from psutil import cpu_freq
from utils.converters import convert_mhz_to_ghz


def get_cpu_freq():
    get_cpu_freq_mhz = cpu_freq().current
    freq_ghz = convert_mhz_to_ghz(get_cpu_freq_mhz)
    return freq_ghz


def apend_cpu_freq_to_interface():
    data = get_cpu_freq()
    interface = ui.items[1]
    interface.title = f'CPU Freq: {data:.2f} Ghz'


def cpu_module():
    apend_cpu_freq_to_interface()
