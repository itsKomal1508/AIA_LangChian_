import gspread
from oauth2client.service_account import ServiceAccountCredentials

def save_to_sheet(user_input, result):
    try:
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "credentials.json",
            scope
        )

        client = gspread.authorize(creds)

        sheet = client.open("AgentLogs").sheet1

        sheet.append_row([user_input, result])

    except Exception as e:
        raise Exception(f"Google Sheets Error: {e}")