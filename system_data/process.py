from psutil import process_iter
from dashboard.interface import ui


def process_with_cpu_usage():
    process_list = []
    for process in process_iter():
        iter_proc = process.as_dict(['pid', 'name', 'cpu_percent', 'status'])
        process_list.append(iter_proc)

    process_list.sort(key=lambda k: k['name'], reverse=True)
    # print(process_list)
    return process_list


""""
Process_Iter Argument List
https://psutil.readthedocs.io/en/latest/index.html?highlight=process_iter#psutil.process_iter
"""


def apend_data_to_interface():
    data = process_with_cpu_usage()
    interface = ui.items[0].items[0]
    interface.text += f"{'PID':>6}{'NAME':>10}{'CPU %':>10}{'STATUS':>10}\n"

    for process in data[:10]:
        interface.text += "{:>7}{:>9}{:>10}{:>12}\n".format(
            process['pid'],
            process['name'],
            process['cpu_percent'],
            process['status']
        )


def process_module():
    apend_data_to_interface()
