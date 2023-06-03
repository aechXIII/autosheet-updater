import os 
import time
import gspread
import schedule
from datetime import datetime
from source.reader import Reader
from oauth2client.service_account import ServiceAccountCredentials

class AutosheetUpdater:
    def __init__(self, config_file='config.yaml'):
        self.reader = Reader()
        self.config = self.reader.read_config(config_file)

    def authenticate(self):
        try:
            scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']  
            credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials/credentials.json', scope)
            client = gspread.authorize(credentials)
        
            return client
        except FileNotFoundError:
            print("\n\nCredentials file not found!\nMake sure you put 'credentials.json' into the 'credentials' folder!\nAutosheet-updater will close in 3 seconds.\n\n")
            time.sleep(3)
            exit()
        except Exception as e:
            print(f"\n\nInvalid credentials file!\nError: {e}\nAutosheet-updater will close in 3 seconds.\n\n")
            time.sleep(3)
            exit()

    def write_to_google_sheets(self, client, sheet_name, worksheet_name, cell_range, dictionary):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        try:
            sheet = client.open(sheet_name).worksheet(worksheet_name)
        except gspread.exceptions.SpreadsheetNotFound:
            print("\n\nSpreadsheet not found!\nMake sure spreadsheet's name in 'config.yaml' is correct!\nAutosheet-updater will close in 3 seconds.\n\n")
            time.sleep(3)
            exit()
        except gspread.WorksheetNotFound:
            print("\n\nWorksheet not found!\nMake sure worksheet's name in 'config.yaml' is correct!\nAutosheet-updater will close in 3 seconds.\n\n")
            time.sleep(3)
            exit()

        cell_values = sheet.range(cell_range)

        for cell in cell_values:
            cell_value_stripped = str(cell.value).lstrip().rstrip()
            if cell_value_stripped in dictionary:
                new_value = dictionary[cell_value_stripped]
                current_value = sheet.cell(cell.row, cell.col + 2).value

                new_highscore_message = f"\n[{current_time}]\nNew highscore!\n{cell_value_stripped} {new_value}"
                
                if current_value is None or current_value == '':
                    sheet.update_cell(cell.row, cell.col + 2, new_value)
                    print(new_highscore_message)
                elif new_value is not None and float(new_value) > float(current_value):
                    sheet.update_cell(cell.row, cell.col + 2, new_value)
                    print(new_highscore_message)

    def job(self):
        directory = self.config['directory']
        benchmarks = self.config['benchmarks']
        sheet_name = self.config['sheet_name']
        worksheet_name = self.config['worksheet_name']
        
        if benchmarks.lower() in ['vt', 'volt', 'voltaic']:
            cell_range = 'C3:C18'
        elif benchmarks.lower() in ['aimerz', 'aimerz+']:
            cell_range = 'E3:E20'
        else:
            print("\n\nBenchmarks not found!\nMake sure benchmark's name in 'config.yaml' is correct!\nAutosheet-updater will close in 3 seconds.\n\n")
            time.sleep(3)
            exit()

        dictionary = self.reader.read_stats(directory)
        client = self.authenticate()

        self.write_to_google_sheets(
            client=client,
            sheet_name=sheet_name, 
            worksheet_name=worksheet_name,
            cell_range=cell_range,
            dictionary=dictionary)

    def main(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Autosheet-updater is running...\nScores will be updated every minute.')
            self.job()
            schedule.every(1).minutes.do(self.job)

            while True:
                try:
                    schedule.run_pending()
                    time.sleep(1)
                except Exception as e:
                    print(f'An error occurred during job execution: {str(e)}')

        except KeyboardInterrupt:
            print('\n\nAutosheet-updater will close in 3 seconds.')
            time.sleep(3)
            exit()

if __name__ == "__main__":
    autoshetupdater = AutosheetUpdater()
    autoshetupdater.main()
