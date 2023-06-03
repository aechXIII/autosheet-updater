import os
import time
import yaml

class Reader:
    @staticmethod
    def read_scenarios(files):
        maps = []

        try:
            for file in files:
                with open(file, 'r') as f:
                    maps.extend(line.rstrip().lstrip() for line in f)

            return maps
        except FileNotFoundError:
            print(f"\n\nNo files were found in './scenarios/' folder!\nMake sure that there is a file called 'aimerz.txt' that contains all all aimerz benchmarks scenarios names and 'voltaic.txt' that contains all voltaic benchmarks scenarios names.\nAutosheet-updater will close in 3 seconds.\n\n")
            time.sleep(3)
            exit()

    if read_scenarios(['./scenarios/aimerz.txt', './scenarios/voltaic.txt']):
        scenarios = read_scenarios(['./scenarios/aimerz.txt', './scenarios/voltaic.txt'])
    else:
        print(f"\n\nNo files were found in './scenarios/' folder!\nMake sure that there is a file called 'aimerz.txt' that contains all all aimerz benchmarks scenarios names and 'voltaic.txt' that contains all voltaic benchmarks scenarios names.\nAutosheet-updater will close in 3 seconds.\n\n")
        time.sleep(3)
        exit()

    @staticmethod   
    def read_stats(directory, scenarios=scenarios):
        scores = {}

        try:
            for file in os.scandir(directory):
                if file.name.endswith('.csv') and file.is_file():
                    with open(file.path, 'r') as f:
                        data = f.read()
                        lines = data.strip().split('\n')

                        scenario = None
                        score = None

                        for line in reversed(lines):
                            line = line.strip()

                            if line.startswith("Score:"):
                                score = round(float(line.split(':,')[1].strip()), 2)
                            elif line.startswith("Scenario:"):
                                scenario = line.split(':,')[1].strip()

                            if scenario in scenarios and score is not None:
                                if scenario not in scores:
                                    scores[scenario] = score
                                else:
                                    scores[scenario] = max(scores[scenario], score)
                                break
        except FileNotFoundError:
            print(f"\n\nNo files were found in '{directory}'\nAutosheet-updater will close in 3 seconds.\n\n")
            time.sleep(3)
            exit()

        if scores:
            return scores
        else:
            print(f"\n\nNo valid files were found in '{directory}'\nAutosheet-updater will close in 3 seconds.\n\n")
            time.sleep(3)
            exit()

    @staticmethod
    def read_config(file='config.yaml'):
        try:
            with open(file, 'r') as f:
                config = yaml.safe_load(f)
            return config
        except FileNotFoundError:
            print(f"\n\nConfig file not found!\nMake sure that '{file}' is in the main directory.\nAutosheet-updater will close in 3 seconds.\n\n")
            time.sleep(3)
            exit()

