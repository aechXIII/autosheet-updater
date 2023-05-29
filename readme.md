# Autosheet-Updater
Simple tool to make your life a little bit easier, by autofilling your spreadsheet.  
Currently, it works only with Aimerz+ and Voltaic's progression sheets, in future all sheets should be supported after simple configuration.

## Installation
### Prerequisites:
- JSON credentials file
- sheet modifying permission
- latest release downloaded.


#### How to get the JSON credentials file:
1. Head to [Google Developers Console](https://console.developers.google.com/), create new project (name doesn't matter).
2. Click `Enabled APIs & Services` -> `ENABLE APIS AND SERVICES`, search for "Google Drive API" and "Google Sheets API", enable both of them. 
3. After enabling needed API's go to `Credentials` -> `CREATE CREDENTIALS` -> `SERVICE ACCOUNT`. Fill the form and press `CREATE AND CONTINUE`, press `DONE`. 
  
   **Email address shown under *'Service account ID'* will be needed later, so you can save it now.**

4. In the "Service Accounts" section, click on the account you just created. Go to `KEYS` tab -> `ADD KEY`, make sure that **JSON** is selected. Press `CREATE`, file will be downloaded automatically.
5. Rename the file you just got to "credentials.json".
6. Done, you got the JSON credentials file. 

### How to give the sheet modifying permission to Autosheet-updater:
1. Open your progress sheet in a web browser.
2. Press `SHARE` button.
3. Paste the service account's email address in "Add people and groups" field.
4. Press `DONE`.

   #### If you didn't save the email address earlier:
   1. Head to [Google Developers Console](https://console.developers.google.com/).
   2. Go to `Credentials` tab.
   3. Your email address will be shown in the "Service Accounts" section.

### Configuration:
Before going to the next step, make sure to configure the config.yaml file with the necessary settings.
```yaml
# +-------------------------------------+
# |config.yaml                          |
# |Every setting here is case sensitive!|
# +-------------------------------------+

#Default directory is 'C:/Program Files (x86)/Steam/steamapps/common/FPSAimTrainer/FPSAimTrainer/stats'
#Make sure that you use '/', not '\'.
directory: ''
sheet_name: ''
worksheet_name: ''

#Currently only 'voltaic' and 'aimerz' are supported!
benchmarks: ''
```
   - **directory** - directory where the code will search for csv files containing scores
   - **sheet_name** - the name of the Google Sheets document
   - **worksheet_name** - the name of the worksheet within the Google Sheets document, for example 'NORMAL' or 'HARD' for Aimerz+ benchmarks and 'Novice', 'Intermediate' or 'Advanced' for Voltaic benchmarks.
   - **benchmarks** - Autosheet-Updater currently supports only 'voltaic' and 'aimerz' benchmarks.

#### Example config:
```yaml
# +-------------------------------------+
# |config.yaml                          |
# |Every setting here is case sensitive!|
# +-------------------------------------+

#Default directory is 'C:/Program Files (x86)/Steam/steamapps/common/FPSAimTrainer/FPSAimTrainer/stats'
#Make sure that you use '/', not '\'.
directory: 'C:/Program Files (x86)/Steam/steamapps/common/FPSAimTrainer/FPSAimTrainer/stats'
sheet_name: '2023 aimerz+ Benchmarks'
worksheet_name: 'HARD'

#Currently only 'voltaic' and 'aimerz' are supported!
benchmarks: 'aimerz'
```
### Usage:
1. Download and unzip the latest release.
2. Set up your config file.
3. Put the `credentials.json` file into the `credentials` folder, located in the main directory.
4. Run `autosheet-updater.exe`, scores will be updated every one minute.

### Alternatively, you can run it using the source code:
#### Additional requirements:
- Python 3.8+ installed
- Required Python packages: `gspread`, `schedule`, `oauth2client`, `pyyaml`.

1. Clone the repo via command or do it manually.
   ```shell
   $ git clone https://github.com/aechXIII/autosheet-updater
   ```
2. ```shell
   $ cd autosheet-updater
   ```
3. Install required packages
   ```shell
   $ pip install -r requirements.txt
   ```
4. Set up the `config.yaml` file.
5. Put your `credentials.json` file into the `credentials` folder.
4. Run the code, scores will be updated every one minute.
   ```shell
   $ py autosheet-updater.py
   ```

