import gspread
import datetime
from google.oauth2.credentials import Credentials
from login_gsheet import SCOPES, TOKEN_LOCATION

gsheet_client = gspread.Client(Credentials.from_authorized_user_file(TOKEN_LOCATION, SCOPES))
spreadsheet = gsheet_client.open_by_url('https://docs.google.com/spreadsheets/d/1PaFime-HZc-U9Zt3MwzZLolC5BMQWTauUuqZ_JRNIhI/edit#gid=0')
sheet = spreadsheet.worksheet('random unstructured running time')
all_records = sheet.get_all_values()

for record in all_records:
    if record[0] or record[1]:
        start_time = datetime.datetime.strptime(record[0], '%Y-%m-%d %H:%M:%S.%f')
        finish_time = datetime.datetime.strptime(record[1], '%Y-%m-%d %H:%M:%S.%f')
        print("%.5f" % (finish_time - start_time).total_seconds())
    else:
        print()
