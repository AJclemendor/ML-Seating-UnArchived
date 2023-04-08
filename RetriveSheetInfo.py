"""
AJ Clemendor ML - Seating

Devd as a gift for Mrs. Donaldson

2023
"""


from __future__ import print_function

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time


class RetrieveSheetInfo:

    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("ML Seating (Responses)").sheet1  # Open the spreadsheet

    def __init__(self):
        self.student_data = self.get_student_data()
        self.scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                      "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("ML Seating (Responses)").sheet1  # Open the spreadsheet
        self.student_data = self.get_student_data()

    def get_student_data(self):
        raw_data = self.sheet.get_all_records()
        student_data = []

        for row in raw_data:
            student_info = {
                "id": row["Student ID # (Should Be 8 Digits)"],
                "difficult_concepts": row["What Concepts Are Most Difficult for You (Can Be altered for other classes)"],
                "best_concepts": row["What Concepts Do You Understand the Best."],
                "current_grade": row["What's Your Current Grade (In This Class)"],
                "group_work_preference": row["When Given Group Work Do You Like to Work"],
                "work_well_with": [name.strip() for name in row['Are there any students you work particularly well with?\n\nEx: Jack Smith, Annika Andersen, First Last, '].split(",")],
                "prefer_not_to_sit_with": [name.strip() for name in row["Are there any students you would prefer not to be seated next to?"].split(",")],
                "study_strategies": row["Are there any specific study strategies or techniques that work well for you?"],
                "academic_goals": row["What are your academic goals for this semester?"],
                "glasses_or_need_close": row["Do you have glasses / need to sit close"] == "Yes"
            }
            student_data.append(student_info)

        return student_data
