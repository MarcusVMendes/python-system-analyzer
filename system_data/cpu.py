from dashboard.interface import ui
from utils.converters import convert_mhz_to_ghz
from psutil import cpu_freq, cpu_percent


def get_cpu_freq():
    get_cpu_freq_mhz = cpu_freq().current
    freq_ghz = convert_mhz_to_ghz(get_cpu_freq_mhz)
    return freq_ghz


def apend_cpu_freq_to_interface():
    data = get_cpu_freq()
    interface = ui.items[1]
    interface.title = f'CPU Freq: {data:.2f} Ghz'


def get_total_percentage_of_cpu_usage():
    total_cpu_percent_usage = cpu_percent()
    return total_cpu_percent_usage


def apend_total_cpu_percent_usage_to_interface():
    data = get_total_percentage_of_cpu_usage()
    interface = ui.items[1].items[0]
    interface.value = data
    interface.title = f'Total CPU usage: {data}%'


def cpu_module():
    apend_cpu_freq_to_interface()
    apend_total_cpu_percent_usage_to_interface()
