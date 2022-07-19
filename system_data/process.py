from psutil import process_iter


def process_with_cpu_usage():
    process_list = []
    for process in process_iter():
        iter_proc = process.as_dict(['ppid', 'name', 'cpu_percent',  'status'])
        process_list.append(iter_proc)

    print(process_list)


process_with_cpu_usage()

""""
as_dict Argument List
https://psutil.readthedocs.io/en/latest/index.html?highlight=process_iter#psutil.process_iter
"""
