from dashboard.interface import ui
from utils.converters import convert_bytes_to_gigas
from psutil import virtual_memory, swap_memory


def get_virtual_memory_infos():
    virtual_memory_infos = virtual_memory()
    return virtual_memory_infos


def apend_virtual_memory_infos_to_interface():
    data = get_virtual_memory_infos()
    interface = ui.items[0].items[1].items[0].items[0]
    interface.text = f"{'RAM':>4}{'AVAILABLE(GB)':>14}{'USED(GB)':>9}{'%':>4}"

    available = convert_bytes_to_gigas(data.available)
    used = convert_bytes_to_gigas(data.used)
    percent = data.percent

    interface.text += "\n{:>4}{:>10.2f}{:>10.2f}{:>8}".format(
        '',
        available,
        used,
        percent
    )


def get_swap_memory_infos():
    swap_memory_infos = swap_memory()
    return swap_memory_infos


def apend_swap_memory_infos_to_interface():
    data = get_swap_memory_infos()
    interface = ui.items[0].items[1].items[0].items[0]
    interface.text += f"\n{'SWAP':>4}{'AVAILABLE(GB)':>14}{'USED(GB)':>9}{'%':>4}"

    swap_available = swap_memory().total - swap_memory().used
    available = convert_bytes_to_gigas(swap_available)
    used = convert_bytes_to_gigas(data.used)
    percent = data.percent

    interface.text += "\n{:>4}{:>10.2f}{:>10.2f}{:>8}".format(
        '',
        available,
        used,
        percent
    )


def memory_module():
    apend_virtual_memory_infos_to_interface()
    apend_swap_memory_infos_to_interface()
