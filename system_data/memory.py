from dashboard.interface import ui
from psutil import virtual_memory, swap_memory


def get_virtual_memory():
    vmem = virtual_memory().as_dict(['total', 'avaliable', 'used', 'percent'])