def save_to_sheet(user_input, output):
    try:
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        credentials = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=scope
        )

        client = gspread.authorize(credentials)

        sheet = client.open("AgentLogs").sheet1

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sheet.append_row([timestamp, user_input, output])

        return True

    except Exception as e:
        st.error(f"Google Sheets Error: {e}")
        return False