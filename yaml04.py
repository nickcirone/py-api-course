#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import yaml

def main():
	with open ("datacenter.yaml", "r") as yammy:
		pyyam = yaml.load(yammy)

	print(pyyam)

main()
