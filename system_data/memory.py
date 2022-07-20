from dashboard.interface import ui
from utils.converters import convert_bytes_to_gigas
from psutil import virtual_memory, swap_memory


def get_virtual_memory_infos():
    """
    Get virtual memory infos as total, available, percent, used
    in bytes and return a tuple
    """
    virtual_memory_infos = virtual_memory()
    return virtual_memory_infos


def apend_virtual_memory_infos_to_interface():
    """
    Get data from get_virtual_memory_infos function and
    apends this to dashboard interface
    """
    data = get_virtual_memory_infos()
    interface = ui.items[0].items[1].items[0].items[0]
    interface.text = f"{'RAM':>4}{'AVAILABLE(GB)':>14}{'USED(GB)':>9}{'%':>4}"

    available = convert_bytes_to_gigas(data.available)
    used = convert_bytes_to_gigas(data.used)
    percent = data.percent

    interface.text += "\n{:>4}{:>10.2f}{:>10.2f}{:>8}\n".format(
        '',
        available,
        used,
        percent
    )


def get_swap_memory_infos():
    """
    Get swap memory infos as total, percent, used
    in bytes and return a tuple
    """
    swap_memory_infos = swap_memory()
    return swap_memory_infos


def apend_swap_memory_infos_to_interface():
    """
    Get data from get_swap_infos function and
    apends this to dashboard interface
    """
    data = get_swap_memory_infos()
    interface = ui.items[0].items[1].items[0].items[0]
    interface.text += (
        f"{'SWAP':>4}{'AVAILABLE(GB)':>14}{'USED(GB)':>9}{'%':>4}"
    )

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


def apend_percent_virtual_memory_to_interface():
    """
    Get data from get_virtual_memory_infos function and
    apends this to dashboard interface
    """
    data = get_virtual_memory_infos()
    interface = interface = ui.items[0].items[1].items[0].items[1].items[0]
    percent = data.percent
    interface.value = percent


def apend_percent_swap_memory_to_interface():
    """
    Get data from get_swap_memory_infos function and
    apends this to dashboard interface
    """
    data = get_swap_memory_infos()
    interface = interface = ui.items[0].items[1].items[0].items[1].items[1]
    percent = data.percent
    interface.value = percent


def memory_module():
    # export this module to the main function
    apend_virtual_memory_infos_to_interface()
    apend_swap_memory_infos_to_interface()
    apend_percent_virtual_memory_to_interface()
    apend_percent_swap_memory_to_interface()
