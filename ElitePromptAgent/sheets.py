import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime


def save_to_sheet(user_input, output):
    try:
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        # Load credentials from Streamlit Secrets
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
        print("Error saving to Google Sheet:", e)
        return False