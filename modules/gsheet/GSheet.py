#!/usr/bin/python3

import sys
import gspread
import logging
from oauth2client.service_account import ServiceAccountCredentials

__author__ = 'nam.phuong'

class GSheet:
    logging.basicConfig(level=logging.INFO,filename='app.log', filemode='a', format='%(asctime)-15s - %(name)s - %(levelname)s - %(message)s')
    LOGGER = logging.getLogger(__name__)

    def __init__(self):
        self.__client = None
        self.__gsheet_file = None
        self.__work_sheet = None
        self.__credential_path = None
        self.__sheet = None
        self.__scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    def create_connection(self):
        GSheet.LOGGER.info("Init connection to google sheet:")
        GSheet.LOGGER.info(f'google_sheet_file: {self.__gsheet_file}, worksheet: {self.__work_sheet}')
        try:
            creds = ServiceAccountCredentials.from_json_keyfile_name(self.__credential_path, self.__scope)
            self.__client = gspread.authorize(creds)
            self.__sheet = self.__client.open(self.__gsheet_file).worksheet(self.__work_sheet)
        except Exception as ex:
            print(ex)
            GSheet.LOGGER.error(ex)
            GSheet.LOGGER.error("Terminate program...")
            sys.exit()

    @property
    def gsheet_file(self):
        return self.__gsheet_file
    
    @property
    def work_sheet(self):
        return self.__work_sheet

    @property
    def sheet(self):
        return self.__sheet
    
    @property
    def credential_path(self):
        if self.__credential_path is None:
            return "../../credentials/gdrive-api.json"
        else:
            return self.__credential_path

    @property
    def client(self):
        return self.__client

    @credential_path.setter 
    def credential_path(self, path):
        GSheet.LOGGER.info(f"Set credential file path:  {path}")
        self.__credential_path = path

    @gsheet_file.setter
    def gsheet_file(self, file_name):
        GSheet.LOGGER.info(f"Set google sheet file to:  {file_name}")
        self.__gsheet_file = file_name

    @work_sheet.setter
    def work_sheet(self, sheet_name):
        GSheet.LOGGER.info(f"Set google worksheet to:  {sheet_name}")
        self.__work_sheet = sheet_name


    def append_row(self, row_data):
        try:
            GSheet.LOGGER.info(f"Append row data to sheet {self.__work_sheet}, data: {row_data}")
            self.__sheet.append_row(row_data)
            return True
        except Exception as ex:
            print(ex)
            GSheet.LOGGER.error(ex)
            return False

    def get_all_data(self):
        GSheet.LOGGER.info(f"Get all data from worksheet: {self.__work_sheet}, gsheet: {self.__gsheet_file}")
        try:
            sheet_data = self.__sheet.get_all_records()
            return sheet_data
        except Exception as ex:
            print(ex)
            GSheet.LOGGER.error(ex)
            return None
        




