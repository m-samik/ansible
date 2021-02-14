import getpass
print("Enter the Details Below : ")
ip=input("Enter the O.s Ip : ")
username=input("Enter the Username : ")
password=getpass.getpass("Enter Your PAssword : ")
with open("hello1.txt","a") as f:
	print("\n")
	f.write("{0} ansible_user={1} ansible_ssh_pass={2} ansible_connection=ssh\n".format(ip,username,password))
