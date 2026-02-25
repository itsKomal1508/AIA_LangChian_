import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def save_to_sheet(user_input, output):
    try:
        print("Connecting...")

        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "credentials.json", scope
        )

        client = gspread.authorize(creds)

        sheet = client.open("AgentLogs").sheet1

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sheet.append_row([timestamp, user_input, output])

        print("✅ Row added successfully!")

    except Exception as e:
        print("❌ Error saving to Google Sheet:", e)


if __name__ == "__main__":
    save_to_sheet("Test Input", "Test Output")