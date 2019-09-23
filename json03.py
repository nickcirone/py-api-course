#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import json

def main():
	hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},{"name": "Arthur Dent", "species": "Human"},{"name": "Marvin the Paranoid Android", "species": None}]
	print(hitchhikers)

	with open("guide.galaxy", "w") as guide:
		json.dump(hitchhikers, guide)

main()
