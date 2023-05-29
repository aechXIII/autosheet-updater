import os
import time

def scan_scenarios(files):
    maps = []

    try:
        for file in files:
            with open(file, 'r') as f:
                for line in f:
                    line = line.rstrip().lstrip()
                    maps.append(line)
        return maps
    except FileNotFoundError:
        print(f"\n\nNo files were found in './scenarios/' folder!\nMake sure that there is a file called 'aimerz.txt' that contains all all aimerz benchmarks scenarios names and 'voltaic.txt' that contains all voltaic benchmarks scenarios names.\nAutosheet-updater will close in 3 seconds.\n\n")
        time.sleep(3)
        exit()

if len(scan_scenarios(['./scenarios/aimerz.txt', './scenarios/voltaic.txt'])):
    scenarios = scan_scenarios(['./scenarios/aimerz.txt', './scenarios/voltaic.txt'])
else:
    print(f"\n\nNo files were found in './scenarios/' folder!\nMake sure that there is a file called 'aimerz.txt' that contains all all aimerz benchmarks scenarios names and 'voltaic.txt' that contains all voltaic benchmarks scenarios names.\nAutosheet-updater will close in 3 seconds.\n\n")
    time.sleep(3)
    exit()
    
def read_stats(directory, scenarios=scenarios):
    scores = {}
    try:
        for file in os.listdir(directory):
            if file.endswith('.csv'):
                file_path = os.path.join(directory, file)
                with open(file_path, 'r') as f:
                    data = f.read()

                    lines = data.strip().split('\n')

                    score = None
                    scenario = None

                    for line in reversed(lines):
                        if line.startswith("Score:"):
                            score = round(float(line.split(':,')[1].strip()), 2)
                        elif line.startswith("Scenario:"):
                            scenario = line.split(':,')[1].strip()

                        if scenario in scenarios:
                            if scenario in scores:
                                if score is not None and scores[scenario] is not None:
                                    if scores[scenario] < score:
                                        scores[scenario] = score
                                elif scores[scenario] is None:
                                    scores[scenario] = score

                            else:
                                scores[scenario] = score
    except FileNotFoundError:
        print(f"\n\nNo files were found in '{directory}'\nAutosheet-updater will close in 3 seconds.\n\n")
        time.sleep(3)
        exit()

    if len(scores):
        return scores
    else:
        print(f"\n\nNo valid files were found in '{directory}'\nAutosheet-updater will close in 3 seconds.\n\n")
        time.sleep(3)
        exit()

