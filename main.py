from dashboard.interface import ui
from system_data.process import process_module
from system_data.cpu import cpu_module
from time import sleep


def main():
    while True:
        """ Main execution of modules """
        process_module()
        cpu_module()

        """ Loop config """
        try:
            ui.display()
            sleep(1)
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
