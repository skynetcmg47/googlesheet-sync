#!/usr/bin/python3
from modules.gsheet.GSheet import GSheet
import json
import logging
import sys

conf_path = "./conf/gsheet/gsheet.json"
logging.basicConfig(level=logging.INFO,filename='app.log', filemode='a', format='%(asctime)-15s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

def load_conf():
	try:
		conf = None
		LOGGER.info(f"Load config from: {conf_path}")
		with open(conf_path) as f:
			conf = json.load(f)
		return conf
	except Exception as ex:
		print(ex)
		LOGGER.error(ex)
		sys.exit()
		

if __name__ == "__main__":
	gsheet =  GSheet()
	conf = load_conf()

	gsheet.gsheet_file = conf['spreadSheet']
	gsheet.work_sheet = conf['worksheet']
	gsheet.credential_path = conf['credentialPath']

	gsheet.create_connection()
	data  = gsheet.get_all_data()
	print(data)

	# gsheet.append_row(["java", 100])
	# data = gsheet.get_all_data()
	# print(data)





