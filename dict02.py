#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3


def main():
	hostipdict = {"host01":"10.10.2.3" , "host02":"10.0.1.1" , "host03":"72.5.4.22"} 
	hostipdict["host04"] = "192.168.1.1"
	print(hostipdict)
	print(hostipdict["host02"])

main() 
