from dashboard.interface import ui
from time import sleep
from system_data.process import process_module
from system_data.cpu import cpu_module
from system_data.memory import memory_module


def main():
    while True:
        """ Main execution of modules """
        process_module()
        cpu_module()
        memory_module()

        """ Loop config """
        try:
            ui.display()
            sleep(1)
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
