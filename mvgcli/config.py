import os


CONFIG_DIRECTORY = os.path.join(os.path.expanduser('~'), '.mvgcli')


def use_config_dir():
    if not os.path.isdir(CONFIG_DIRECTORY):
        os.mkdir(CONFIG_DIRECTORY)
