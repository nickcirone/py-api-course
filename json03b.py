#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
"""ncirone@cisco.com || reading in json files"""

import json

def main():
	# open up datacenter.json and convert it to pythonic data
	with open("datacenter.json", "r") as datacenter:
		myData = json.load(datacenter)

	# print out each row - line by line
	print("Printing JSON file")
	print("-----------")
	print(myData["row1"])
	print(myData["row2"])
	print(myData["row3"])


main()
