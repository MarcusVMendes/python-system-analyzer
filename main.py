from dashboard.interface import ui
from system_data.process import process_module
from time import sleep


def main():
    """ Main execution of modules """
    process_module()

    """ Loop config """
    while True:
        try:
            ui.display()
            sleep(1)
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
