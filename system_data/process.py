from psutil import process_iter, pids
from dashboard.interface import ui


def process_with_cpu_usage():
    """
    Return a list of dictionaries containing pid, name, cpu_percent
    and status keys
    """
    process_list = []
    name_list = []
    for process in process_iter():
        iter_proc = process.as_dict(['pid', 'name', 'cpu_percent', 'status'])

        if '-' in iter_proc['name']:
            iter_proc['name'] = iter_proc['name'].split('-')[0]

        if '.' in iter_proc['name']:
            iter_proc['name'] = iter_proc['name'].split('.')[0]

        if iter_proc['name'] not in name_list:
            name_list.append(iter_proc['name'])
            process_list.append(iter_proc)

    process_list.sort(key=lambda k: k['cpu_percent'], reverse=True)
    return process_list[:10]


""""
Process_Iter Argument List
https://psutil.readthedocs.io/en/latest/index.html?highlight=process_iter#psutil.process_iter
"""


def apend_process_with_cpu_usage_to_interface():
    """
    Get data from process_with_cpu_usage function and
    apends this to dashboard interface
    """
    data = process_with_cpu_usage()
    interface = ui.items[0].items[0]
    interface.text = f"{'PID':>6}{'NAME':>10}{'CPU %':>10}{'STATUS':>10}\n"
    for process in data:
        interface.text += "{:>6}{:>10}{:>9}{:>12}\n".format(
            process['pid'],
            process['name'],
            process['cpu_percent'],
            process['status']
        )


def total_process_number():
    """
    Return a number of total system process
    """
    total_process = len(pids())
    return total_process


def apend_total_process_to_interface():
    """
    Get data from total_process_number function and
    apends this to dashboard interface
    """
    total_process = total_process_number()
    interface = ui.items[0].items[0]
    interface.title = f'Total System Process: {total_process}'


def process_module():
    # export this module to the main function
    apend_total_process_to_interface()
    apend_process_with_cpu_usage_to_interface()
