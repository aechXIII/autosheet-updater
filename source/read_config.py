import time
import yaml

def read_config(file='config.yaml'):
    try:
        with open(file, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        print(f"\n\nConfig file not found!\nMake sure that '{file}' is in the main directory.\nAutosheet-updater will close in 3 seconds.\n\n")
        time.sleep(3)
        exit()


