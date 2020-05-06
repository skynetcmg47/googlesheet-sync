from modules.gsheet.GSheet import GSheet
import json


conf_path = "./conf/gsheet/gsheet.json"

def load_conf():
	conf = None
	with open(conf_path) as f:
		conf = json.load(f)

	return conf

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





